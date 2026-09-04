# Private verifier rewrite

This overlay targets the repository-pinned AdGuard Home `v0.107.79`. It adds one
user rule matching only a 32-lowercase-hex label below
`verify.usesafeweb.com`. The rule is local to UseSafeWeb DNS and is never an
authoritative public-DNS record.

Verify or apply after installing the externally held `0600 root:root` admin
credential file and substituting the verifier's authorized IPv4 address:

```sh
python3 manage-rewrite.py --verify --verifier-ipv4 192.0.2.10
python3 manage-rewrite.py --apply --verifier-ipv4 192.0.2.10
```

The tool requires the exact AdGuard version, loopback control API, query/file
logging disabled, ECS disabled, anonymization enabled, and filtering enabled.
Statistics may remain disabled or may use the currently authorized minimum
anonymized aggregate mode with exactly one-day retention; any enabled longer
retention or runtime/persisted disagreement fails closed. It preserves all
unrelated user rules. A failed update is rolled back to the exact prior rule
list without printing it.
An existing managed rule pointing to a different address must be removed
explicitly before applying the replacement, so an address conflict cannot be
silently overwritten.
Apply also installs `/etc/usesafeweb/verifier-rewrite.env` as the canonical
TSK-0422 pipeline overlay input; removal deletes it. Later baseline
reconciliation therefore preserves the exact managed rewrite rather than
treating it as drift.
Set `USESAFEWEB_TSK0243_REQUIRED=1` for the post-activation TSK-0422 invocation;
that makes a missing overlay input fail closed instead of reverting to the
pre-verifier empty-rule baseline.

Removal is explicit and leaves unrelated rules intact:

```sh
python3 manage-rewrite.py --remove --verifier-ipv4 192.0.2.10
```

The example address is documentation only and must be replaced. Missing or
conflicting configuration fails closed.
