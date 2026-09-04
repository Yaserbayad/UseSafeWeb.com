#!/usr/bin/env python3
"""Render the verifier nginx vhost after fail-closed wildcard TLS checks."""

from __future__ import annotations

import argparse
import os
import re
import subprocess
import tempfile
from pathlib import Path


WILDCARD = "*.verify.usesafeweb.com"
ROOT = Path(__file__).resolve().parent
TEMPLATE = ROOT / "nginx" / "usesafeweb-verifier.conf.template"


def openssl(*args: str) -> str:
    result = subprocess.run(
        ["openssl", *args], check=True, capture_output=True, text=True, timeout=10
    )
    return result.stdout


def validate_tls(certificate: Path, private_key: Path) -> None:
    if not certificate.is_file() or not private_key.is_file():
        raise SystemExit("TLS_INPUT=FAIL missing certificate or private key")
    if os.name != "nt" and private_key.stat().st_mode & 0o077:
        raise SystemExit("TLS_INPUT=FAIL private key must not be group/world accessible")
    openssl("x509", "-checkend", "0", "-in", str(certificate), "-noout")
    san = openssl("x509", "-in", str(certificate), "-noout", "-ext", "subjectAltName")
    names = re.findall(r"DNS:([^,\s]+)", san)
    if WILDCARD not in names:
        raise SystemExit("TLS_INPUT=FAIL exact wildcard SAN missing")
    with tempfile.TemporaryDirectory(prefix="usesafeweb-tls-") as directory:
        cert_pub = Path(directory) / "cert.pub"
        key_pub = Path(directory) / "key.pub"
        cert_pub.write_text(openssl("x509", "-in", str(certificate), "-pubkey", "-noout"))
        key_pub.write_text(openssl("pkey", "-in", str(private_key), "-pubout"))
        if cert_pub.read_bytes() != key_pub.read_bytes():
            raise SystemExit("TLS_INPUT=FAIL certificate/private-key mismatch")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--certificate", type=Path, required=True)
    parser.add_argument("--private-key", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--nginx-test", action="store_true")
    args = parser.parse_args()
    validate_tls(args.certificate, args.private_key)
    rendered = TEMPLATE.read_text(encoding="utf-8")
    rendered = rendered.replace("__TLS_CERTIFICATE__", str(args.certificate.resolve()))
    rendered = rendered.replace("__TLS_PRIVATE_KEY__", str(args.private_key.resolve()))
    if "__TLS_CERTIFICATE__" in rendered or "__TLS_PRIVATE_KEY__" in rendered:
        raise SystemExit("NGINX_RENDER=FAIL unresolved configuration input")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    temporary = args.output.with_suffix(args.output.suffix + ".tmp")
    temporary.write_text(rendered, encoding="utf-8")
    os.chmod(temporary, 0o644)
    temporary.replace(args.output)
    if args.nginx_test:
        subprocess.run(["nginx", "-t"], check=True, timeout=10)
    print("TLS_WILDCARD_VALIDATION=PASS")
    print("NGINX_VERIFIER_RENDER=PASS")


if __name__ == "__main__":
    main()
