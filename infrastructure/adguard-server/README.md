# `/infrastructure/adguard-server` — AdGuard direct-host deployment/recovery source

**Owner:** Cloud / Platform Engineering with Network / DNS acceptance  
**Target:** owner-provided **Ubuntu 24.04 LTS** AdGuard/DNS VM after handoff.

This directory is the canonical source location for the frozen self-hosted **AdGuard** direct-host deployment/recovery implementation and its versioned non-secret desired-state inputs.

## Current boundary

Existing scripts and contracts remain individually governed by their owning task evidence. TSK-0445 defines the production orchestration design. **TSK-0455** owns implementation and target-environment proof of the future entry point:

`deploy_or_recover.sh`

TSK-0454 does not claim that script exists or passes recovery acceptance yet.

## Secrets and runtime configuration

Keep **secrets outside Git**. Credentials, password material, tokens, TLS private keys, protected backups and environment-specific runtime configuration are provided through approved protected host/runtime mechanisms. Version control may contain only the non-secret scripts, templates, desired-state fragments, compatibility metadata and verification code explicitly allowed by the current contracts.

## Azure boundary

The **Azure control-plane** remains owner-managed. Repository automation must not create/resize/delete VMs, NSGs or other Azure resources unless a later explicit owner decision changes CON-0004. Direct-host automation starts after fresh-host handoff and must preserve the accepted recovery/privacy/security contracts.
