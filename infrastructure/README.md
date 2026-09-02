# Infrastructure source root

`/infrastructure` contains versioned infrastructure/runtime implementation source only. It does not own Azure control-plane state and does not create a second project checkpoint.

The current frozen direct-host DNS implementation lives under `/infrastructure/adguard-server`. Azure VM creation/configuration remains owner-managed under CON-0004; project automation starts only after supported VM handoff.
