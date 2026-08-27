# UseSafeWeb — Pilot Device Encrypted-DNS Configuration Methods

**Task:** TSK-0439  
**Acceptance:** ACC-0439  
**Decision date:** 2026-08-27  
**Scope:** Experiment-1 first-phone pilot only

## Supported platform baseline

UseSafeWeb supports exactly these two phone configuration families for Experiment 1:

1. **iPhone — iOS 14 or later** using a manually installed Apple DNS Settings configuration profile with **DNS-over-HTTPS (DoH)**.
2. **Android phone — Android 9 or later** when the device exposes the system **Private DNS provider hostname** setting, using **DNS-over-TLS (DoT)**.

This is a capability-based pilot boundary, not a claim that every OEM/version combination is identical. If the required native control is absent, altered by the manufacturer, or cannot be verified on the exact device, that device variant is unsupported for the pilot until separately tested.

The frozen PKG-09 package scope already permits **DoH/DoT where supported**. No VPN-based DNS app, AdGuard client app, or third-party DNS app is part of the baseline.

## Shared resolver identity

- Resolver FQDN: **`dns.usesafeweb.com`**
- Canonical iPhone DoH URL: **`https://dns.usesafeweb.com/dns-query`**
- Android native Private DNS / DoT hostname: **`dns.usesafeweb.com`**
- Android DoT service requirement: **TCP 853** on the same certificate-valid FQDN.
- `srv.usesafeweb.com` remains the server/administrative identity and is not a client configuration endpoint.

The Android DoT requirement does not replace the canonical DoH URL selected by TSK-0440. It is the native Android transport required by the already-frozen “DoH/DoT where supported” architecture. Downstream TLS/service/firewall work must therefore validate both transports before Android is admitted to a real pilot session.

---

## Method A — iPhone / iOS 14+

### Install

Use a reviewed `.mobileconfig` DNS Settings profile whose encrypted DNS payload specifies:

- protocol: `HTTPS`;
- server URL: `https://dns.usesafeweb.com/dns-query`;
- all-domain/system-wide application for the pilot; and
- no user-specific identifier, client token, wildcard hostname, or browsing-history payload.

The profile may be delivered from a UseSafeWeb HTTPS page and installed manually by the parent. Apple’s current support flow is:

1. download the configuration profile;
2. open **Settings**;
3. tap **Profile Downloaded**;
4. tap **Install** and follow the device prompts.

Current Apple documentation states that a website/email-downloaded profile must be installed from Settings and is automatically deleted if not installed within **8 minutes**. Apple also currently notes that, outside a familiar location, **Stolen Device Protection may need to be disabled before profile installation and re-enabled after installation**. This is a pilot friction/known-limit condition and must not be hidden from the parent.

### Verify

A successful iPhone verification requires all of the following:

1. **Configuration state:** the UseSafeWeb profile is visible under **Settings → General → VPN & Device Management**.
2. **Endpoint readiness:** downstream service evidence has already proven the certificate and DoH endpoint for `https://dns.usesafeweb.com/dns-query`.
3. **Effective resolver check:** while the profile is installed, the device must pass the approved UseSafeWeb synthetic DNS test pair/test set once that test set is deployed: an allowed control lookup resolves normally and a UseSafeWeb-only blocked control lookup returns the approved blocked result. The test uses synthetic names only; it must not inspect browsing history.
4. **Network-change check:** repeat the effective resolver check on at least one supported Wi-Fi path and cellular data because the profile is intended to be system-wide.
5. **Truth-state rule:** if the profile exists but the effective resolver check fails or another network/VPN/DNS mechanism makes routing ambiguous, classify the state as **Action needed** / unsupported rather than “Protected — verified.”

### Remove / restore

1. Open **Settings → General → VPN & Device Management**.
2. Select the UseSafeWeb profile.
3. Choose **Remove Profile** and complete the device prompts.
4. Re-run the synthetic control lookup that was previously blocked; it must return to the device’s normal resolver behavior.

Apple documents that removing a configuration profile removes the settings associated with that profile.

### Known limits

- Baseline support begins at **iOS 14**, where Apple exposes built-in encrypted DNS configuration for DoH/DoT.
- Manual profile installation requires user interaction and current Apple security prompts; it is not silent provisioning.
- A pending downloaded profile expires if not installed within the current Apple window.
- Current Stolen Device Protection behavior can add installation friction outside a familiar location.
- Conflicting VPN, DNS, network-extension, or network-routing behavior must be treated as a compatibility condition and directly re-verified; do not infer coverage from profile presence alone.
- The pilot does not support iPhone variants where the profile cannot be installed, retained, or verified safely.

---

## Method B — Android 9+ with native Private DNS

### Install

Android’s native Private DNS uses **DNS-over-TLS**, not the canonical DoH URL. The server must first expose a valid DoT service for `dns.usesafeweb.com` with a certificate valid for that hostname.

Google’s current generic Android flow is:

1. open **Settings**;
2. open **Network & internet**;
3. open **Private DNS**;
4. select **Private DNS provider hostname**;
5. enter **`dns.usesafeweb.com`**;
6. tap **Save**.

If the manufacturer moves the setting, search Settings for **Private DNS**. If the device has no provider-hostname control, it is unsupported for the baseline rather than being silently switched to an app/VPN method.

### Verify

A successful Android verification requires all of the following:

