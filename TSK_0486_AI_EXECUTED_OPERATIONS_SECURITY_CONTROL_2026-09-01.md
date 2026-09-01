# TSK-0486 — AI-Executed Operations Security Control

**Version:** 1.0.0  
**Date:** 2026-09-01  
**Lifecycle:** L5 — Architecture, Technical Design & Delivery Readiness  
**Task:** TSK-0486 — Define least-privilege access, secret handling, approval gates, audit evidence, and emergency revocation for AI-executed operations  
**Acceptance:** ACC-0486 / VER-0486 / EVD-0486  
**Authority:** current WBS; DEC-0054/CR-0007; DEC-0055/CR-0008; REQ-0055; REQ-0056; REQ-0058; CON-0009; CON-0028; RSK-0007; INT-0015  
**Dependency:** TSK-0007 current PASS  
**Action authority:** A3 / AUTO_ALLOWED

## 1. Decision

UseSafeWeb operations use two independent controls:

1. **Project action authority** decides whether an action may be performed at all.
2. **Technical privilege** supplies only the minimum operating-system, provider, repository, application, or service permission needed to perform an already-authorized action.

Possession of a root-capable path, administrator role, deployment credential, GitHub token, provider token, SSH credential, application secret, or service credential **never creates project authority** and never bypasses a WBS action-authority or acceptance gate.

Normal runtime services operate least privilege. An owner-provided root-capable host path may be used only where bootstrap, deployment, recovery, or another technically necessary host action genuinely requires it, and only as a bounded and auditable execution path. No standing root requirement is introduced for normal application or DNS service operation.

This task defines the control contract. It does not claim that any external host, token, key, secret, runner, provider role, or production deployment is already configured or accepted.

## 2. Protected assets and trust boundaries

Protected assets include:

- owner-provided host/root-capable access paths;
- SSH/private-key material and equivalent host authentication mechanisms;
- GitHub and CI credentials/tokens;
- Azure/provider credentials where a later authorized task actually uses them;
- application/runtime environment secrets;
- AdGuard administrative credentials;
- authentication-provider and server-side service credentials;
- deployment/recovery identities;
- audit records proving privileged actions without exposing credentials;
- canonical GitHub planning/runtime authority.

Trust boundaries are:

| Boundary | Rule |
|---|---|
| Governance / action authority | Current WBS, Layer 5, current owner decisions and runtime evidence determine whether an action is authorized. |
| Secret injection | Secret values originate outside Git and durable evidence and enter only the exact authorized executor/runtime boundary. |
| Root-capable host path | Used only when technically necessary for an already-authorized bounded host action. |
| Normal runtime services | Dedicated/non-root identities and only permissions required for their service responsibility. |
| CI / automation | Job-scoped or otherwise narrowly scoped permissions; write/target privileges only when the current task requires them. |
| Evidence / audit | Records action identity, target, result and verification without storing credentials, private keys, raw DNS history or unnecessary personal data. |

## 3. Least-privilege and privileged-host rules

1. **Normal services are non-root by default.** Application, DNS support processes, monitoring and routine automation receive only the filesystem, network, process and service rights they require.
2. **Root-capable access is exceptional, not authoritative.** It is permitted only for technically necessary bootstrap/deployment/recovery/host-administration steps already authorized by the current task.
3. Before privileged use, the executor must verify:
   - exact task ID and current runtime eligibility;
   - current Action Authority;
   - exact target identity/environment;
   - required privilege level and why a lower level is insufficient;
   - rollback/recovery path for a material mutation;
   - that the credential/access path is intended for that executor/target.
4. Privilege must be bounded by **target, purpose and duration** wherever the platform supports those dimensions.
5. A broad credential must not be used merely because it is available when a narrower credential/path can satisfy the accepted task.
6. Routine service operation must not depend on an interactive root shell or an unrestricted administrator session.
7. Unknown target identity, stale authority, ambiguous credential provenance, unexplained privilege escalation, or a mismatch between task authority and requested effect is **fail-closed**: do not perform the privileged operation.
8. Privileged execution never changes HUMAN_ONLY, A2, spend, contract, legal, identity, strategic or other higher-authority boundaries.

## 4. Secret and token handling contract

All credentials, tokens, secrets and private keys used by ChatGPT-assisted operations, GitHub Actions or runtime automation must satisfy all of the following:

