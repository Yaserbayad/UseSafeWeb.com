# TSK-0355 — Minimum TypeScript + Next.js Application Architecture ADRs

**Version:** 1.0.0
**Date:** 2026-09-01
**Lifecycle:** L5 — Architecture, Technical Design & Delivery Readiness
**Task:** TSK-0355 — Validate and record the minimum owner-selected TypeScript + Next.js application architecture
**Acceptance:** ACC-0355 / VER-0355 / EVD-0355
**Authority:** current WBS; DEC-0053/CR-0006; DEC-0054/CR-0007; DEC-0055/CR-0008
**Dependency:** TSK-0235 current PASS; LG-06 current PASS
**Primary accepted architecture:** `TSK_0354_VERSION_1_APPLICATION_ARCHITECTURE_2026-09-01.md`, blob `4196c83e95a013c10b5c0a9a13005b97bbe08a59`
**Accepted context/integration diagrams:** `TSK_0235_SYSTEM_CONTEXT_CONTAINER_INTEGRATION_DIAGRAMS_2026-09-01.md`, blob `ecac82c1e020977a50af1d02345091415afba4ce`
**DNS/privacy desired-state source:** `infrastructure/adguard-server/tsk-0413-bundle-v1/README.md`, blob `5a162a87dd2761ff5a0da587fa660549309a1404`

## 1. Decision

Freeze the minimum Version-1 application architecture as **one TypeScript + Next.js App Router full-stack application under `/website`**, self-hosted on the owner-provided Ubuntu 24.04 LTS web/application VM, with a reverse proxy in front of a Node.js runtime and a separately deployed AdGuard/DNS VM.

The application serves both the public website and the product experience. The complete accountless safety journey remains usable without authentication. Optional Google/Firebase identity and a server-managed session add only the bounded parent account, minimum parent/device ownership persistence, and lightweight dashboard/device-management capability already authorized by DEC-0053/CR-0006.

The architecture is deliberately one deployable application, not a microservice estate. Browser code never receives AdGuard administrative credentials, Firebase Admin credentials, datastore credentials, TLS private keys, or recovery secrets. Ordinary DNS queries never traverse the Next.js application, account store, authentication provider, CMS, analytics, or dashboard.

No browsing, DNS-query, visited-domain, child-activity, or account-linked browsing history is created by this architecture.

## 2. Current framework evidence and version policy

Current official Next.js documentation was checked on 2026-09-01.

- The current App Router documentation reports **Next.js 16.3.4** as the latest documented version.
- The current installation guide states a minimum Node.js version of **20.9** and recommends the App Router in the default project setup.
- The current self-hosting guide recommends a reverse proxy such as nginx in front of a self-hosted Next.js server.
- Current documentation states that environment variables are server-only unless deliberately prefixed `NEXT_PUBLIC_`; browser-exposed values are built into the client bundle.
- Current Server/Client Component guidance states that layouts/pages are Server Components by default and recommends server execution for API keys, tokens, and other secrets.
- Current Route Handler guidance provides the application-native HTTP boundary under the `app` directory.
- Current output-file-tracing documentation supports `output: 'standalone'` to produce a minimal deployable Node.js server artifact.

Official sources:

- https://nextjs.org/docs/app/guides/self-hosting
- https://nextjs.org/docs/app/getting-started/installation
- https://nextjs.org/docs/app/guides/environment-variables
- https://nextjs.org/docs/app/getting-started/server-and-client-components
- https://nextjs.org/docs/app/getting-started/route-handlers
- https://nextjs.org/docs/app/api-reference/config/next-config-js/output

### Version decision

`/website` and `/website/package.json` do not yet exist in the canonical repository, so this architecture task does **not fabricate an installed dependency graph**.

The initial implementation baseline is:

1. Next.js **16.3.4 current-reference baseline** with TypeScript and App Router architecture.
2. Node.js runtime only; no Edge Runtime dependency is required by this architecture.
3. Node.js must be a maintained supported release satisfying Next.js's documented `>=20.9` minimum; the implementation/release manifest must pin the exact Node patch/major actually built and tested.
4. `package.json`/lockfile must pin the exact Next.js/React/runtime dependency set at first implementation. Any change away from the 16.3.4 current-reference baseline must be source-verified and treated as an explicit dependency update rather than silently floating on `latest`.
5. No package version is claimed installed until `/website/package.json` and the lockfile exist and are verified.

