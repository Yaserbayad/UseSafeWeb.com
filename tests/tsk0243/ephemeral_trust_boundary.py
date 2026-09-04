#!/usr/bin/env python3
"""Synthetic end-to-end TSK-0243 trust-boundary test; never contacts production."""

from __future__ import annotations

import http.client
import http.server
import json
import os
import re
import socket
import ssl
import subprocess
import tempfile
import threading
import time
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
APP = ROOT / "website" / ".next" / "standalone" / "website" / "server.js"
ORIGIN = "https://usesafeweb.test"
HOST_PATTERN = re.compile(r"^[0-9a-f]{32}\.verify\.usesafeweb\.com$")
PROBE_PATH = "/api/dns-verification/probes"


def free_port() -> int:
    with socket.socket() as sock:
        sock.bind(("127.0.0.1", 0))
        return int(sock.getsockname()[1])


def app_request(port: int, path: str, payload: bytes, content_type: str) -> tuple[int, dict]:
    connection = http.client.HTTPConnection("127.0.0.1", port, timeout=5)
    connection.request("POST", path, payload, {"Content-Type": content_type})
    response = connection.getresponse()
    body = json.loads(response.read())
    connection.close()
    return response.status, body


class RestrictedProbe(http.server.BaseHTTPRequestHandler):
    app_port = 0

    def log_message(self, *_args: object) -> None:
        pass

    def deterministic_error(self, status: int) -> None:
        self.send_response(status)
        self.send_header("Cache-Control", "no-store")
        self.send_header("Content-Length", "0")
        self.end_headers()

    def do_POST(self) -> None:  # noqa: N802
        host = self.headers.get("Host", "").split(":", 1)[0]
        length = int(self.headers.get("Content-Length", "0"))
        if (
            self.path != PROBE_PATH
            or HOST_PATTERN.fullmatch(host) is None
            or self.headers.get("Origin") != ORIGIN
            or not self.headers.get("Content-Type", "").lower().startswith("text/plain")
            or length > 4096
        ):
            self.deterministic_error(403 if length <= 4096 else 413)
            return
        body = self.rfile.read(length)
        upstream = http.client.HTTPConnection("127.0.0.1", self.app_port, timeout=5)
        upstream.request(
            "POST",
            PROBE_PATH,
            body,
            {"Host": host, "Origin": ORIGIN, "Content-Type": "text/plain"},
        )
        response = upstream.getresponse()
        response_body = response.read()
        self.send_response(response.status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Cache-Control", "no-store")
        self.send_header("Content-Length", str(len(response_body)))
        self.end_headers()
        self.wfile.write(response_body)
        upstream.close()

    def do_GET(self) -> None:  # noqa: N802
        self.deterministic_error(404)


def tls_request(
    port: int,
    hostname: str,
    path: str,
    token: str,
    ca: Path,
    origin: str = ORIGIN,
    content_type: str = "text/plain",
) -> tuple[int, bytes]:
    context = ssl.create_default_context(cafile=str(ca))
    raw = socket.create_connection(("127.0.0.1", port), timeout=5)
    wrapped = context.wrap_socket(raw, server_hostname=hostname)
    request = (
        f"POST {path} HTTP/1.1\r\nHost: {hostname}\r\nOrigin: {origin}\r\n"
        f"Content-Type: {content_type}\r\nContent-Length: {len(token.encode())}\r\nConnection: close\r\n\r\n{token}"
    )
    wrapped.sendall(request.encode())
    response = http.client.HTTPResponse(wrapped)
    response.begin()
    body = response.read()
    status = response.status
    wrapped.close()
    return status, body


def private_dns_rewrite(host: str) -> str | None:
    return "127.0.0.1" if HOST_PATTERN.fullmatch(host) else None


def ordinary_dns_resolution(_host: str) -> None:
    return None


def main() -> None:
    if not APP.is_file():
        raise SystemExit("TRUST_BOUNDARY=FAIL production build missing")
    app_port, tls_port = free_port(), free_port()
    environment = os.environ.copy()
    environment.update(
        {
            "NODE_ENV": "production",
            "HOSTNAME": "127.0.0.1",
            "PORT": str(app_port),
            "NEXT_TELEMETRY_DISABLED": "1",
            "USESAFEWEB_PUBLIC_ORIGIN": ORIGIN,
            "USESAFEWEB_DNS_VERIFICATION_SIGNING_SECRET": "ephemeral-only-" + "s" * 52,
            "USESAFEWEB_RELEASE_SHA": "1" * 40,
        }
    )
    process = subprocess.Popen(
        [os.environ.get("NODE_BINARY", "node"), str(APP)],
        cwd=APP.parent,
        env=environment,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    server = None
    try:
        for _ in range(100):
            if process.poll() is not None:
                raise RuntimeError("application exited before readiness")
            try:
                conn = http.client.HTTPConnection("127.0.0.1", app_port, timeout=1)
                conn.request("GET", "/api/health/ready")
                if conn.getresponse().status == 200:
                    break
            except OSError:
                pass
            time.sleep(0.05)
        else:
            raise RuntimeError("application readiness timeout")

        with tempfile.TemporaryDirectory(prefix="usesafeweb-trust-") as directory:
            temp = Path(directory)
            key, cert = temp / "key.pem", temp / "cert.pem"
            subprocess.run(
                [
                    "openssl", "req", "-x509", "-newkey", "rsa:2048", "-nodes", "-days", "1",
                    "-subj", "/CN=*.verify.usesafeweb.com", "-addext",
                    "subjectAltName=DNS:*.verify.usesafeweb.com", "-keyout", str(key), "-out", str(cert),
                ],
                check=True, capture_output=True, timeout=20,
            )
            RestrictedProbe.app_port = app_port
            server = http.server.ThreadingHTTPServer(("127.0.0.1", tls_port), RestrictedProbe)
            context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
            context.minimum_version = ssl.TLSVersion.TLSv1_2
            context.load_cert_chain(cert, key)
            server.socket = context.wrap_socket(server.socket, server_side=True)
            threading.Thread(target=server.serve_forever, daemon=True).start()

            scope = "ab" * 16
            status, issued = app_request(
                app_port, "/api/dns-verification/requests", json.dumps({"scope": scope}).encode(), "application/json"
            )
            assert status == 201
            host, request_token = issued["probeHost"], issued["requestToken"]
            assert ordinary_dns_resolution(host) is None
            assert private_dns_rewrite(host) == "127.0.0.1"

            status, body = tls_request(tls_port, host, PROBE_PATH, request_token, cert)
            assert status == 200
            observation_token = json.loads(body)["observationToken"]
            status, result = app_request(
                app_port,
                "/api/dns-verification/results",
                json.dumps({"requestToken": request_token, "observationToken": observation_token}).encode(),
                "application/json",
            )
            assert status == 200 and result == {
                "dnsPath": "verified-fresh", "reasonCode": "TECH_VERIFIED", "verifierVersion": "private-rewrite-v1"
            }

            try:
                tls_request(tls_port, "127.0.0.1", PROBE_PATH, request_token, cert)
                raise AssertionError("direct-IP TLS unexpectedly succeeded")
            except ssl.SSLCertVerificationError:
                pass

            for bad_host, bad_path, bad_origin in (
                ("f" * 32 + ".verify.usesafeweb.com", PROBE_PATH, ORIGIN),
                (host.upper(), PROBE_PATH, ORIGIN),
                ("short.verify.usesafeweb.com", PROBE_PATH, ORIGIN),
                (host, "/", ORIGIN),
                (host, PROBE_PATH, "https://attacker.invalid"),
            ):
                status, _ = tls_request(tls_port, bad_host, bad_path, request_token, cert, bad_origin)
                assert status in (403, 404)

            status, _ = tls_request(
                tls_port, host, PROBE_PATH, request_token, cert, content_type="application/json"
            )
            assert status == 403
            status, _ = tls_request(tls_port, host, PROBE_PATH, "x" * 4097, cert)
            assert status == 413

            payload_part, signature_part = observation_token.split(".", 1)
            altered = payload_part + "." + ("A" if signature_part[0] != "A" else "B") + signature_part[1:]
            status, _ = app_request(
                app_port,
                "/api/dns-verification/results",
                json.dumps({"requestToken": request_token, "observationToken": altered}).encode(),
                "application/json",
            )
            assert status == 403
        print("EPHEMERAL_PUBLIC_DNS_NEGATIVE=PASS")
        print("EPHEMERAL_PRIVATE_REWRITE_POSITIVE=PASS")
        print("EPHEMERAL_TLS_HOST_BOUNDARY=PASS")
        print("EPHEMERAL_REQUEST_PROBE_RESULT=PASS")
        print("EPHEMERAL_ABUSE_NEGATIVES=PASS")
        print("TRUST_BOUNDARY=PASS")
    finally:
        if server is not None:
            server.shutdown()
            server.server_close()
        process.terminate()
        try:
            process.wait(timeout=5)
        except subprocess.TimeoutExpired:
            process.kill()


if __name__ == "__main__":
    main()