- **Externally injected:** no literal production secret, token, private key or credential is committed to Git, embedded in a durable artifact, copied into evidence, or placed in source/config intended for publication.
- **Minimum scope:** restrict repository, environment, host, service, operation and permissions to what the current purpose requires.
- **Revocable and rotatable:** the credential must have a deterministic provider/owner path to disable/revoke and replace it.
- **Time-bounded where supported:** prefer job/session/short-lived credentials over standing credentials when technically practical.
- **Server-side only when privileged:** browser/client/customer surfaces never receive AdGuard admin credentials, provider admin credentials, private keys or server-only application secrets.
- **No log disclosure:** do not echo secret-bearing commands or values; do not print environment-variable values containing credentials; preserve only sanitized status/identifier evidence.
- **No evidence disclosure:** evidence may record a secret reference/name/provider scope or redacted identifier when necessary, but never the secret value itself.
- **No untrusted-context exposure:** production/privileged secrets are not made available to untrusted fork/PR/content execution contexts or arbitrary user-controlled command paths.
- **No convenience reuse:** a production credential is not copied into local/preview/ephemeral testing merely to simplify setup; use synthetic/test-only scoped credentials where needed.
- **No raw DNS/personal-data substitution:** credentials and audit paths must not be used to collect browsing/query history or unnecessary personal data as operational evidence.

If a secret value is ever found in Git history, logs, evidence, chat output, an unintended runner, or another unauthorized location, treat the credential as potentially compromised even if access is believed limited.

## 5. Action-authority and approval gates

Credential availability and technical privilege are subordinate to current action authority.

| Current authority | Operational rule |
|---|---|
| AUTO_ALLOWED and acceptance/dependencies/gates satisfied | AI may execute the bounded action using the minimum required privilege, with verification/evidence/read-back required by Layer 5. |
| A2 contextual-confidence action | Explicit Project Owner approval is required at the point of use before the consequential action. Preparation/read-only analysis may continue where safe. |
| HUMAN_APPROVAL_REQUIRED | Consequential execution waits for explicit current approval; possessing credentials does not remove the gate. |
| HUMAN_ONLY | AI may prepare/analyze but must not perform or fabricate the human act. |
| Ambiguous/conflicting authority | Fail closed and resolve the smallest exact authority ambiguity before privileged execution. |

Owner-provided credentials or host access constitute **capability**, not approval. An instruction to make access available does not silently authorize every operation technically possible with that access.

## 6. Auditable privileged-operation envelope

Before a material privileged operation, record or deterministically derive the minimum audit envelope:

- task ID and acceptance boundary;
- current action authority and any required explicit approval reference;
- sanitized executor identity/type;
- sanitized exact target/environment identifier;
- source commit/artifact/config version where applicable;
- intended action and bounded effect;
- required privilege class and reason;
- idempotency/reversibility expectation;
- rollback/recovery path when applicable.

After execution, durable evidence should contain only what is necessary to prove the outcome:

- start/end or evidence timestamp;
- changed object/path/service identifiers without secret values;
- result and exact verification/read-back outcome;
- artifact/version/hash/commit where applicable;
- verifier/test/run identifier;
- rollback/revocation reference if invoked;
- deviations and their disposition.

Evidence must never contain secret values, private keys, authentication cookies, raw DNS browsing/query history, or unnecessary personal data.

Under DEC-0055, separate evidence documents/workflows are not mandatory when an existing durable commit/run/read-back record proves the boundary more efficiently.

## 7. Emergency stop, revoke and rotate procedure

Trigger this procedure when credential exposure/compromise is confirmed or reasonably suspected, privileged use is ambiguous or unauthorized, target identity cannot be trusted, or an operation exceeds its accepted authority.

1. **Stop** the affected privileged operation. Do not continue merely to complete the task.
2. **Fence** the affected target/action path so additional automated use cannot proceed.
3. **Revoke or disable** the affected credential/session/access path using the provider/owner-supported mechanism.
4. **Rotate/replace** the credential when exposure or compromise is possible; do not rely on deletion of the leaked copy as remediation.
5. **Preserve sanitized evidence**: credential reference/type, affected target, timestamps, observed unauthorized/exposed condition, revocation/rotation result and verifier. Never preserve the credential value.
6. **Verify revocation** using a non-disclosing provider/status check or a bounded negative access test where safe; do not print or replay the secret merely to prove revocation.
7. **Correct the cause** before issuing/re-enabling access: scope, injection path, logging, runner isolation, permissions, target selection, authority check or other identified control failure.
8. **Reissue narrowly** only if a still-eligible task genuinely requires replacement access.
9. **Recompute eligibility and authority** before resuming the interrupted governed operation.

