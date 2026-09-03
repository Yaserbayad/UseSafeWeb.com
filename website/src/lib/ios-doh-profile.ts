const SERVER_URL = 'https://dns.usesafeweb.com/dns-query';
const PAYLOAD_IDENTIFIER = 'com.usesafeweb.profile.doh';
const DNS_PAYLOAD_IDENTIFIER = 'com.usesafeweb.profile.doh.dns';
const ALLOWED_RELEASE_KEYS = new Set(['artifactStatus', 'version', 'payloadUuid', 'dnsPayloadUuid']);
const UUID_PATTERN = /^[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$/i;

type ApprovedRelease = {
  artifactStatus: 'verified';
  version: number;
  payloadUuid: string;
  dnsPayloadUuid: string;
};

function parseApprovedRelease(input: unknown): ApprovedRelease {
  if (typeof input !== 'object' || input === null || Array.isArray(input)) {
    throw new TypeError('verified release metadata must be an object');
  }

  const record = input as Record<string, unknown>;
  const keys = Object.keys(record);
  if (keys.length !== ALLOWED_RELEASE_KEYS.size || keys.some((key) => !ALLOWED_RELEASE_KEYS.has(key))) {
    throw new TypeError('release metadata contains undeclared fields');
  }
  if (record.artifactStatus !== 'verified') {
    throw new TypeError('release artifact is not verified');
  }
  if (typeof record.version !== 'number' || !Number.isSafeInteger(record.version) || record.version <= 0) {
    throw new TypeError('profile version must be a positive safe integer');
  }
  if (typeof record.payloadUuid !== 'string' || !UUID_PATTERN.test(record.payloadUuid)) {
    throw new TypeError('profile payload UUID is invalid');
  }
  if (typeof record.dnsPayloadUuid !== 'string' || !UUID_PATTERN.test(record.dnsPayloadUuid)) {
    throw new TypeError('DNS payload UUID is invalid');
  }

  const payloadUuid = record.payloadUuid.toUpperCase();
  const dnsPayloadUuid = record.dnsPayloadUuid.toUpperCase();
  if (payloadUuid === dnsPayloadUuid) {
    throw new TypeError('profile payload UUIDs must be distinct');
  }

  return {
    artifactStatus: 'verified',
    version: record.version,
    payloadUuid,
    dnsPayloadUuid,
  };
}

export function generateSafeWebIosDohProfile(input: unknown): string {
  const release = parseApprovedRelease(input);

  return `<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>PayloadContent</key>
    <array>
        <dict>
            <key>DNSSettings</key>
            <dict>
                <key>DNSProtocol</key>
                <string>HTTPS</string>
                <key>ServerURL</key>
                <string>${SERVER_URL}</string>
            </dict>
            <key>PayloadDescription</key>
            <string>SafeWeb DNS over HTTPS configuration for iPhone.</string>
            <key>PayloadDisplayName</key>
            <string>SafeWeb DNS</string>
            <key>PayloadIdentifier</key>
            <string>${DNS_PAYLOAD_IDENTIFIER}</string>
            <key>PayloadOrganization</key>
            <string>SafeWeb</string>
            <key>PayloadType</key>
            <string>com.apple.dnsSettings.managed</string>
            <key>PayloadUUID</key>
            <string>${release.dnsPayloadUuid}</string>
            <key>PayloadVersion</key>
            <integer>${release.version}</integer>
        </dict>
    </array>
    <key>PayloadDescription</key>
    <string>Configures SafeWeb DNS over HTTPS. Remove this profile to restore the device's normal DNS settings.</string>
    <key>PayloadDisplayName</key>
    <string>SafeWeb Encrypted DNS</string>
    <key>PayloadIdentifier</key>
    <string>${PAYLOAD_IDENTIFIER}</string>
    <key>PayloadOrganization</key>
    <string>SafeWeb</string>
    <key>PayloadType</key>
    <string>Configuration</string>
    <key>PayloadUUID</key>
    <string>${release.payloadUuid}</string>
    <key>PayloadVersion</key>
    <integer>${release.version}</integer>
</dict>
</plist>
`;
}
