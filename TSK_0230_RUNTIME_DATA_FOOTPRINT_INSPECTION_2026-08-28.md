# TSK-0230 runtime data-footprint inspection

**Date:** 2026-08-28
**Target:** production runner host adguardvm
**Purpose:** privacy-safe read-only inspection for TSK-0230. No access/error log contents or DNS query records were read or exported.

## Verifier correction history

- Run 33193360160 failed before evidence because the verifier tested root-protected AdGuard config readability as the unprivileged runner user. No target mutation occurred.
- Run 33193437786 corrected that permission probe but read anonymize_client_ip from the YAML root instead of the accepted AdGuard schema path dns.anonymize_client_ip. That false negative is not accepted as runtime evidence.
- Run 33193504036 used the correct schema and all privacy assertions passed; only report rendering failed because Markdown backticks were interpreted by the shell and diff-check rejected trailing whitespace. No target mutation occurred.
- Run 33193560476 preserved those assertions and produced the first accepted corrected runtime report.
- This revision adds only error-log metadata and logrotate configuration; it still never reads log contents.

## Target identity

- machine-id SHA-256: e4988ed374ffd1836ca5c154f8ee8d727a2795bfcceb4ef9f682aecf95e177c2
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

### Error-log target metadata only

```
/var/log/nginx/error.log: exists=yes size_bytes=0 mode=640 owner=www-data:adm
/var/log/nginx/usesafeweb-doh-error.log: exists=yes size_bytes=0 mode=644 owner=root:root
```

### Nginx logrotate configuration

```
/var/log/nginx/*.log {
	daily
	missingok
	rotate 14
	compress
	delaycompress
	notifempty
	create 0640 www-data adm
	sharedscripts
	prerotate
		if [ -d /etc/logrotate.d/httpd-prerotate ]; then \
			run-parts /etc/logrotate.d/httpd-prerotate; \
		fi \
	endscript
	postrotate
		invoke-rc.d nginx rotate >/dev/null 2>&1
	endscript
}
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
anonymize_client_ip=true
anonymize_client_ip_schema=dns.anonymize_client_ip
```

## Privacy boundary

This inspection intentionally did not read, sample, grep, print or commit any Nginx log record, DNS query, source IP, domain, URL payload, user agent, participant identifier, credential or secret. It records configuration directives, retention configuration and file metadata only.

## Accepted runtime facts

- Nginx access logging: explicitly off.
- Nginx error logging: critical severity only to the configured error-log files; exact file metadata and logrotate configuration are recorded above without reading records.
- AdGuard persistent query logging: off.
- AdGuard file query logging: off.
- AdGuard statistics: off.
- AdGuard client-IP anonymisation at dns.anonymize_client_ip: enabled.

## Disposition

TSK-0230 must preserve these privacy-minimal facts. Any future access-log enablement or material AdGuard logging/statistics/anonymisation change requires a governed necessity case, purpose/lawful-basis/retention/access/deletion definition, actual-runtime verification, and impact review before participant/public use. Critical error logs must remain restricted to operational/security diagnosis and follow the evidenced bounded rotation policy rather than become product analytics or browsing-history data.
