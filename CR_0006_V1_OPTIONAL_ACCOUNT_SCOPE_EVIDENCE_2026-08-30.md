# CR-0006 — Version-1 optional account scope amendment evidence

**Owner authority:** explicit Project Owner instruction 2026-08-30: the website must be able to have accounts from Version 1.

## Decision
DEC-0053 activates the existing account/authentication/minimum-persistence/lightweight-dashboard branch for Version 1 while retaining a complete accountless core path. Mandatory login for core value, browsing/activity history, child accounts and unrestricted DNS administration remain excluded. DEC-0052/CR-0005 human-validation sequencing is unchanged.

## Impact
- Activated 43 existing WBS rows previously deferred solely by EXC-0001.
- Reopened account-exclusion-dependent L4 baseline/prototype/accessibility/freeze/self-service evidence rather than fabricating equivalence.
- Revised LG-06/LG-07/LG-08 acceptance in product -> architecture/privacy/security -> implementation order.
- Activated existing auth/authz/IDOR/ClientID/deletion/recovery controls and updated the deterministic validator to enforce the new owner contract.
- Preserved prior evidence for unchanged accountless-core, DNS, brand, content and other facts.

## Pre-change identities
- planning base commit: `9606d83a82f121acffdf574e9973a7a937da0990`
- WBS blob: `f23b4f017d1baf73258fa30ecd71549bbfe1b815`
- relationship index blob: `9ed219b4ccb6b05e68c6a264fc2b21b1008b02a4`
- manifest blob: `1fc24e28e70c8005a75d37c1d21aecd4ea967ae5`
- runtime blob before later reconciliation: `ad3fd01395150b802fbb025a48f7692e82b80244`

Canonical reliance requires successful full validation, publication and read-back.
