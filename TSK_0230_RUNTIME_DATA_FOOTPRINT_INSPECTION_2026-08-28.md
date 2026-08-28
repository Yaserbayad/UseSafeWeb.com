# TSK-0230 runtime data-footprint inspection

**Date:** 2026-08-28  
**Target:** production runner host   
**Purpose:** privacy-safe read-only inspection for TSK-0230. No access/error log contents or DNS query records were read or exported.

## Target identity

- machine-id SHA-256: `e4988ed374ffd1836ca5c154f8ee8d727a2795bfcceb4ef9f682aecf95e177c2`
- expected accepted production fingerprint: MATCH

## Nginx effective logging configuration

### access_log directives

```
access_log off;
```

- Effective explicit non-off access-log target present: **NO**

### Access-log target metadata only

```
<no enabled access-log target metadata>
```

### error_log directives

```
error_log /var/log/nginx/error.log crit;
error_log /var/log/nginx/usesafeweb-doh-error.log crit;
```

### log-format declaration shape (sensitive variable names redacted)

```
<none explicit in effective config>
```

## AdGuard privacy flags

```
querylog_enabled=false
querylog_file_enabled=false
statistics_enabled=false
anonymize_client_ip=false
```

## Privacy boundary

This inspection intentionally did not read, sample, grep, print or commit any Nginx log record, DNS query, source IP, domain, URL payload, user agent, participant identifier, credential or secret. It records configuration directives and file metadata only.

## Disposition

TSK-0230 must treat any enabled Nginx access-log target as an actual potential source-IP/request-metadata processing location and must define purpose, lawful basis, retention/deletion, access and prohibited use before later participant/public use. If no such target is enabled, the NFR must preserve that privacy-minimal state unless a governed necessity case authorizes a change.
