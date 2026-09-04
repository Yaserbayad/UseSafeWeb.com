# TSK-0243 public verifier deployment and rollback

Status: deploy-ready repository package only. This document does not assert
TSK-0243, LG-08, LG-09, release, or launch acceptance.

## Source and runtime

Deploy only the exact independently reviewed PR head. Set
`USESAFEWEB_RELEASE_SHA` to that exact 40-lowercase-hex commit; the deployment
script rejects a mismatch. Runtime is Node `22.23.2`, npm `10.9.8`, Next.js
`16.3.3`, and the existing direct-host systemd/Nginx architecture. No database,
container runtime, or additional platform is required.

Required external inputs are: the reviewed source checkout; a dedicated
`usesafeweb` service account; `/etc/usesafeweb/website.env` installed as `0600
root:root`; an authorized verifier IPv4 address; AdGuard loopback-admin
credentials installed as `0600 root:root`; and an externally issued certificate
and private key whose SAN includes exactly `*.verify.usesafeweb.com`.

The website environment file is created from `website.env.example`. The DNS
verification signing secret must be at least 32 UTF-8 bytes, random, server-only,
and must never use a `NEXT_PUBLIC_` name. The readiness endpoint exposes only
readiness, release SHA, and verifier contract version; it never exposes the key.

## Build and application start

On the application host, install the systemd unit and environment file, then run:

```sh
sudo infrastructure/web-server/deploy-release.sh <source-checkout> <reviewed-commit-sha>
curl --fail --silent http://127.0.0.1:3100/api/health/ready
```

The deployer runs `npm ci`, the full website validation/build, installs the
standalone output atomically, starts/restarts the hardened service, and restores
the previous release if readiness fails. `Restart=on-failure` provides bounded
recovery; systemd and Nginx errors remain visible without request bodies or
tokens.

## TLS and reverse proxy

Obtain the wildcard certificate later under separate authority using a DNS-01
client/provider integration whose credential stays external. Create
`/etc/usesafeweb/verifier-tls.env` from `tls.env.example`, with `0600 root:root`,
then run `install-verifier-config.sh`. Supply the public application certificate,
key, exact public hostname, and system CA trust bundle in the same external file.
The installer verifies current validity, trusted chain, exact SANs, key
permissions and key/certificate matches, disables only the recognized stock
Ubuntu default-site symlink, renders both public-origin and challenge virtual
hosts, runs
`nginx -t`, reloads, and restores the prior config on failure. Configure the
certificate client's deployment hook to call
`renew-verifier-certificate-hook.sh`; failed renewal validation leaves the last
working configuration in place.

The default HTTP listener drops requests and the default TLS listener rejects
the handshake. Only an exact lowercase 32-hex challenge hostname gets the
certificate and only `POST /api/dns-verification/probes` reaches the app.
Unrelated paths, methods, arbitrary Host values and direct-IP TLS do not sign.
Access logging is off, bodies are limited to 4 KiB, timeouts are short, and the
source-IP rate bucket returns 429 without persisting client history.

## Private DNS rewrite

On the DNS host, use `tsk-0243-verifier/manage-rewrite.py` as documented beside
the script. Its versioned AdGuard syntax is:

```text
/^[0-9a-f]{32}\.verify\.usesafeweb\.com$/$dnsrewrite=NOERROR;A;<verifier-ipv4>
```

Do not publish an equivalent authoritative record or wildcard. Ordinary public
DNS must remain negative. The manager validates the exact pinned AdGuard version
and inherited filtering, ECS-off, anonymization, querylog/filelog-off, and
statistics-off controls before changing the local user-rule list.

## Target acceptance (separate authority)

Read-only preflight performs health, public-negative DNS, UseSafeWeb-private DNS,
certificate hostname/chain, direct-IP TLS, and unrelated-path checks:

```sh
python3 infrastructure/web-server/verify-public-verifier.py \
  --application-origin https://<authorized-app-origin> \
  --usesafeweb-doh https://<authorized-doh-origin>/dns-query
```

Only after separate target authority, add
`--functional-authority TSK-0243-TARGET-PROOF`. Add `--wait-for-expiry` for the
bounded expiry test and `--rate-test-count 20` for the controlled rate test.
Tokens are redacted and each failed boundary has a stable nonzero exit code.
Inspect the target after the run to confirm no query/file log, statistics,
request body, proof token, challenge, domain history or client history was
stored. That target inspection is not simulated into repository PASS.

## Rotation, rollback, and removal

To rotate the signing key, install a new random key in the external environment
file and restart the application. There is deliberately no overlap: material
signed by the old key immediately fails verification. Roll back by restoring the
previous reviewed release and, only if explicitly authorized, its corresponding
external key.

Successful request/observation pairs are represented only by an in-memory
SHA-256 digest until their short expiry so a pair is accepted once. This bounded
replay cache is lost on restart and never writes proof material to disk; direct
host deployment intentionally runs a single application process so the guard is
not split across replicas.

To remove the verifier, first remove the private rewrite with
`manage-rewrite.py --remove`, then remove/disable the challenge Nginx config and
reload only after `nginx -t`. Retain the certificate externally or revoke it only
under separate certificate authority. Run read-only preflight with
`--expect-removed` to prove the private rewrite is gone. Application or verifier
unavailability, missing config/key/certificate, DNS disagreement, timeout,
staleness, replay across checks, wrong Host/Origin, or conflicting evidence all
fail closed and cannot produce `TECH_VERIFIED`.

Never log or retain signing keys, request/observation tokens, challenges, DNS
queries, browsing/domain history, identifiable client statistics, request
bodies, or credential URLs. Diagnostic output is category-only and no production
telemetry is enabled by this package.
