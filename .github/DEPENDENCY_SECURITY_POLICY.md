# Dependency and supply-chain security policy

**Owner:** Security  
**Applies to:** versioned project dependencies, downloaded release artifacts, future container images, lockfiles/digests, and CI-generated SBOM evidence.

## Required dependency state

- `website/package.json` declares direct npm dependencies and `website/package-lock.json` is the committed exact npm dependency-tree authority for this application boundary.
- Direct npm dependency declarations, exact lock-resolved versions, and current non-npm supply-chain inputs are recorded in `website/config/dependency-inventory.json`.
- The AdGuard Home release artifact used by current repository source is version-pinned and SHA-256 pinned in `infrastructure/adguard-server/install-adguard.sh`; a change to either value requires the same change review as the installer.
- There is no current container-image dependency. If a container image is introduced later, record it in the dependency inventory and pin it by immutable digest before it may satisfy this policy.
- Ubuntu 24.04 LTS host packages used by the current recovery source are provider-managed system-package inputs, not npm-lockfile artifacts. Their package names and provider/versioning model are inventoried. Exact installed target versions are target-environment evidence owned by the applicable deployment/recovery task; this policy does not invent or freeze target package versions outside that authority.

## Change and update rules

1. Dependency changes use a pull request and include the manifest, lockfile or immutable digest, dependency inventory, and any affected source/configuration in the same reviewable change.
2. CI must regenerate a CycloneDX SBOM from the committed npm lockfile and verify that every direct npm dependency is represented before the change is accepted.
3. Native package-manager audit results are reviewed with the change. A known **critical or high** vulnerability that is applicable to the runtime, build, test, or delivery path **blocks promotion** until it is remediated or an explicit current owner decision records the residual risk and its controls.
4. Moderate/low findings and routine updates remain tracked and are handled in bounded reviewable changes according to their actual reachability and risk; this document does not invent an unsupported calendar deadline.
5. `npm audit fix --force` must not be used as automatic remediation. Major/range-crossing or otherwise material dependency changes require explicit review plus the normal regression gates.
6. New download sources, package registries, install scripts, binary assets, or container images require source/provenance review and the strongest available immutable version/digest evidence before acceptance.
7. Dependency installation in the TSK-0491 acceptance workflow uses scripts disabled. A later dependency that requires an install lifecycle script must be reviewed explicitly rather than silently broadening execution.

## Secrets and evidence

Dependency and SBOM work must not commit or print production secrets, credentials, tokens, private keys, protected registry credentials, or private package bodies. Authentication material, if ever required for an approved private source, is externally injected and scoped/revocable. Durable evidence records only non-secret package/artifact identifiers, versions, digests, audit results, workflow/run identities, and deviations/dispositions.

## Exceptions

An exception must be explicit, narrow, owned, justified against the current risk, and time-bounded or tied to a deterministic resolution condition. An exception cannot silently bypass action-authority, security/privacy, deployment, launch, or human-approval gates.