1. **Configuration state:** Private DNS remains set to **Private DNS provider hostname → `dns.usesafeweb.com`**.
2. **Transport readiness:** downstream target evidence has already proven DoT/TCP 853 and the certificate for `dns.usesafeweb.com`.
3. **Connectivity:** normal allowed DNS resolution works with Private DNS in strict provider-hostname mode.
4. **Effective resolver check:** the approved UseSafeWeb synthetic allowed/blocked test pair/test set produces the expected results without collecting ordinary browsing history.
5. **Network-change check:** repeat the control test after switching between a supported Wi-Fi path and cellular data.
6. **Truth-state rule:** a saved hostname with failed/ambiguous effective checks is **Action needed** / unsupported, not “Protected — verified.”

### Remove / restore

1. Open **Settings → Network & internet → Private DNS** (or search Settings for Private DNS).
2. Replace **Private DNS provider hostname** with **Automatic** to restore Android’s normal recommended Private DNS behavior.
3. Tap **Save**.
4. Re-run the synthetic control test to confirm the UseSafeWeb-specific block is no longer in effect.

Do not instruct parents to leave Private DNS permanently **Off** as the normal removal path; Google’s current guidance recommends keeping Private DNS enabled where possible.

### Known limits

- Native Private DNS/DoT baseline support begins at **Android 9**.
- Manufacturer menus vary. A device without a verifiable provider-hostname setting is unsupported for Experiment 1.
- DoT uses dedicated port **853**, which some networks may block even when HTTPS/443 works; such a network is a compatibility failure, not a reason to downgrade silently to plaintext DNS.
- Google explicitly notes that Private DNS secures DNS questions/answers only; it is not complete device/content protection.
- Apps or VPN/network components that bypass or replace the system resolver can invalidate the effective protection state; detect this through the control test and classify the variant as unsupported/action-needed if it cannot be made deterministic.

---

## Unsupported Experiment-1 variants

The following are explicitly outside the supported phone baseline unless a later task validates and approves them:

- iOS versions earlier than 14;
- Android versions earlier than 9;
- Android devices without a usable/verifiable **Private DNS provider hostname** setting;
- app/VPN-based DNS clients as a substitute for the native baseline;
- per-user ClientID hostnames/paths or wildcard-certificate client identity schemes;
- plaintext DNS as the child-phone pilot path;
- Windows, macOS, ChromeOS, routers, game consoles, smart TVs, and other non-phone device classes;
- iPad/tablet activation as an Experiment-1 cohort path, despite underlying Apple platform compatibility;
- any phone/network combination where VPN, alternate encrypted DNS, captive-portal behavior, carrier/OEM customization, or another routing layer makes the effective resolver path ambiguous after bounded troubleshooting.

Unsupported means **do not recruit/activate that configuration as a successful pilot path**; it does not mean the technology could never be supported later.

## Synthetic verification-test contract

TSK-0439 defines the client verification method but does not create the live test records/filter rules. Before real device activation, downstream DNS/filter work must version a privacy-safe synthetic test set with at least:

- one **allowed control name** that resolves normally through UseSafeWeb; and
- one **UseSafeWeb-only blocked control name** whose public DNS exists but whose resolution is blocked by the approved AdGuard test rule.

The pair must contain no participant identifier and must not require query-history logging. The client method verifies the configuration’s effect; server-side DoH/DoT/TLS tests independently verify encrypted transport. Both are required for a “Protected — verified” claim.

## Source and compatibility review

Official/current sources reviewed 2026-08-27:

### Apple

- Apple Support — Install a configuration profile on iPhone/iPad: `https://support.apple.com/102400`
- Apple Support — Install or remove configuration profiles on iPhone: `https://support.apple.com/guide/iphone/iph6c493b19/ios`
- Apple Developer — DNSSettings payload: `https://developer.apple.com/documentation/devicemanagement/dnssettings`
- Apple Developer — DNSSettings encrypted DNS dictionary: `https://developer.apple.com/documentation/devicemanagement/dnssettings/dnssettings-data.dictionary`
- Apple Developer — DNS settings / built-in encrypted DNS: `https://developer.apple.com/documentation/NetworkExtension/dns-settings`

Apple documentation supports HTTPS/TLS encrypted DNS, `ServerURL` for HTTPS, manual/local profile installation, and profile removal. Current Apple developer availability shows encrypted DNS server URL support from iOS 14+.

### Android / Google

- Google Android Help — Manage advanced network settings / Private DNS: `https://support.google.com/android/answer/9654714`
- Android Developers — Android 9 DNS privacy / system resolver DoT: `https://developer.android.com/about/versions/pie/android-9.0-changes-28`

Google documents the **Private DNS provider hostname** workflow; Android 9 documentation identifies system resolver DNS-over-TLS behavior.

### AdGuard Home

- AdGuard Home — DNS encryption: `https://adguard-dns.io/kb/adguard-home/encryption/`
- AdGuard Home — Configuration: `https://adguard-dns.io/kb/adguard-home/configuration/`

Current AdGuard Home guidance explicitly states that Android 9+ supports native DoT and iOS 14+ supports DoH/DoT through configuration profiles; AdGuard Home supports both protocols. Its configuration model exposes `port_dns_over_tls` for DoT and the TLS server name/certificate contract.

## Acceptance review

ACC-0439: “Each supported platform has an install, verification, removal, and known-limit method; unsupported variants are explicit.”

- iPhone install method: **PASS**.
- iPhone verification method: **PASS**.
- iPhone removal method: **PASS**.
- iPhone known limits: **PASS**.
- Android install method: **PASS**.
- Android verification method: **PASS**.
- Android removal method: **PASS**.
- Android known limits: **PASS**.
- Unsupported variants explicit: **PASS**.
- Accountless/minimum-data boundary preserved: **PASS**.
- DoH/DoT platform compatibility preserved: **PASS**.

**TSK-0439 stable outcome: PASS.**
