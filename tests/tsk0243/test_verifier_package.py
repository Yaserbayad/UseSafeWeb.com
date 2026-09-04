import importlib.util
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
        self.assertRegex(config, r'server_name "~\^\[0-9a-f\]\{32\}\\\.verify\\\.usesafeweb\\\.com\$";')
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
        self.assertIn("server_name __PUBLIC_APPLICATION_HOST__;", config)
        self.assertIn('ssl_certificate "__PUBLIC_TLS_CERTIFICATE__";', config)
        self.assertIn("location = /api/health/ready", config)
        workflow = self.read(".github/workflows/accept-tsk0489-governed-ci-promotion-20260904.yml")
        gate = self.read(".github/scripts/tsk0489-governed-ci.sh")
        self.assertIn("nginx-core", workflow)
        self.assertIn("tests/tsk0243/nginx_syntax_test.sh", gate)
        installer = self.read("infrastructure/web-server/install-verifier-config.sh")
        self.assertIn("/etc/nginx/sites-enabled/default", installer)
        self.assertIn("unexpected default site owner", installer)
        self.assertIn("DEFAULT_SITE_DISABLED", installer)

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
        pipeline = self.read("infrastructure/adguard-server/tsk-0422-adguard-config-pipeline.sh")
        self.assertIn("/etc/usesafeweb/verifier-rewrite.env", pipeline)
        self.assertIn("TSK0243_VERIFIER_RULE", pipeline)
        self.assertIn("expected_user_rules", pipeline)

    def test_adguard_privacy_accepts_both_current_authorized_statistics_modes(self) -> None:
        path = ROOT / "infrastructure/adguard-server/tsk-0243-verifier/manage-rewrite.py"
        spec = importlib.util.spec_from_file_location("tsk0243_manage_rewrite", path)
        self.assertIsNotNone(spec)
        self.assertIsNotNone(spec.loader)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

        class FakeApi:
            def __init__(self, statistics_enabled: bool, statistics_interval: int = 1) -> None:
                self.statistics_enabled = statistics_enabled
                self.statistics_interval = statistics_interval

            def request(self, endpoint: str, payload=None):
                if endpoint == "/querylog/config":
                    return {"enabled": False}
                if endpoint == "/stats/config":
                    return {"enabled": self.statistics_enabled, "interval": self.statistics_interval}
                raise AssertionError(endpoint)

        with tempfile.TemporaryDirectory() as directory:
            config = Path(directory) / "AdGuardHome.yaml"

            def write_statistics(enabled: bool, interval: str = "1d") -> None:
                config.write_text(
                    "querylog:\n"
                    "  enabled: false\n"
                    "  file_enabled: false\n"
                    "statistics:\n"
                    f"  enabled: {'true' if enabled else 'false'}\n"
                    f"  interval: {interval}\n"
                    "dns:\n"
                    "  anonymize_client_ip: true\n"
                    "  edns_client_subnet:\n"
                    "    enabled: false\n"
                    "filtering:\n"
                    "  protection_enabled: true\n"
                    "  filtering_enabled: true\n",
                    encoding="utf-8",
                )

            write_statistics(False)
            module.validate_privacy(FakeApi(False), config)

            write_statistics(True)
            module.validate_privacy(FakeApi(True), config)

            write_statistics(True, "7d")
            with self.assertRaises(SystemExit):
                module.validate_privacy(FakeApi(True), config)

            write_statistics(True)
            with self.assertRaises(SystemExit):
                module.validate_privacy(FakeApi(False), config)
            with self.assertRaises(SystemExit):
                module.validate_privacy(FakeApi(True, 7), config)

    def test_deployment_rollback_restores_release_identity_and_cleans_first_failure(self) -> None:
        deploy = self.read("infrastructure/web-server/deploy-release.sh")
        self.assertIn('previous_release_sha=', deploy)
        self.assertIn('set_release_binding "${previous_release_sha}"', deploy)
        self.assertIn('CURRENT_UPDATED=0', deploy)
        self.assertIn('RELEASE_INSTALLED=0', deploy)
        self.assertIn('systemctl stop "${SERVICE}"', deploy)
        self.assertIn('rm -f "${current}"', deploy)
        self.assertIn('rm -rf -- "${release}"', deploy)
        self.assertRegex(
            deploy,
            r'set_release_binding "\$\{previous_release_sha\}"[\s\S]+systemctl restart "\$\{SERVICE\}"',
        )

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
        self.assertIn("st_uid != 0", adguard)
        self.assertIn('!= "adguardvm"', adguard)

    def test_external_preflight_checks_all_resolution_and_authority_boundaries(self) -> None:
        preflight = self.read("infrastructure/web-server/verify-public-verifier.py")
        self.assertIn("dns_query(host, args.public_dns, 1)", preflight)
        self.assertIn("dns_query(host, args.public_dns, 28)", preflight)
        self.assertIn("UNEXPECTED_DNS_ANSWER", preflight)
        self.assertIn("except ssl.SSLError", preflight)
        self.assertIn('AUTHORITY = "TSK-0243-TARGET-PROOF"', preflight)
        self.assertIn('print("REPLAY=PASS")', preflight)

    def test_ephemeral_harness_is_synthetic_and_has_both_dns_paths(self) -> None:
        harness = self.read("tests/tsk0243/ephemeral_trust_boundary.py")
        self.assertIn("ordinary_dns_resolution", harness)
        self.assertIn("private_dns_rewrite", harness)
        self.assertIn("TRUST_BOUNDARY=PASS", harness)
        self.assertIn("EPHEMERAL_SHIPPED_CONFIG_RENDER=PASS", harness)
        self.assertIn("rule.template", harness)
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
                    "subjectAltName=DNS:*.verify.usesafeweb.com,DNS:usesafeweb.test", "-keyout", str(key), "-out", str(cert),
                ],
                check=True, capture_output=True,
            )
            key.chmod(0o600)
            result = subprocess.run(
                [
                    "python", str(renderer), "--certificate", str(cert), "--private-key", str(key),
                    "--public-host", "usesafeweb.test", "--public-certificate", str(cert),
                    "--public-private-key", str(key), "--trust-bundle", str(cert), "--output", str(output),
                ],
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
                [
                    "python", str(renderer), "--certificate", str(wrong_cert), "--private-key", str(key),
                    "--public-host", "usesafeweb.test", "--public-certificate", str(cert),
                    "--public-private-key", str(key), "--trust-bundle", str(wrong_cert), "--output", str(output),
                ],
                capture_output=True, text=True,
            )
            self.assertNotEqual(rejected.returncode, 0)
            self.assertIn("required SAN missing", rejected.stderr + rejected.stdout)


if __name__ == "__main__":
    unittest.main()
