#!/usr/bin/env python3
"""Verify, install, or remove the private TSK-0243 AdGuard Home rewrite."""

from __future__ import annotations

import argparse
import base64
import ipaddress
import json
import subprocess
import urllib.request
from pathlib import Path

import yaml


PINNED_VERSION = "v0.107.79"
RULE_PREFIX = "/^[0-9a-f]{32}\\.verify\\.usesafeweb\\.com$/$dnsrewrite=NOERROR;A;"
TEMPLATE = Path(__file__).with_name("rule.template")


def fail(message: str) -> None:
    raise SystemExit(f"ADGUARD_REWRITE=FAIL {message}")


def read_credentials(path: Path) -> tuple[str, str]:
    if not path.is_file() or path.stat().st_mode & 0o077:
        fail("credential file missing or permissions exceed 0600")
    values = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        if "=" in line and not line.lstrip().startswith("#"):
            key, value = line.split("=", 1)
            values[key.strip()] = value.strip()
    username = values.get("ADGUARD_ADMIN_USER", "")
    password = values.get("ADGUARD_ADMIN_PASSWORD", "")
    if not username or not password:
        fail("credential input incomplete")
    return username, password


class ControlAPI:
    def __init__(self, base: str, username: str, password: str) -> None:
        if base != "http://127.0.0.1:3000/control":
            fail("control API must be loopback-only")
        self.base = base
        token = base64.b64encode(f"{username}:{password}".encode()).decode()
        self.headers = {"Authorization": f"Basic {token}"}

    def request(self, path: str, payload: dict | None = None) -> dict:
        body = None if payload is None else json.dumps(payload, separators=(",", ":")).encode()
        headers = dict(self.headers)
        if body is not None:
            headers["Content-Type"] = "application/json"
        request = urllib.request.Request(self.base + path, data=body, headers=headers)
        with urllib.request.urlopen(request, timeout=10) as response:
            data = response.read()
        return json.loads(data) if data else {}


def validate_privacy(api: ControlAPI, config_path: Path | None = None) -> None:
    querylog = api.request("/querylog/config")
    statistics = api.request("/stats/config")
    if querylog.get("enabled") is not False:
        fail("querylog privacy invariant is not disabled")
    if statistics.get("enabled") is not False:
        fail("statistics privacy invariant is not disabled")
    if config_path is not None:
        if not config_path.is_file():
            fail("AdGuard configuration missing")
        config = yaml.safe_load(config_path.read_text(encoding="utf-8")) or {}
        query_config = config.get("querylog") or {}
        statistics_config = config.get("statistics") or {}
        dns = config.get("dns") or {}
        filtering = config.get("filtering") or {}
        if query_config.get("enabled") is not False or query_config.get("file_enabled") is not False:
            fail("persistent querylog privacy invariant is not disabled")
        if statistics_config.get("enabled") is not False:
            fail("identifiable statistics privacy invariant is not disabled")
        if dns.get("anonymize_client_ip") is not True:
            fail("client anonymization privacy invariant is not enabled")
        if (dns.get("edns_client_subnet") or {}).get("enabled") is not False:
            fail("ECS privacy invariant is not disabled")
        if filtering.get("protection_enabled") is not True or filtering.get("filtering_enabled") is not True:
            fail("filtering protection invariant is not enabled")


def render_rule(value: str) -> str:
    try:
        address = ipaddress.ip_address(value)
    except ValueError:
        fail("verifier address is invalid")
    if address.version != 4 or any(
        (address.is_unspecified, address.is_loopback, address.is_link_local, address.is_multicast)
    ):
        fail("verifier address is not an eligible IPv4 address")
    rule = TEMPLATE.read_text(encoding="utf-8").strip().replace("__VERIFIER_IPV4__", str(address))
    if "__" in rule or not rule.startswith(RULE_PREFIX):
        fail("rule template is invalid")
    return rule


def main() -> None:
    parser = argparse.ArgumentParser()
    modes = parser.add_mutually_exclusive_group(required=True)
    modes.add_argument("--verify", action="store_true")
    modes.add_argument("--apply", action="store_true")
    modes.add_argument("--remove", action="store_true")
    parser.add_argument("--verifier-ipv4", required=True)
    parser.add_argument("--credentials", type=Path, default=Path("/var/lib/usesafeweb/adguard/admin.env"))
    parser.add_argument("--binary", default="/opt/AdGuardHome/AdGuardHome")
    parser.add_argument("--config", type=Path, default=Path("/opt/AdGuardHome/AdGuardHome.yaml"))
    parser.add_argument("--base", default="http://127.0.0.1:3000/control")
    args = parser.parse_args()
    version = subprocess.run(
        [args.binary, "--version"], check=True, capture_output=True, text=True, timeout=10
    ).stdout
    if PINNED_VERSION not in version.split():
        fail("unsupported AdGuard Home version")
    username, password = read_credentials(args.credentials)
    api = ControlAPI(args.base, username, password)
    validate_privacy(api, args.config)
    desired = render_rule(args.verifier_ipv4)
    status = api.request("/filtering/status")
    original = list(status.get("user_rules") or [])
    managed = [rule for rule in original if rule.startswith(RULE_PREFIX)]
    if len(managed) > 1:
        fail("conflicting managed rewrite rules")
    mode = "--apply" if args.apply else "--remove" if args.remove else "--verify"
    if mode == "--verify":
        if managed != [desired]:
            fail("required rewrite is missing or points elsewhere")
    else:
        candidate = [rule for rule in original if not rule.startswith(RULE_PREFIX)]
        if mode == "--apply":
            candidate.append(desired)
        try:
            api.request("/filtering/set_rules", {"rules": candidate})
            after = list((api.request("/filtering/status").get("user_rules") or []))
            if after != candidate:
                raise RuntimeError("post-change verification mismatch")
            validate_privacy(api)
        except Exception:
            api.request("/filtering/set_rules", {"rules": original})
            fail("change failed; original rules restored")
    print(f"ADGUARD_VERSION={PINNED_VERSION}")
    print("ADGUARD_PRIVACY_INVARIANTS=PASS")
    print("ADGUARD_REWRITE=PASS")


if __name__ == "__main__":
    main()