This fixes the framework and runtime boundary while keeping the eventual build evidence truthful.

## 3. ADR-0355-01 — One deployable Next.js application

**Decision:** Use one `/website` TypeScript + Next.js App Router application for:

- public discovery/trust/content surfaces;
- accountless setup and Protection Map journey;
- optional sign-in/session endpoints;
- lightweight dashboard/device-management UI;
- self-service troubleshooting, removal, reset, and recovery;
- server-side ownership and verification services;
- the typed server-only AdGuard adapter;
- the content/CMS adapter.

**Rationale:** This is the smallest production-capable shape already frozen by TSK-0354 and REQ-0036. It avoids unnecessary service boundaries, duplicated authentication, additional deployment/observability surfaces, and cross-service state.

**Rejected for Version 1:** separate frontend/backend services, microservices, Kubernetes, service mesh, dedicated broker/queue, native mobile app, public integration API, child-account service, school portal, data warehouse, or a second application solely for the dashboard.

## 4. ADR-0355-02 — App Router, server-first execution, bounded Route Handlers

**Decision:** Use the App Router. Server Components are the default for reads/rendering that can remain server-side. Client Components are limited to browser interaction/state/API needs. State-changing integration endpoints are bounded Route Handlers owned by the application.

Server-only modules own:

- optional session verification and account authorization;
- persistent account/device-store access;
- AdGuard control operations;
- recovery/secret-bearing integrations;
- protected content-administration operations;
- current technical Protection Map verification logic where secrets/config are required.

Browser code may contain only intentionally public configuration and product state. Secret values must never use `NEXT_PUBLIC_*`.

**Rule:** A browser-supplied account ID, device ID, AdGuard ClientID, Protection Map state, or parent confirmation is untrusted input, not authorization and not technical verification.

## 5. ADR-0355-03 — Direct-host deployment and rollback boundary

**Decision:** Self-host the application on the owner-provided Ubuntu 24.04 LTS web/application VM, separate from the DNS VM.

Production shape:

`Internet -> HTTPS reverse proxy -> single Next.js Node.js application process`

Minimum deployment rules:

1. Reverse proxy terminates/controls the public HTTP boundary and shields the Next.js process from direct Internet exposure.
2. The Next.js build uses `output: 'standalone'` unless later verified evidence demonstrates a concrete blocker. The deployable release includes the required standalone server, public assets/static output, release manifest, exact dependency lockfile/checksums, and configuration contract.
3. The application process runs as a dedicated least-privilege service identity under a direct-host process manager such as systemd; it does not run as root during normal operation.
4. Secrets are injected from the approved external secret mechanism at runtime and are absent from Git and build artifacts.
5. Releases are immutable/versioned. Rollback means restoring the previously verified application artifact plus its compatible configuration, not editing production files in place.
6. No Azure control-plane creation/configuration is implied. The owner-provided VM boundary remains in force.
7. INT-0011 remains a downstream release interface: this ADR defines the release shape but does not claim a deployable L6 candidate already exists.

## 6. ADR-0355-04 — Three separate state domains

### J0 — browser/session-only accountless state

Preferred for accountless progress and presentation state. It is not durable proof of protection or identity.

### J1 — optional anonymous transient server state

J1 exists only where implementation proves it necessary for safe setup completion, technical verification, artifact generation, or a deliberately supported short resume path.

If used, it inherits the accepted TSK-0229/TSK-0354 boundaries:

- opaque random token;
- minimum allowlisted fields only;
- hard non-sliding lifetime no longer than 24 hours;
- deletion on completion/reset/exit/integrity failure where applicable;
- no automatic linkage to an account;
- no identity, persistent ClientID, stable fingerprint, browsing/query/domain history, raw diagnostics, payment profile, or marketing profile;
- no durable backup by default;
- account sign-in does not extend its expiry.

### A — optional persistent account/device domain

A exists solely to support the approved optional Version-1 parent account/dashboard value. It may persist only the minimum:

- parent authentication/provider reference required to identify the account;
- opaque parent-owned device identity and ownership relation;
- bounded device label/settings/lifecycle state required by the dashboard;
- minimum timestamps/version/concurrency/deletion-reconciliation metadata needed for reliable lifecycle operations.