Emergency handling does not expand action authority. If revocation/rotation itself requires an owner/provider human act that the AI cannot perform, the project becomes WAITING/BLOCKED for that exact act after all safe containment/preparation is completed.

## 8. CI and automation defaults

- GitHub workflow permissions default to read where write is unnecessary; a write-capable workflow declares only the permission needed for the accepted mutation.
- Production target access is absent from ordinary source-only CI.
- Target/self-hosted execution verifies target identity and current task authority before mutation.
- Secret-bearing values are passed through the platform secret mechanism or owner-provided environment and are not materialized into committed files.
- User-controlled strings are not interpolated into privileged shell/command execution without validation/allowlisting appropriate to the command boundary.
- Destructive or non-idempotent effects require explicit target validation, acceptance authority and a recovery/rollback strategy; ambiguous results are reconciled before retry.
- A workflow/job succeeding is not itself PASS; the task acceptance and durable target/source read-back remain controlling.

## 9. ACC-0486 traceability

| ACC-0486 clause | Control |
|---|---|
| AI action authority remains independent of server privilege | Sections 1, 3 and 5 separate governance authority from technical capability and explicitly prohibit privilege-derived authority. |
| Owner-provided host bootstrap/deployment may use an auditable root-capable path where technically required | Sections 1, 3 and 6 allow bounded root-capable use only when technically required and audit it. |
| Normal services run least privilege | Sections 1 and 3 require non-root/minimum-permission normal service operation. |
| Tokens/secrets are externally injected | Section 4 requires external injection and no committed literal secret. |
| Tokens/secrets are scoped/revocable | Sections 4 and 7 require minimum scope and deterministic revocation/rotation. |
| Tokens/secrets are absent from Git/evidence | Sections 4 and 6 prohibit secret values/private keys in Git and evidence. |
| HUMAN_ONLY and A2 remain gated | Section 5 makes both gates binding regardless of credential or server privilege. |

## 10. Verification checklist — VER-0486

A verifier must confirm against the exact versioned artifact and current canonical repository state that:

- [ ] TSK-0007 is current PASS and TSK-0486 is currently eligible/AUTO_ALLOWED.
- [ ] The WBS row, ACC-0486, VER-0486 and EVD-0486 match the current canonical WBS.
- [ ] The action-authority/technical-privilege separation is explicit.
- [ ] Root-capable bootstrap/deployment/recovery is permitted only when technically required and auditable.
- [ ] Normal runtime least privilege is mandatory.
- [ ] External injection, minimum scope, revocation/rotation and no-Git/no-evidence secret-value controls are explicit.
- [ ] HUMAN_ONLY, HUMAN_APPROVAL_REQUIRED and A2 gates cannot be bypassed by credential possession.
- [ ] Emergency stop/revoke/rotate/fence/read-back/recompute behavior is defined.
- [ ] Audit evidence is sufficient to reconstruct the privileged action without exposing secret or prohibited personal/DNS data.
- [ ] Current master-plan validation still passes and no canonical planning authority is changed by this task artifact.

## 11. EVD-0486 evidence contract

For acceptance, retain at minimum:

- artifact name/version/blob and source commit;
- current WBS and Layer-5 source/blob references;
- exact verification output/run identifier;
- verification date and verifier;
- dependency/current-authority result;
- deviations and disposition.

**Current deviations:** none defined by this control artifact. Actual future external host/credential configurations may reveal environment-specific deviations and must be handled by their owning task rather than silently inferred here.

## 12. Non-inference

Acceptance of TSK-0486 proves that the required AI-operations security control has been defined and verified against current authority. It does **not** prove that:

- any production credential/key/token has been created, injected, rotated or tested;
- either owner-provided Azure VM has been handed off or configured;
- a root-capable path exists or has been exercised;
- a GitHub/Azure/Firebase/AdGuard credential has any particular live scope;
- a production deployment, security test, release gate, launch, or real-user activation is PASS.

Those claims require direct evidence from the exact downstream environment/task that owns them.
