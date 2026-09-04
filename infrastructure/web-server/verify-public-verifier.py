#!/usr/bin/env python3
"""Deterministic TSK-0243 preflight and explicitly authorized target proof.

Default mode performs synthetic DNS queries, TLS, GET health, and negative GET
routing only.  Functional verifier POSTs require the exact authority phrase.
Raw tokens are never printed.
"""

from __future__ import annotations

import argparse
import http.client
import json
import secrets
import socket
import ssl
import struct
import time
import urllib.parse


AUTHORITY = "TSK-0243-TARGET-PROOF"
PROBE_PATH = "/api/dns-verification/probes"


class BoundaryFailure(Exception):
    def __init__(self, code: int, boundary: str, detail: str) -> None:
        super().__init__(detail)
        self.code, self.boundary = code, boundary


def dns_query(host: str, resolver: str, doh: bool = False) -> list[str]:
    identifier = secrets.randbelow(65536)
    labels = b"".join(bytes([len(label)]) + label.encode("ascii") for label in host.split(".")) + b"\0"
    wire = struct.pack("!HHHHHH", identifier, 0x0100, 1, 0, 0, 0) + labels + struct.pack("!HH", 1, 1)
    if doh:
        url = urllib.parse.urlparse(resolver)
        if url.scheme != "https" or not url.hostname:
            raise BoundaryFailure(67, "USESAFEWEB_DNS", "DoH URL must be HTTPS")
        connection = http.client.HTTPSConnection(url.hostname, url.port or 443, timeout=8)
        connection.request(
            "POST", url.path or "/dns-query", wire,
            {"Content-Type": "application/dns-message", "Accept": "application/dns-message"},
        )
        response = connection.getresponse()
        data = response.read()
        if response.status != 200:
            raise BoundaryFailure(67, "USESAFEWEB_DNS", f"DoH returned HTTP {response.status}")
    else:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client:
            client.settimeout(5)
            client.sendto(wire, (resolver, 53))
            data = client.recvfrom(4096)[0]
    if len(data) < 12 or struct.unpack("!H", data[:2])[0] != identifier:
        raise BoundaryFailure(66, "DNS_RESPONSE", "invalid DNS response")
    _, flags, qd, answers, _, _ = struct.unpack("!HHHHHH", data[:12])
    if flags & 0xF not in (0, 3):
        raise BoundaryFailure(66, "DNS_RESPONSE", f"DNS rcode={flags & 0xF}")

    def skip_name(offset: int) -> int:
        while offset < len(data):
            length = data[offset]
            if length & 0xC0 == 0xC0:
                return offset + 2
            offset += 1
            if length == 0:
                return offset
            offset += length
        raise BoundaryFailure(66, "DNS_RESPONSE", "truncated DNS name")

    offset = 12
    for _ in range(qd):
        offset = skip_name(offset) + 4
    addresses = []
    for _ in range(answers):
        offset = skip_name(offset)
        record_type, record_class, _, length = struct.unpack("!HHIH", data[offset : offset + 10])
        offset += 10
        value = data[offset : offset + length]
        offset += length
        if record_type == 1 and record_class == 1 and length == 4:
            addresses.append(socket.inet_ntoa(value))
    return addresses


def https_request(host: str, address: str, method: str, path: str, body: bytes = b"", headers=None):
    context = ssl.create_default_context()
    raw = socket.create_connection((address, 443), timeout=8)
    wrapped = context.wrap_socket(raw, server_hostname=host)
    supplied = {"Host": host, "Connection": "close", "Content-Length": str(len(body)), **(headers or {})}
    request = f"{method} {path} HTTP/1.1\r\n" + "".join(f"{k}: {v}\r\n" for k, v in supplied.items()) + "\r\n"
    wrapped.sendall(request.encode() + body)
    response = http.client.HTTPResponse(wrapped)
    response.begin()
    payload, status = response.read(), response.status
    wrapped.close()
    return status, payload