The concrete datastore product, exact schema, indexes, field-level retention, and backup implementation are owned by downstream data-model work and are **not invented here**. Only server-side code accesses A. ClientID is never authorization.

J0/J1 and A remain separate. No automatic journey-token/account stitching, IP fingerprinting, analytics stitching, or implicit account conversion is permitted.

## 7. ADR-0355-05 — Optional authentication and server-managed session pattern

**Decision:** Core value requires no login. When a parent elects optional persistent account/dashboard functionality, authentication follows the planned Google/Firebase route and terminates in a server-managed application session.

Current official Firebase documentation checked on 2026-09-01 supports exchanging a client-obtained ID token for a server-created session cookie, applying CSRF protection, using `HttpOnly`/`Secure` cookie policy, verifying the cookie server-side, and checking revocation when required.

Official source:

- https://firebase.google.com/docs/auth/admin/manage-cookies

Architecture flow:

1. Browser initiates optional Google/Firebase sign-in.
2. Browser receives the provider ID token.
3. Browser posts the token to a dedicated server Route Handler with the required anti-forgery protection.
4. Server verifies/exchanges the token through the approved Firebase Admin mechanism and establishes an `HttpOnly`, `Secure` server-managed session cookie with appropriate SameSite/path/domain policy.
5. Every protected account/dashboard operation verifies the server session and then performs server-side parent-to-device authorization.
6. Expired, invalid, revoked, disabled, or deleted-account sessions fail closed.
7. Logout clears local session state; security-sensitive revocation behavior follows the downstream TSK-0356 session contract.
8. Firebase/provider outage may disable sign-in/dashboard access but must not disable the healthy accountless core or DNS data plane.

TSK-0355 fixes this **session architecture pattern**, not Firebase pricing/quota/terms, exact cookie lifetime, exact SDK version, provider migration threshold, or final vendor acceptance. Those remain TSK-0356/related downstream acceptance.

## 8. ADR-0355-06 — Server-only AdGuard adapter and TSK-0413 privacy baseline

All application-to-AdGuard administrative interaction is server-side through a typed, allowlisted adapter. There is no generic browser-visible proxy to AdGuard `/control/*` endpoints.

The application architecture inherits the current TSK-0413 bundle exactly:

- AdGuard Home `v0.107.79`, configuration schema `34`;
- upstream exactly `https://dns10.quad9.net/dns-query`;
- ECS disabled;
- persistent query/file logging disabled;
- exceptional query diagnostics require separate authority, are capped at 24 hours, and are deleted after use;
- minimum anonymized aggregate statistics only, 24-hour retention;
- identifiable per-client statistics/history excluded;
- client-IP anonymization enabled;
- initial active filter is only the official AdGuard DNS filter represented by the TSK-0413 bundle;
- initial allowlist is empty and later exceptions are governed/versioned;
- AdGuard administration is authenticated and loopback-bound at `127.0.0.1:3000`;
- no AdGuard admin secret, TLS private key, raw DNS query history, or browsing/activity history is stored in Git or browser code.

The browser calls UseSafeWeb operations; the server adapter validates authorization/input and returns bounded product states. The exact cross-VM mechanism that securely reaches the DNS VM's loopback-only administration remains a downstream integration decision and must fail closed if it cannot preserve the TSK-0413 private-admin baseline.

INT-0012 is therefore fixed as:

`Browser -> UseSafeWeb server Route Handler -> authorization -> typed AdGuard adapter -> approved private control transport -> loopback-only AdGuard administration`

The ordinary DNS data plane remains separate:

`Managed device -> encrypted dns.usesafeweb.com DoH/DoT -> AdGuard -> Quad9 dns10 DoH`

Account/device ownership, ClientID presence, dashboard state, or parent confirmation can never substitute for current technical DNS verification.

## 9. ADR-0355-07 — Observability without surveillance

The application must expose the minimum operational signals required for safe operation while preserving the product privacy boundary.

Architecture-level signals:

- process health/readiness;
- external HTTP availability/latency/error rate;
- bounded Route Handler success/failure classes;
- authentication provider availability/error class without token content;
- ownership-store availability/error class;
- AdGuard control-adapter availability/result class without raw admin payloads;
- resource metrics such as CPU/memory/disk/availability through the infrastructure layer;
- certificate/domain expiry/availability signals where owned by operations.

Prohibited observability data:

- DNS query/domain/visited-site history;
- identifiable per-client DNS statistics;
- raw authentication tokens/session cookies;
- AdGuard admin credentials;
- persistent cross-session fingerprinting of accountless users;
- child activity feeds or engagement profiles.

Detailed log/metric field schemas, thresholds, retention, and dashboards remain downstream observability work. TSK-0355 fixes the boundary that those systems must obey.

## 10. ADR-0355-08 — Backup, deletion, and recovery boundaries

Backups and recovery are purpose-separated.

### Application/account domain

Only the approved persistent A-domain data and necessary application/content configuration may be included in application backups. J1 is excluded from durable backup by default. DNS query/domain history is never a backup dataset because it is not an application dataset.

Account/device deletion and recovery must distinguish:

- session revocation/logout;
- account record deletion;
- device ownership/control-record deletion/revocation;
- AdGuard client/resource reconciliation;
- physical DNS/profile removal from the managed device.

No one operation may falsely claim another completed. Restore procedures must not silently resurrect deleted account/device data; downstream data-model/backup work must define the smallest deletion-reconciliation mechanism required to prevent that failure.

### DNS domain

AdGuard recovery consumes the versioned TSK-0413 secret-safe desired-state bundle and externally injected secrets. It does not restore raw DNS query history, client browsing history, or historical third-party filters.

The application's availability/recovery design must tolerate temporary AdGuard-control unavailability without fabricating mutation success or changing the TSK-0413 DNS privacy baseline.

## 11. ADR-0355-09 — Content/CMS and accessible UI boundaries

REQ-0036 requires a mature accessible component library and lightweight browser-editable CMS. This architecture provides explicit adapters/boundaries for both without prematurely choosing products that have not yet been evaluated by their owning work.

### UI/component boundary

- shared accessible design-system components are consumed by both public and product surfaces;
- component-library selection must preserve WCAG 2.2 AA targets and the accepted L4 brand/design system;
- the library must not create a second application architecture or hidden telemetry requirement;
- exact library/package selection and version are bound when implementation dependencies exist and can be verified.

### CMS/content boundary

- browser-editable CMS is a content source only;
- content is versioned/reviewable and must preserve source-backed setup guidance;
- CMS never stores account/device ownership state, sessions, DNS data/history, AdGuard secrets, payment state, or product telemetry;
- CMS outage must not corrupt existing account/device state or DNS protection;
- exact CMS product remains downstream selection.

## 12. Failure behavior

| Condition | Required result | Forbidden result |
|---|---|---|
| Auth provider unavailable | Optional sign-in/dashboard degraded; accountless core remains usable | Force login for core value |
| Session invalid/revoked | Deny account data and require reauthentication for account features | Serve cached prior-parent data |
| Ownership store unavailable | Dashboard/device management fails safely; accountless core remains available | Infer ownership from ClientID/browser state |
| J1 unavailable | Use J0/no-resume path where safe or fail only dependent feature | Require account creation as workaround |
| AdGuard control unavailable | Report unavailable/uncertain; reconcile idempotently | Blindly replay ambiguous mutation or claim success |
| DNS verification unavailable | Protection state becomes uncertain/action-needed/error | Treat account/device presence as Verified |
| CMS unavailable | Serve last verified content where safe or bounded content-unavailable state | Expand CMS into product-state authority |
| Backup restore | Restore only permitted persistent state and reconcile deletions | Restore expired J1 or browsing/query history |

## 13. Explicit non-goals

Version 1 does not include:

- mandatory login for core safety value;
- child accounts/profiles;
- browsing/query/activity history;
- top-domain/visited-domain dashboards;
- unrestricted customer DNS administration or raw policy editing;
- public AdGuard administration or arbitrary `/control/*` passthrough;
- browser delivery of AdGuard/Firebase Admin/datastore/TLS/recovery secrets;
- microservices, Kubernetes, service mesh, dedicated queue/broker, multi-region active-active architecture;
- native mobile application or school portal;
- a second dashboard application;
- payment as a prerequisite to core value;
- architecture-level selection of datastore/CMS/component-library products without their owning evidence;
- inference of technical protection from ownership/account state.

## 14. RSK-0045 disposition

`RSK-0045` remains **OPEN as an active scope/privacy control**, not silently closed by this task.

TSK-0355 contains the required preventive architecture controls:

