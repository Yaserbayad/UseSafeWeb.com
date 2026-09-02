# Website configuration boundary

This directory may contain only **non-secret** versioned application configuration whose owning task has defined a stable contract.

Environment-specific values are supplied by the approved deployment/runtime mechanism. Every **runtime secret**, credential, token and private key remains **outside Git** and must never be committed here, in `.env` files, or in application source.

A future task may add an explicit typed/configured environment contract after the application stack is implemented; TSK-0454 does not invent variable names or provider choices.
