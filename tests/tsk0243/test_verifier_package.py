import re
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


class VerifierPackageContract(unittest.TestCase):
    def read(self, relative: str) -> str:
        return (ROOT / relative).read_text(encoding="utf-8")

    def test_nginx_is_an_exact_non_default_signer(self) -> None:
        config = self.read("infrastructure/web-server/nginx/usesafeweb-verifier.conf.template")
        self.assertIn("listen 443 ssl default_server", config)
        self.assertIn("ssl_reject_handshake on", config)
        self.assertRegex(config, r"server_name ~\^\[0-9a-f\]\{32\}\\\.verify\\\.usesafeweb\\\.com\$;")
        self.assertIn("location = /api/dns-verification/probes", config)
        self.assertIn("limit_except POST", config)
        self.assertIn("client_max_body_size 4k", config)
        self.assertIn('if ($args != "") { return 404; }', config)
        self.assertIn("limit_req_status 429", config)
        self.assertIn("access_log off", config)
        self.assertIn("error_log /dev/null crit", config)
        self.assertIn("proxy_set_header Host $host", config)
        self.assertIn("location /", config)
        self.assertNotIn("server_name *.verify.usesafeweb.com", config)

    def test_adguard_rule_is_narrow_and_private_to_the_resolver(self) -> None:
        template = self.read("infrastructure/adguard-server/tsk-0243-verifier/rule.template")
        expected = "/^[0-9a-f]{32}\\.verify\\.usesafeweb\\.com$/$dnsrewrite=NOERROR;A;__VERIFIER_IPV4__"
        self.assertEqual(template.strip(), expected)
        host_pattern = re.compile(r"^[0-9a-f]{32}\.verify\.usesafeweb\.com$")
        self.assertIsNotNone(host_pattern.fullmatch("a" * 32 + ".verify.usesafeweb.com"))
        for host in (
            "A" * 32 + ".verify.usesafeweb.com",
            "a" * 31 + ".verify.usesafeweb.com",
            "a" * 33 + ".verify.usesafeweb.com",
            "a" * 32 + ".usesafeweb.com",
            "usesafeweb.com",
            "anything.verify.usesafeweb.com",
        ):
            self.assertIsNone(host_pattern.fullmatch(host), host)

    def test_renderers_fail_closed_and_never_contain_credentials(self) -> None:
        nginx = self.read("infrastructure/web-server/render-verifier-config.py")
        adguard = self.read("infrastructure/adguard-server/tsk-0243-verifier/manage-rewrite.py")
        for source in (nginx, adguard):
            self.assertNotRegex(source, r"(?i)(password|secret)\s*=\s*['\"][^'\"]+['\"]")
        self.assertIn("*.verify.usesafeweb.com", nginx)
        self.assertIn("v0.107.79", adguard)
        self.assertIn("--apply", adguard)
        self.assertIn("--remove", adguard)
        self.assertIn("querylog", adguard)
        self.assertIn("statistics", adguard)

    def test_ephemeral_harness_is_synthetic_and_has_both_dns_paths(self) -> None:
        harness = self.read("tests/tsk0243/ephemeral_trust_boundary.py")
        self.assertIn("ordinary_dns_resolution", harness)
        self.assertIn("private_dns_rewrite", harness)
        self.assertIn("TRUST_BOUNDARY=PASS", harness)
        self.assertIn("ephemeral-only-", harness)
        self.assertNotIn("dns.usesafeweb.com/dns-query", harness)

    @unittest.skipUnless(shutil.which("openssl"), "openssl is required for TLS rendering")
    def test_tls_renderer_accepts_only_matching_external_material(self) -> None:
        renderer = ROOT / "infrastructure/web-server/render-verifier-config.py"
        with tempfile.TemporaryDirectory() as directory:
            temp = Path(directory)
            key, cert, output = temp / "key.pem", temp / "cert.pem", temp / "nginx.conf"
            subprocess.run(
                [
                    "openssl", "req", "-x509", "-newkey", "rsa:2048", "-nodes", "-days", "1",
                    "-subj", "/CN=*.verify.usesafeweb.com", "-addext",
                    "subjectAltName=DNS:*.verify.usesafeweb.com", "-keyout", str(key), "-out", str(cert),
                ],
                check=True, capture_output=True,
            )
            key.chmod(0o600)
            result = subprocess.run(
                ["python", str(renderer), "--certificate", str(cert), "--private-key", str(key), "--output", str(output)],
                check=True, capture_output=True, text=True,
            )
            self.assertIn("TLS_WILDCARD_VALIDATION=PASS", result.stdout)
            rendered = output.read_text(encoding="utf-8")
            self.assertIn(str(cert.resolve()), rendered)
            self.assertIn(str(key.resolve()), rendered)

            wrong_cert = temp / "wrong.pem"
            subprocess.run(
                [
                    "openssl", "req", "-x509", "-newkey", "rsa:2048", "-nodes", "-days", "1",
                    "-subj", "/CN=example.invalid", "-addext", "subjectAltName=DNS:example.invalid",
                    "-keyout", str(temp / "wrong-key.pem"), "-out", str(wrong_cert),
                ],
                check=True, capture_output=True,
            )
            rejected = subprocess.run(
                ["python", str(renderer), "--certificate", str(wrong_cert), "--private-key", str(key), "--output", str(output)],
                capture_output=True, text=True,
            )
            self.assertNotEqual(rejected.returncode, 0)
            self.assertIn("exact wildcard SAN missing", rejected.stderr + rejected.stdout)


if __name__ == "__main__":
    unittest.main()