- accountless core is a first-class route and failure fallback;
- account scope is limited to minimum parent/device ownership/settings/lifecycle metadata;
- no browsing/activity history;
- no child account;
- no raw DNS policy editor;
- no use of account state as technical verification;
- scope expansion requires fresh owner/privacy/security review under DEC-0053.

If implementation violates any of these controls, affected architecture/product/privacy acceptance must reopen; the correct response is removal/reduction of the offending scope and excess data, not acceptance of drift.

## 15. Requirement/interface trace

| Authority item | TSK-0355 architecture response | Result |
|---|---|---|
| ACC-0355 framework boundary | One TypeScript + Next.js App Router application; current reference 16.3.4; truthful implementation pin policy | SATISFIED |
| ACC-0355 deployment/runtime | Direct-host Ubuntu web VM, reverse proxy, Node.js runtime, standalone release boundary | SATISFIED |
| ACC-0355 anonymous ephemeral state | J0 preferred; J1 optional, minimum, anonymous, <=24h, non-linking, non-durable by default | SATISFIED |
| ACC-0355 minimum persistent store | Separate server-only A domain limited to approved parent/device purpose; product/schema downstream | SATISFIED |
| ACC-0355 auth/session | Optional Google/Firebase identity -> server-validated secure session-cookie pattern; no mandatory login | SATISFIED |
| ACC-0355 server-only AdGuard adapter | Typed allowlist, authorization before control, no browser admin credentials, private transport only | SATISFIED |
| ACC-0355 observability | Health/error/resource signals only; no DNS/domain history or identifiable client statistics | SATISFIED |
| ACC-0355 backup/deletion/recovery | Purpose-separated backup; deletion operations remain distinct; no J1/history resurrection | SATISFIED |
| ACC-0355 explicit non-goals | Section 13 | SATISFIED |
| ACC-0355 persistent-data limit | A domain only for approved account/device purpose; no browsing/activity history | SATISFIED |
| REQ-0036 | One `/website` full-stack app plus UI/CMS architecture boundaries | SATISFIED AT ARCHITECTURE BOUNDARY |
| REQ-0037 | Minimum short-lived anonymous state; minimum optional account/device persistence; history prohibited | SATISFIED |
| REQ-0039 | Architecture consumes validated TSK-0354/TSK-0235 scope rather than inventing UX during coding | SATISFIED |
| CON-0010 | Optional account/dashboard retained; complete core remains accountless-capable | SATISFIED |
| CON-0011 | No payment/card/trial before core value | SATISFIED |
| INT-0011 | Direct-host release/rollback shape defined; actual L6 release candidate remains downstream | SATISFIED AT ARCHITECTURE BOUNDARY |
| INT-0012 | Server-only DNS setup/verification integration; no admin credentials; evidence-backed state only | SATISFIED |
| TSK-0413 | Exact privacy-first desired state carried into AdGuard integration/recovery boundaries | SATISFIED |

## 16. Deviations, deferred selections, and non-inference

The following are intentionally **not** selected by TSK-0355 because their owning tasks/evidence have not completed:

- exact persistent datastore product/schema/indexes/field retention;
- exact Firebase SDK versions, pricing/quota/terms, cookie lifetime, and migration trigger;
- exact CMS product;
- exact accessible component-library package/version;
- exact cross-VM private transport reaching AdGuard's loopback-only administration;
- final production secret-provider implementation;
- a built `/website` package graph or release artifact.

These are not ACC-0355 gaps because the required architecture boundaries and failure/privacy constraints are fixed here. A downstream task must fail closed rather than fill any of these selections with an unsupported assumption.

**No implementation, build, deployment, LG-07/LG-08, production activation, launch, payment, or real-user validation PASS is inferred by these ADRs.**

## 17. Review record

- Review date: 2026-09-01.
- Responsible architecture review: ChatGPT Project Governor under A3 / AUTO_ALLOWED, with GitHub canonical-source read-back and a separate deterministic acceptance check required before runtime PASS.
- Current source review: TSK-0235 current PASS, TSK-0354 accepted architecture, current WBS/register controls, TSK-0413 v1.0.0 privacy-first bundle, and current official Next.js/Firebase documentation cited above.
- Repository observation before decision: `/website` and `/website/package.json` do not exist at this architecture decision point; therefore no installed dependency version is fabricated.
- Deviations: downstream product/vendor selections listed in Section 16 remain unresolved by design and do not weaken the fixed architecture boundary.