def app_request(origin: str, method: str, path: str, value=None):
    url = urllib.parse.urlparse(origin)
    connection = http.client.HTTPSConnection(url.hostname, url.port or 443, timeout=8)
    body = b"" if value is None else json.dumps(value, separators=(",", ":")).encode()
    headers = {"Content-Type": "application/json", "Content-Length": str(len(body))}
    connection.request(method, path, body, headers)
    response = connection.getresponse()
    payload = response.read()
    return response.status, json.loads(payload) if payload else {}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--application-origin", required=True)
    parser.add_argument("--usesafeweb-doh", required=True)
    parser.add_argument("--public-dns", default="1.1.1.1")
    parser.add_argument("--functional-authority")
    parser.add_argument("--expect-removed", action="store_true")
    parser.add_argument("--wait-for-expiry", action="store_true")
    parser.add_argument("--rate-test-count", type=int, default=0, choices=range(0, 21), metavar="0..20")
    args = parser.parse_args()
    challenge = secrets.token_hex(16)
    host = f"{challenge}.verify.usesafeweb.com"
    current_boundary = "ARGUMENTS"
    try:
        current_boundary = "APPLICATION_HEALTH"
        status, health = app_request(args.application_origin, "GET", "/api/health/ready")
        if status != 200 or health.get("ready") is not True:
            raise BoundaryFailure(65, "APPLICATION_HEALTH", f"HTTP {status}")
        print("APPLICATION_HEALTH=PASS")

        current_boundary = "PUBLIC_DNS_NEGATIVE"
        if dns_query(host, args.public_dns):
            raise BoundaryFailure(66, "PUBLIC_DNS_NEGATIVE", "ordinary public DNS returned an A record")
        print("PUBLIC_DNS_NEGATIVE=PASS")
        current_boundary = "USESAFEWEB_DNS_POSITIVE"
        private_addresses = dns_query(host, args.usesafeweb_doh, doh=True)
        if args.expect_removed:
            if private_addresses:
                raise BoundaryFailure(67, "VERIFIER_REMOVAL", "private rewrite still returns an A record")
            print("VERIFIER_REMOVAL=PASS")
            return
        if len(private_addresses) != 1:
            raise BoundaryFailure(67, "USESAFEWEB_DNS_POSITIVE", "expected exactly one verifier A record")
        address = private_addresses[0]
        print("USESAFEWEB_DNS_POSITIVE=PASS")

        current_boundary = "TLS_OR_PATH_RESTRICTION"
        status, _ = https_request(host, address, "GET", "/")
        if status != 404:
            raise BoundaryFailure(68, "TLS_OR_PATH_RESTRICTION", f"unrelated path returned HTTP {status}")
        print("TLS_CHAIN_HOSTNAME=PASS")
        print("CHALLENGE_PATH_RESTRICTION=PASS")
        current_boundary = "DIRECT_IP_TLS"
        try:
            https_request("127.0.0.1", address, "GET", "/")
            raise BoundaryFailure(68, "DIRECT_IP_TLS", "direct-IP TLS unexpectedly authenticated")
        except ssl.SSLCertVerificationError:
            print("DIRECT_IP_TLS=PASS")

        if args.functional_authority is None:
            print("FUNCTIONAL_TARGET_PROOF=NOT_RUN_EXPLICIT_AUTHORITY_REQUIRED")
            return
        if args.functional_authority != AUTHORITY:
            raise BoundaryFailure(64, "FUNCTIONAL_AUTHORITY", "authority phrase mismatch")

        current_boundary = "REQUEST_API"
        scope = secrets.token_hex(16)
        status, issued = app_request(args.application_origin, "POST", "/api/dns-verification/requests", {"scope": scope})
        if status != 201 or issued.get("probeHost") != host:
            # The server owns its random challenge; re-query both paths for that exact host.
            host = issued.get("probeHost", "")
            if status != 201 or not host.endswith(".verify.usesafeweb.com"):
                raise BoundaryFailure(69, "REQUEST_API", f"HTTP {status}")
            current_boundary = "PUBLIC_DNS_NEGATIVE"
            if dns_query(host, args.public_dns):
                raise BoundaryFailure(66, "PUBLIC_DNS_NEGATIVE", "issued host resolved publicly")
            current_boundary = "USESAFEWEB_DNS_POSITIVE"
            private_addresses = dns_query(host, args.usesafeweb_doh, doh=True)
            if len(private_addresses) != 1:
                raise BoundaryFailure(67, "USESAFEWEB_DNS_POSITIVE", "issued host did not privately resolve")
            address = private_addresses[0]
        current_boundary = "PROBE_API"
        request_token = issued["requestToken"]
        status, payload = https_request(
            host, address, "POST", PROBE_PATH, request_token.encode(),
            {"Origin": args.application_origin, "Content-Type": "text/plain"},
        )
        if status != 200:
            raise BoundaryFailure(70, "PROBE_API", f"HTTP {status}")
        observation_token = json.loads(payload)["observationToken"]
        current_boundary = "RESULT_API"
        status, result = app_request(
            args.application_origin, "POST", "/api/dns-verification/results",
            {"requestToken": request_token, "observationToken": observation_token},
        )
        if status != 200 or result.get("reasonCode") != "TECH_VERIFIED":
            raise BoundaryFailure(71, "RESULT_API", f"HTTP {status}")
        print("REQUEST_PROBE_RESULT=PASS tokens=REDACTED")

        current_boundary = "HOST_ABUSE"
        wrong_host = "f" * 32 + ".verify.usesafeweb.com"
        current_boundary = "ORIGIN_ABUSE"
        status, _ = https_request(
            wrong_host, address, "POST", PROBE_PATH, request_token.encode(),
            {"Origin": args.application_origin, "Content-Type": "text/plain"},
        )
        if status not in (403, 421):
            raise BoundaryFailure(72, "HOST_ABUSE", f"HTTP {status}")
        status, _ = https_request(
            host, address, "POST", PROBE_PATH, request_token.encode(),
            {"Origin": "https://invalid.example", "Content-Type": "text/plain"},
        )
        if status != 403:
            raise BoundaryFailure(73, "ORIGIN_ABUSE", f"HTTP {status}")
        print("HOST_ORIGIN_ABUSE=PASS")
        current_boundary = "RATE_CONTROL"
        if args.rate_test_count:
            statuses = [
                https_request(
                    host, address, "POST", PROBE_PATH, request_token.encode(),
                    {"Origin": args.application_origin, "Content-Type": "text/plain"},
                )[0]
                for _ in range(args.rate_test_count)
            ]
            if 429 not in statuses:
                raise BoundaryFailure(76, "RATE_CONTROL", "no HTTP 429 observed")
            print("RATE_CONTROL=PASS")
        else:
            print("RATE_CONTROL=NOT_RUN_USE_--rate-test-count")

        current_boundary = "REPLAY_SCOPE"
        second_status, second = app_request(
            args.application_origin, "POST", "/api/dns-verification/requests", {"scope": scope}
        )
        status, _ = app_request(
            args.application_origin, "POST", "/api/dns-verification/results",
            {"requestToken": second.get("requestToken"), "observationToken": observation_token},
        )
        if second_status != 201 or status != 403:
            raise BoundaryFailure(74, "REPLAY_SCOPE", f"HTTP {status}")
        print("REPLAY_SCOPE=PASS")
        if args.wait_for_expiry:
            current_boundary = "EXPIRY"
            delay = max(0, issued["expiresAt"] - int(time.time() * 1000) + 1000) / 1000
            time.sleep(delay)
            status, _ = app_request(
                args.application_origin, "POST", "/api/dns-verification/results",
                {"requestToken": request_token, "observationToken": observation_token},
            )
            if status != 403:
                raise BoundaryFailure(75, "EXPIRY", f"HTTP {status}")
            print("EXPIRY=PASS")
        else:
            print("EXPIRY=NOT_RUN_USE_--wait-for-expiry")
        print("FUNCTIONAL_TARGET_PROOF=PASS")
    except BoundaryFailure as failure:
        print(f"{failure.boundary}=FAIL detail={failure}")
        raise SystemExit(failure.code)
    except Exception as unexpected:
        print(f"{current_boundary}=FAIL detail=transport_or_schema_error:{type(unexpected).__name__}")
        raise SystemExit(77)


if __name__ == "__main__":
    main()
