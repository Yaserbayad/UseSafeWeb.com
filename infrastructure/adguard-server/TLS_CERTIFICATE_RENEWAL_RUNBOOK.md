# UseSafeWeb TLS Certificate Renewal and Recovery Runbook

**Scope:** `dns.usesafeweb.com` production encrypted-DNS certificate  
**Task:** TSK-0443  
**Owner:** Project Owner  
**Production target:** Azure VM `adguardvm`, West Europe  
**TLS terminator:** Nginx  
**Certificate manager:** Certbot

## Normal renewal path

1. Ubuntu `certbot.timer` invokes `certbot renew` twice daily with randomized delay.
2. Certbot renews the `dns.usesafeweb.com` lineage using its existing `/etc/letsencrypt/renewal/` configuration when the certificate is due.
3. A root-owned deploy hook at `/etc/letsencrypt/renewal-hooks/deploy/10-usesafeweb-reload-nginx.sh` validates Nginx configuration and reloads Nginx after a successful renewal so the running DoH/DoT service presents the new certificate.
4. The external GitHub workflow `.github/workflows/certificate-expiry-monitor.yml` checks the public TLS endpoints daily. It creates or maintains an owner-assigned GitHub issue if either encrypted-DNS TLS endpoint fails validation or the minimum observed remaining certificate lifetime is 30 days or less. It closes the open alert after a later healthy check shows more than 30 days remaining.

The monitor contains no DNS browsing history, participant identifier, client IP, credential, certificate private key, or other child/family data.

## Routine verification

On production, verify:

```bash
sudo certbot certificates
systemctl is-enabled certbot.timer
systemctl is-active certbot.timer
sudo nginx -t
```

Run a renewal rehearsal without replacing the production certificate:

```bash
sudo certbot renew --dry-run --no-random-sleep-on-renew
```

Then verify the deploy hook independently:

```bash
sudo /etc/letsencrypt/renewal-hooks/deploy/10-usesafeweb-reload-nginx.sh
```

After the hook, confirm Nginx remains active and local TLS validation succeeds for both the DoH listener on TCP 443 and the DoT listener on TCP 853 using SNI/hostname `dns.usesafeweb.com`.

## Alert threshold and owner route

- **Threshold:** 30 calendar days remaining or less, or any external TLS connection/hostname/chain validation failure.
- **Lead time rationale:** the certificate is approximately 90 days and Certbot begins normal renewal before expiry; a 30-day external threshold leaves a substantial manual recovery window if automatic renewal has failed.
- **Owner route:** an issue in `Yaserbayad/UseSafeWeb.com` assigned to GitHub user `Yaserbayad`.
- **Deduplication:** the monitor reuses one open alert issue rather than creating a new issue every day.
- **Recovery:** once both TLS endpoints validate and remaining lifetime is greater than 30 days, the monitor comments on and closes the open alert issue.

## When an expiry/renewal alert fires

1. Confirm whether the public certificate is actually near expiry or TLS validation is failing; do not infer failure from the alert text alone.
2. On `adguardvm`, verify exact Azure VM identity before privileged action.
3. Check `systemctl status certbot.timer certbot.service` and `journalctl -u certbot.service` for the renewal failure. Do not copy credentials/private keys into GitHub evidence.
4. Run `sudo certbot certificates` and `sudo certbot renew --dry-run --no-random-sleep-on-renew`.
5. Check DNS `dns.usesafeweb.com`, inbound TCP 80 needed by the existing HTTP-01 renewal path, and Nginx/host firewall state without opening plaintext DNS 53.
6. Correct the smallest verified cause. If a real renewal is due, allow the normal Certbot renewal path to run or invoke the existing lineage renewal only after confirming the cause and avoiding unnecessary forced renewals/rate-limit risk.
7. Run the deploy hook and verify Nginx serves the renewed certificate on 443 and 853 with the correct hostname/chain and the admin/plain-DNS boundaries unchanged.
8. Confirm the next external monitor run closes the GitHub alert, or perform the same public TLS checks immediately and record evidence.

## Emergency certificate replacement boundary

If the existing lineage cannot be safely renewed and the certificate is approaching expiry:

1. Keep plain DNS 53 non-public and preserve the private administration boundary.
2. Verify current public DNS and owner-controlled Azure ingress before requesting a replacement certificate.
3. Reuse the established Certbot/Let's Encrypt HTTP-01 architecture and the exact hostname `dns.usesafeweb.com`; do not introduce wildcard certificates, per-client hostnames, or certificate material in GitHub.
4. Validate the replacement certificate hostname/chain/private-key permissions locally before reloading Nginx.
5. Reload Nginx only after `nginx -t` succeeds.
6. Verify DoH `/dns-query` on 443 and DoT on 853, confirm `/` and `/control/status` remain non-public/404 through the TLS virtual host, and confirm TCP/UDP 53 remain loopback-only.
7. Re-run the real supported-device validation if certificate identity/path materially changed.

If replacement cannot be made trustworthy before expiry, do not fail open to plaintext DNS. Treat encrypted-DNS service as unavailable/uncertain and follow the service-removal/alternative guidance and later incident/runbook gates.

## Evidence to retain

Retain only privacy-safe operational evidence:

- certificate name, issuer/expiry/remaining days, and public hostname;
- Certbot timer enabled/active state;
- renewal dry-run result;
- deploy-hook file mode/hash and successful Nginx reload validation;
- external monitor workflow result and owner-alert routing test;
- exact production VM identity and date;
- deviations and their disposition.

Never retain private keys, ACME account credentials, raw DNS query history, participant data, or browsing/domain history in GitHub evidence.
