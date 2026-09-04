#!/usr/bin/env bash
set -Eeuo pipefail

ROOT="$(git rev-parse --show-toplevel)"
TMP="$(mktemp -d)"
trap 'rm -rf -- "${TMP}"' EXIT
command -v nginx >/dev/null || { echo 'NGINX_SYNTAX=FAIL nginx unavailable' >&2; exit 1; }

openssl req -x509 -newkey rsa:2048 -nodes -days 1 \
  -subj '/CN=*.verify.usesafeweb.com' \
  -addext 'subjectAltName=DNS:*.verify.usesafeweb.com,DNS:usesafeweb.test' \
  -keyout "${TMP}/key.pem" -out "${TMP}/cert.pem" >/dev/null 2>&1
chmod 600 "${TMP}/key.pem"
python3 "${ROOT}/infrastructure/web-server/render-verifier-config.py" \
  --certificate "${TMP}/cert.pem" --private-key "${TMP}/key.pem" \
  --public-host usesafeweb.test --public-certificate "${TMP}/cert.pem" \
  --public-private-key "${TMP}/key.pem" --trust-bundle "${TMP}/cert.pem" \
  --output "${TMP}/verifier.conf" >/dev/null

sed \
  -e 's/listen 80 default_server;/listen 18080 default_server;/' \
  -e 's/listen \[::\]:80 default_server;/listen [::]:18080 default_server;/' \
  -e 's/listen 443 ssl default_server;/listen 18443 ssl default_server;/' \
  -e 's/listen \[::\]:443 ssl default_server;/listen [::]:18443 ssl default_server;/' \
  -e 's/listen 443 ssl;/listen 18443 ssl;/' \
  -e 's/listen \[::\]:443 ssl;/listen [::]:18443 ssl;/' \
  "${TMP}/verifier.conf" > "${TMP}/verifier-test.conf"
cat > "${TMP}/nginx.conf" <<EOF
pid ${TMP}/nginx.pid;
events {}
http {
  access_log off;
  include ${TMP}/verifier-test.conf;
}
EOF
nginx -t -p "${TMP}/" -c "${TMP}/nginx.conf"
printf 'NGINX_RENDERED_SYNTAX=PASS\n'
