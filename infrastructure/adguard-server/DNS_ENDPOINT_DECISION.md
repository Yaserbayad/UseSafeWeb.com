# UseSafeWeb — Pilot Encrypted DNS Endpoint Decision

**Task:** TSK-0440  
**Acceptance:** ACC-0440  
**Decision date:** 2026-08-27  
**Decision status:** APPROVED for the Experiment-1 technical baseline

## Selected endpoint

- Canonical client-facing hostname: **`dns.usesafeweb.com`**
- Canonical DNS-over-HTTPS URL: **`https://dns.usesafeweb.com/dns-query`**
- Protocol/port: **DoH over HTTPS/TCP 443**
- Canonical DoH path: **`/dns-query`**
- Server-management hostname remains separate: **`srv.usesafeweb.com`**

Hostnames are documented in lowercase for canonical consistency; DNS comparison remains case-insensitive.

## Scope boundary

This task selects identity/path only. It does not create the DNS record, issue/install the certificate, install AdGuard Home, open public service ports, or authorize participant traffic. Those actions remain owned by their downstream WBS tasks and acceptance evidence.

For this baseline:

- `dns.usesafeweb.com` is the client resolver identity.
- `srv.usesafeweb.com` remains the host/administrative identity and is not advertised as the family DNS endpoint.
- The AdGuard administration UI must not be exposed as part of the `dns.usesafeweb.com` public service surface; later deployment keeps administration private/restricted and verifies it separately.
- The public DNS record for `dns.usesafeweb.com` is **DNS-only/direct to the Azure resolver**, not proxied through the website CDN/edge. The website edge and family DNS path remain separate.
- No AAAA record is selected until a public IPv6 target is directly verified.
- No user-specific ClientID hostname or `/dns-query/{ClientID}` path is selected for the accountless Experiment-1 baseline.

## Compatibility evidence

Current AdGuard Home documentation supports DNS-over-HTTPS and documents the default DoH routes as `GET /dns-query` and `POST /dns-query`, with optional ClientID variants. The configuration documentation also requires the configured TLS `server_name` to match a DNS Name in the certificate and documents HTTPS port 443 for HTTPS/DoH.

Therefore the downstream endpoint contract is:

- certificate SAN/DNS Name includes exactly `dns.usesafeweb.com`;
- DoH request route remains the native/default `/dns-query`;
- if AdGuard Home terminates TLS directly, its configured TLS `server_name` must be `dns.usesafeweb.com` and the deployed configuration must prove that the administration surface is not publicly exposed;
- if direct AdGuard HTTPS would expose the web administration surface on the same public listener, a same-host reverse proxy may terminate TLS and expose only `/dns-query`, forwarding to AdGuard Home on loopback using the documented unencrypted-DoH/reverse-proxy mode;
- the TLS-termination choice is deliberately deferred to the downstream deployment/security task because this task selects the stable client identity/path, not the server implementation.

Official sources reviewed 2026-08-27:

- AdGuard DNS Knowledge Base — AdGuard Home configuration: `https://adguard-dns.io/kb/adguard-home/configuration/`
- AdGuard DNS Knowledge Base — AdGuard Home DNS encryption: `https://adguard-dns.io/kb/adguard-home/encryption/`

## Uniqueness review

- The frozen planning tree contains no pre-existing selection of `dns.usesafeweb.com`.
- Existing target identity `srv.usesafeweb.com` is intentionally separate.
- `dns` is a clear protocol/service label and does not couple the resolver identity to a specific VM name or future replacement host.
- Rebuilding/replacing the single AdGuard VM can therefore preserve the public resolver identity while the A/AAAA target changes under later DNS tasks.

**Network Engineering review: PASS.** The hostname is stable, service-oriented, certificate-compatible, independent of the VM hostname, and uses AdGuard Home's native DoH route.

## Security review

- Separate service and administration identities reduce accidental exposure of the management surface.
- The endpoint uses HTTPS/TLS and the certificate name must match the resolver hostname.
- AdGuard Home documentation states that its HTTPS port can serve both the web UI and DoH; therefore direct TLS termination is acceptable only if the later deployed configuration proves the administration surface remains non-public. Otherwise a same-host reverse proxy limited to `/dns-query` is the safer compatible pattern.
- The baseline does not use per-user ClientIDs, wildcard certificates, or user-specific resolver paths, consistent with accountless/minimum-data operation.
- DNS/CDN proxying is excluded for the resolver endpoint so the DNS path remains the directly verified Azure/AdGuard path.
- Public listener/firewall changes are deferred to deployment/security tasks and must be opened only when the corresponding service is installed and verified.

**Security review: PASS.** The hostname/path itself does not force public administration exposure or a particular TLS-termination architecture. The downstream implementation is explicitly required to keep the admin surface private and may introduce a same-host reverse proxy only when necessary to enforce that boundary.

## Downstream contract

TSK-0441 and later DNS/TLS/deployment work should implement and verify:

1. `dns.usesafeweb.com` resolves to the verified pilot target from multiple independent resolvers, with no stale/conflicting record.
2. The resolver record is not CDN/proxy-fronted.
3. The certificate chain is trusted and valid for `dns.usesafeweb.com`.
4. The TLS terminator presents the matching certificate and AdGuard Home serves DoH at `/dns-query`; direct AdGuard TLS is used only if the admin surface remains non-public, otherwise a same-host path-limited reverse proxy is used.
5. Public 443 is opened only with the service ready; administration remains restricted/non-public.
6. Removal/rebuild can change the backing target without changing the documented client endpoint.

## Acceptance evaluation

ACC-0440 requires the hostname/path to be unique, documented, compatible with certificates and AdGuard, and approved by network/security reviewers.

- Unique: **PASS**.
- Documented: **PASS**.
- Certificate compatible: **PASS** — explicit certificate/SNI contract above.
- AdGuard Home compatible: **PASS** — current documented native DoH route `/dns-query` and TLS server-name model.
- Network review: **PASS**.
- Security review: **PASS**.

**TSK-0440 stable outcome: PASS.**
