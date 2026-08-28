# TSK-0443 — Certificate Renewal and Expiry Alert Evidence

**Task:** TSK-0443 — Automate certificate renewal and expiry alerting  
**Acceptance:** ACC-0443  
**Date:** 2026-08-28  
**Resolver:** `dns.usesafeweb.com`

## Acceptance contract

ACC-0443 requires all of the following:

1. a certificate renewal dry-run succeeds;
2. an expiry monitor alerts the owner with adequate lead time; and
3. recovery steps are documented.

TSK-0443 is L2 / A3 / `AUTO_ALLOWED` / HIGH / critical path with hard predecessors `TSK-0442; TSK-0011`, both satisfied before execution.

## Production renewal automation

Preflight run `33161696679` established the existing production renewal substrate:

- Certbot `2.9.0` installed;
- `certbot.timer` enabled and active;
- timer scheduled twice daily with randomized delay;
- Certbot service invokes quiet renewal;
- no existing deploy hook was present to reload Nginx after a successful renewal;
- no existing local mail/sendmail notification channel was available.

The governed production control run then installed the missing deploy hook and performed the renewal rehearsal.

Workflow: `.github/workflows/governance-task-row-inspect.yml`  
Commit: `a835c84c647846a411731b76b3365aa08c3d383d`  
Run: `33162046237`  
Production job: `98818564431` (`adguardvm`)  
Independent recovery-host matrix job: `98818564209` (`adguartestdvm_correct`) — correctly skipped after proving a non-production Azure VM ID.  
Result: **PASS**

Production identity was guarded by Azure VM ID `bc7f566f-7231-41fb-9fdd-49cf190fd5e1` before privileged mutation.

Installed deploy hook:

- path: `/etc/letsencrypt/renewal-hooks/deploy/10-usesafeweb-reload-nginx.sh`;
- owner/group/mode: root:root `0755`;
- SHA-256: `980197605ee3230c4c4463817ff53a734a5f9c9aa9b6c2b1672cd168a35de8e5`;
- behavior: run `nginx -t`, then reload Nginx only if configuration validation succeeds.

The hook was independently invoked and returned `DEPLOY_HOOK_RELOAD=PASS` with Nginx remaining active.

Certbot rehearsal command:

`certbot renew --dry-run --no-random-sleep-on-renew`

Certbot reported: **all simulated renewals succeeded** for `/etc/letsencrypt/live/dns.usesafeweb.com/fullchain.pem`.

Markers:

- `CERTBOT_RENEWAL_DRY_RUN=PASS`
- `POST_RENEWAL_SECURITY_BOUNDARY=PASS`
- `TSK_0443_PRODUCTION_RENEWAL_CONTROL=PASS`

Post-rehearsal verification also re-proved:

- certificate hostname `dns.usesafeweb.com` valid;
- more than 30 days remaining;
- private key remains root-owned mode `0600`;
- local TLS chain/hostname validation succeeds on TCP 443 and 853;
- AdGuard administration remains `127.0.0.1:3000` only;
- plain DNS remains loopback-only on TCP/UDP 53;
- Certbot timer remains enabled and active.

## Expiry monitor and owner alert

Persistent monitor: `.github/workflows/certificate-expiry-monitor.yml`  
Final monitor blob: `b565df52182e325d1d416a07be31f152078fd373`.

The final monitor:

- runs daily at `06:17 UTC`;
- uses only repository-scoped `contents: read` and `issues: write` permissions;
- checks both TLS endpoints, TCP 443 and TCP 853;
- validates the public hostname/chain through the independent recovery runner when scheduled there, or the same certificate locally when GitHub schedules the production runner;
- alerts at **30 days remaining or less**, or on TLS connection/chain/hostname validation failure;
- creates/reuses one GitHub issue assigned to Project Owner `Yaserbayad`;
- closes the alert after healthy validation returns above the threshold;
- contains no participant identifier, DNS query history, browsing history, private key, ACME credential, or other child/family data.

The initial version attempted GitHub-hosted execution in run `33161898754`, but GitHub terminated that job before any step executed. That run is not acceptance evidence. The monitor was moved to the already verified self-hosted execution pool without changing the acceptance requirement.

Successful monitor validation:

- commit: `36d92364c3a2d33948f8ca9571d35328ef0551bc`;
- run: `33161991492`;
- job: `98818390448`;
- runner: `adguartestdvm_correct` on independent Azure recovery VM;
- result: **PASS**;
- check role: `independent-external`;
- TCP 443: TLS 1.3, 89 days remaining, expiry `2026-11-26T07:57:17+00:00`;
- TCP 853: TLS 1.3, 89 days remaining, same expiry;
- `TLS_MINIMUM_DAYS=89`;
- `OWNER_ALERT_ROUTE=HEALTHY_NO_OPEN_ALERT`.

### Owner route proof

The installation validation created GitHub issue `#1`, title `[TEST] UseSafeWeb TLS expiry owner-alert route`, assigned it to `Yaserbayad`, commented completion, and closed it.

Direct GitHub issue read-back confirms:

- issue number: `1`;
- assignee: `Yaserbayad`;
- state: closed;
- state reason: completed;
- created and closed by the governed monitor route on 2026-08-28.

Marker: `OWNER_ALERT_TEST=PASS`.

After that proof, the temporary `push` test trigger and test-issue code were removed. The durable monitor is now schedule-only and will not create test issues on ordinary repository changes.

The 30-day threshold provides adequate owner lead time relative to the approximately 90-day certificate lifetime and the already-active automatic Certbot renewal path.

## Recovery documentation

Runbook: `infrastructure/adguard-server/TLS_CERTIFICATE_RENEWAL_RUNBOOK.md`  
Blob: `881d797ea6f69879d0c8696d61e596733c38c3c5`.

It documents:

- normal timer/renewal/deploy-hook flow;
- routine verification and dry-run commands;
- the 30-day owner-alert threshold and GitHub owner route;
- troubleshooting for timer/service/HTTP-01/DNS/Nginx/firewall failures;
- safe real-renewal handling without unnecessary forced renewal/rate-limit risk;
- Nginx reload and DoH/DoT verification;
- emergency certificate replacement boundaries;
- prohibition on failing open to plaintext DNS;
- privacy-safe evidence requirements and explicit prohibition on private keys, ACME credentials, raw DNS history, participant data, and browsing history.

## Acceptance synthesis

- Renewal dry-run succeeds: **PASS** — run `33162046237`, production job `98818564431`.
- Expiry monitor alerts owner with adequate lead time: **PASS** — final daily monitor blob `b565df52182e325d1d416a07be31f152078fd373`, successful independent external check run `33161991492`, and owner-assigned issue `#1` route proof.
- Recovery steps documented: **PASS** — runbook blob `881d797ea6f69879d0c8696d61e596733c38c3c5`.

## Stable outcome

**TSK-0443: PASS.**

ACC-0443 is fully satisfied. This operational certificate-renewal PASS does not authorize participant recruitment/activation or alter the separate TSK-0431 Azure-native recovery boundary.
