# TSK-0307 — Current Source-Backed Instruction / Content Catalogue Revalidation

**Task:** TSK-0307 — Create the source-backed instruction/content catalogue with applicability and review triggers  
**Acceptance / Verification / Evidence:** ACC-0307 / VER-0307 / EVD-0307  
**Lifecycle / Priority / Authority:** L4 / HIGH / A3 / AUTO_ALLOWED  
**Version:** 2.0.0-post-CR0008  
**Date:** 2026-09-02 UTC  
**Candidate disposition:** CURRENT PASS pending independent VER-0307, EVD-0307 and guarded runtime read-back.

## 1. Revalidation decision

The historical TSK-0307 catalogue remains valid for its nine instruction classes, applicability model, metadata fields, truth-state rules, recovery rules and trigger-based source maintenance. Current revalidation is required because direct predecessor TSK-0317 is newer and the historical parent-facing copy uses the superseded visible name `UseSafeWeb` rather than the owner-approved `SafeWeb` / `SafeWeb DNS` language.

No new install mechanism is introduced. The current catalogue keeps Android native Private DNS provider-hostname guidance and the bounded iPhone encrypted-DNS profile route. Exact technical identifiers continue to use the `usesafeweb.com` domain because they are technical endpoints, not visible-brand copy.

## 2. Current official-source review — 2026-09-02

Current first-party sources were rechecked before this revalidation:

- **ANDROID-HELP-PRIVATE-DNS:** https://support.google.com/android/answer/9654714 — Android still exposes `Off`, `Automatic`, and `Private DNS provider hostname`; Android Help explicitly limits Private DNS protection to DNS questions/answers.
- **ANDROID-DPM-PRIVATE-DNS:** https://developer.android.com/reference/android/app/admin/DevicePolicyManager — specified-host Private DNS uses a hostname serving DNS-over-TLS; managed-device APIs can fail when the host is invalid/unreachable and have device-owner constraints.
- **ANDROID-LINKPROPERTIES-DNS:** https://developer.android.com/reference/android/net/LinkProperties — current APIs still expose whether Private DNS is active and the strict-mode private-DNS server name.
- **APPLE-DNS-SETTINGS:** https://support.apple.com/guide/deployment/dns-settings-payload-settings-dep86469ba99/web — Apple still documents encrypted DNS Settings payloads using HTTPS or TLS and Server URL semantics for HTTPS.
- **APPLE-PROFILE-INSTALL/REMOVE:** https://support.apple.com/guide/iphone/install-or-remove-configuration-profiles-iph6c493b19/ios — profile installation requires explicit user permission and installed profiles are managed under VPN & Device Management.
- **APPLE-PROFILE-REMOVE-SAFETY:** https://support.apple.com/guide/personal-safety/ips327569a75/web — profile deletion removes the settings/information owned by that profile; managed/school/business devices require caution before deletion.

Current platform facts remain compatible with current TSK-0317. Apple security/device-management policy may prevent or constrain profile installation/removal; SafeWeb must not advise weakening a required security/management control simply to obtain a positive protection state.

## 3. Current project sources

- Current direct predecessor `TSK_0317_POST_CR0008_CURRENT_PLATFORM_PATH_REVALIDATION_2026-09-02.md` — current PASS.
- Current TSK-0408 DNS endpoint/profile authority remains the source of exact technical endpoint identity.
- Current TSK-0409 support/conflict matrix remains the source of supported/uncertain/not-covered applicability.
- Current TSK-0320 remains the source of protection-state evidence thresholds and copy semantics.
- Historical TSK-0307 catalogue `TSK_0307_SOURCE_BACKED_INSTRUCTION_CONTENT_CATALOGUE_2026-08-28.md`, blob `b6d58ffca7af4124c563164361ff01043561abb9`, remains provenance for still-valid catalogue structure/content.
- Historical TSK-0307 evidence `TSK_0307_SOURCE_BACKED_INSTRUCTION_CONTENT_CATALOGUE_EVIDENCE_2026-08-28.md` remains provenance for the nine-class field-by-field verification.

## 4. Catalogue-wide current rules

1. Parent-facing product name is **SafeWeb** / **SafeWeb DNS**. Do not use generic visible-brand copy such as `UseSafeWeb DNS`, `Get UseSafeWeb profile`, or `Turn on UseSafeWeb`.
2. Exact technical identifiers remain literal: `dns.usesafeweb.com` and, where owned/required, `https://dns.usesafeweb.com/dns-query`.
3. Accountless setup/verification/help/removal remains complete. Optional account/session/dashboard/device-management does not change the OS DNS mechanism and never substitutes for technical verification.
4. Platform menu labels are source-owned; OEM/OS wording may vary. Do not invent one immutable menu route where the official source explicitly allows variation.
5. Profile/setting presence, parent confirmation, account ownership or dashboard state never equals `Verified`.
6. No browsing/query/activity history or child profile/activity is requested for verification.
7. Unsupported, managed, locked or conflicting combinations stop with truthful Action needed / Not covered / Status uncertain behavior rather than speculative alternate clients.
8. Retry requires changed condition/new evidence. Do not repeatedly replay a failed consequential platform action without reconciliation.
9. Localized variants preserve source meaning and do not activate a market or broaden support.
10. Review is trigger-based: affected rows become stale after platform/source/endpoint/profile/support/truth-state changes or contradictory target evidence.

## 5. Current registry

| ID | Purpose | Platform/version | Region/locale applicability | Official/current source | Owner | Last verified | Review trigger | Known limits | Test reference |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `INS-AND-SETUP-01` | Configure SafeWeb DNS | Supported Android phone, Android 9+ with usable Private DNS provider-hostname control | Mechanism where supported; en-GB baseline; tr-TR/ar provisional | ANDROID-HELP-PRIVATE-DNS; ANDROID-DPM-PRIVATE-DNS; current TSK-0317/0408/0409 | UX + Network Engineering | 2026-09-02 | Android/OEM setting path; endpoint/certificate/support change; contradictory target evidence | Tablets/ChromeOS/managed/locked/missing setting not implied; network may block DoT | TSK-0317; TSK-0409; TSK-0511/0514 |
| `INS-AND-VERIFY-01` | Verify Android SafeWeb DNS | Same after configuration | Same | ANDROID-LINKPROPERTIES-DNS; TSK-0320; current TSK-0317/0408/0409 | Network Engineering + UX | 2026-09-02 | Verifier/endpoint/conflict model changes | Setting presence is insufficient; VPN/app/browser/network resolver may make state uncertain | TSK-0317; TSK-0409; TSK-0511/0207 |
| `INS-AND-REMOVE-01` | Remove/recover Android SafeWeb DNS | Supported Android phone path | Same | ANDROID-HELP-PRIVATE-DNS; current TSK-0317/0409 | UX + Network Engineering | 2026-09-02 | Android removal semantics/recovery/support change | Normal recovery returns to platform normal policy, normally Automatic; removal ends SafeWeb DNS claim | TSK-0317; TSK-0514; TSK-0409 |
| `INS-IOS-SETUP-01` | Configure SafeWeb encrypted-DNS profile | Supported iPhone profile path | Mechanism where supported; en-GB baseline; tr-TR/ar provisional | APPLE-DNS-SETTINGS; APPLE-PROFILE-INSTALL/REMOVE; current TSK-0317/0408/0409 | UX + Network Engineering | 2026-09-02 | iOS/profile/security/install path; profile format/signing/distribution; endpoint/support change | Exact production profile requires separate artifact verification; managed/security-policy-blocked paths not silently bypassed | TSK-0317; TSK-0511/0514; TSK-0409 |
| `INS-IOS-VERIFY-01` | Verify iPhone SafeWeb DNS | Same after profile installation | Same | APPLE-DNS-SETTINGS; TSK-0320; current TSK-0317/0408/0409 | Network Engineering + UX | 2026-09-02 | Verifier/profile/endpoint/conflict change | Profile presence is insufficient; VPN/Private Relay/custom resolver coexistence is not assumed | TSK-0317; TSK-0511/0207; TSK-0409 |
| `INS-IOS-REMOVE-01` | Remove/recover iPhone SafeWeb DNS | Supported iPhone profile path | Same | APPLE-PROFILE-INSTALL/REMOVE; APPLE-PROFILE-REMOVE-SAFETY; current TSK-0317/0409 | UX + Network Engineering | 2026-09-02 | Apple profile removal/security/management semantics change | Remove only the exact SafeWeb profile; managed device policy may constrain removal; profile removal ends its DNS configuration claim only | TSK-0317; TSK-0514; TSK-0409 |
| `INS-COMMON-UNCERTAIN-01` | Truthful conflict/uncertainty state | Any supported path with unresolved VPN/Private Relay/app/browser/network/managed conflict | All locales; no support expansion | TSK-0320; current TSK-0317/0409 | UX + Network Engineering | 2026-09-02 | Conflict compatibility or state taxonomy changes | Do not weaken employer/school/security controls merely to make SafeWeb green | TSK-0317; TSK-0409 |
| `INS-COMMON-NOTCOVERED-01` | Truthful unsupported/not-yet-supported state | Unaccepted OS/device/network/profile combination | All locales | current TSK-0317/0409 | Product/UX | 2026-09-02 | Support matrix adds/removes combination | No speculative alternate VPN/client/profile path; no positive protection claim | TSK-0317; TSK-0409 |
| `INS-COMMON-RECOVERY-01` | Connectivity failure safe recovery | Supported path where SafeWeb configuration materially breaks intended resolution | All locales; platform-specific removal selected underneath | current TSK-0317/0408/0409 | UX + Network Engineering | 2026-09-02 | Recovery/resolver/removal regression | No silent plaintext fallback while retaining a SafeWeb protection claim | TSK-0317; TSK-0514 |

## 6. Current instruction variants

### Android setup

**en-GB:** Open Android's Private DNS setting and choose the provider-hostname option. Enter `dns.usesafeweb.com` and save. Use the hostname exactly as shown — not an `https://` address. Return to SafeWeb so protection can be checked.

**tr-TR (provisional):** Android'da Özel DNS ayarını açın ve sağlayıcı ana bilgisayar adı seçeneğini seçin. `dns.usesafeweb.com` adresini girip kaydedin. Ana bilgisayar adını gösterildiği gibi kullanın; `https://` adresi girmeyin. Korumanın kontrol edilebilmesi için SafeWeb'e geri dönün.

**ar (provisional):** افتح إعداد DNS الخاص في Android واختر خيار اسم مضيف المزوّد. أدخل `dns.usesafeweb.com` ثم احفظ. استخدم اسم المضيف كما هو ظاهر ولا تُدخل عنوانًا يبدأ بـ `https://`. ارجع إلى SafeWeb حتى يمكن التحقق من الحماية.

**Limit:** if the setting is absent, locked, managed or unusable, stop with the current truthful unsupported/uncertain route rather than inventing another setup mechanism.

### Android verification

**en-GB:** Checking SafeWeb DNS… A saved Private DNS setting is not enough on its own. SafeWeb shows **Verified** only when the approved technical check confirms the intended encrypted DNS path. If another VPN, app, browser or network may control DNS, the result can remain **Status uncertain**.

**tr-TR (provisional):** SafeWeb DNS kontrol ediliyor… Özel DNS ayarının kaydedilmiş olması tek başına yeterli değildir. SafeWeb yalnızca onaylı teknik kontrol amaçlanan şifreli DNS yolunu doğruladığında **Doğrulandı** durumunu gösterir. Başka bir VPN, uygulama, tarayıcı veya ağ DNS'i kontrol ediyor olabilir; bu durumda sonuç **Durum belirsiz** kalabilir.

**ar (provisional):** جارٍ التحقق من SafeWeb DNS… حفظ إعداد DNS الخاص وحده لا يكفي. يعرض SafeWeb حالة **تم التحقق** فقط عندما يؤكد الفحص التقني المعتمد مسار DNS المشفّر المقصود. إذا كان VPN أو تطبيق أو متصفح أو شبكة أخرى قد تتحكم في DNS فقد تبقى الحالة **غير مؤكدة**.

### Android removal/recovery

**en-GB:** To remove SafeWeb DNS, leave the custom Private DNS provider-hostname mode and return Android to its normal DNS policy, normally **Automatic**. After removal, SafeWeb no longer claims DNS protection. A neutral connectivity check may confirm recovery.

**tr-TR (provisional):** SafeWeb DNS'i kaldırmak için özel sağlayıcı ana bilgisayar adı modundan çıkın ve Android'i normal DNS politikasına, genellikle **Otomatik** seçeneğine döndürün. Kaldırmadan sonra SafeWeb DNS koruması iddiasında bulunmaz.

**ar (provisional):** لإزالة SafeWeb DNS، اخرج من وضع اسم مضيف مزوّد DNS الخاص وأعد Android إلى سياسة DNS العادية، وعادةً إلى **تلقائي**. بعد الإزالة لا يدّعي SafeWeb استمرار حماية DNS.

### iPhone setup

**en-GB:** Get the exact verified SafeWeb DNS profile for this environment, then follow iPhone's profile-installation flow and explicitly approve the installation in iOS. SafeWeb does not install it silently. If current device-management/security policy blocks installation, do not weaken that control merely to make SafeWeb green; use the truthful current blocked/uncertain route and retry only when conditions change.

**tr-TR (provisional):** Bu ortam için doğrulanmış SafeWeb DNS profilini alın, ardından iPhone'un profil yükleme akışını izleyin ve yüklemeyi iOS'ta açıkça onaylayın. SafeWeb profili sessizce yüklemez. Güvenlik veya cihaz yönetimi ilkesi yüklemeyi engelliyorsa yalnızca SafeWeb'i etkin göstermek için bu kontrolü zayıflatmayın.

**ar (provisional):** احصل على ملف تعريف SafeWeb DNS الذي تم التحقق منه لهذه البيئة، ثم اتبع مسار تثبيت ملف التعريف في iPhone ووافق صراحةً على التثبيت في iOS. لا يثبّت SafeWeb الملف بصمت. إذا منعت سياسة الأمان أو إدارة الجهاز التثبيت، فلا تُضعف هذا التحكم لمجرد إظهار SafeWeb بحالة إيجابية.

### iPhone verification

**en-GB:** Checking SafeWeb DNS… An installed profile or signed-in account is not enough on its own. **Verified** requires the approved technical check. VPN, Private Relay, app/browser custom resolver or other unresolved path conflicts remain evidence-bounded uncertainty/not-covered states.

**tr-TR (provisional):** SafeWeb DNS kontrol ediliyor… Yüklü bir profil veya oturum açılmış hesap tek başına yeterli değildir. **Doğrulandı** durumu için onaylı teknik kontrol gerekir.

**ar (provisional):** جارٍ التحقق من SafeWeb DNS… وجود ملف تعريف مثبّت أو حساب مسجّل الدخول لا يكفي وحده. تتطلب حالة **تم التحقق** الفحص التقني المعتمد.

### iPhone removal/recovery

**en-GB:** In iPhone Settings, identify the exact SafeWeb DNS profile under the current profile-management route and remove that profile. On a school/business-managed device, follow the applicable management policy rather than deleting required profiles without authorization. Removing the SafeWeb profile removes its profile-owned DNS configuration; it does not delete the SafeWeb account/device record or anonymous web state.

**tr-TR (provisional):** iPhone Ayarları'nda mevcut profil yönetimi yolunda SafeWeb DNS profilini bulun ve yalnızca o profili kaldırın. Okul/işletme tarafından yönetilen bir cihazda gerekli profilleri yetkisiz silmek yerine geçerli yönetim politikasını izleyin.

**ar (provisional):** في إعدادات iPhone، حدّد ملف تعريف SafeWeb DNS بالضبط ضمن مسار إدارة الملفات الحالي واحذف هذا الملف فقط. إذا كان الجهاز مُدارًا من مدرسة أو مؤسسة، فاتبع سياسة الإدارة المعمول بها بدل حذف ملفات مطلوبة دون تصريح.

### Common uncertainty

**en-GB:** SafeWeb cannot prove the intended DNS path right now. Keep required VPN, school, work or security controls in place. Change only the condition you understand, then recheck; otherwise keep **Status uncertain** / **Not covered**.

**tr-TR (provisional):** SafeWeb şu anda amaçlanan DNS yolunu doğrulayamıyor. Gerekli VPN, okul, iş veya güvenlik kontrollerini açık bırakın. Yalnızca anladığınız koşulu değiştirdikten sonra yeniden kontrol edin.

**ar (provisional):** لا يستطيع SafeWeb إثبات مسار DNS المقصود الآن. أبقِ عناصر تحكم VPN أو المدرسة أو العمل أو الأمان المطلوبة مفعّلة. غيّر فقط الحالة التي تفهمها ثم أعد التحقق.

### Common not covered

**en-GB:** This device/network combination is not covered by the current SafeWeb setup path. Do not improvise another VPN, DNS client or profile. SafeWeb makes no positive protection claim for this path.

**tr-TR (provisional):** Bu cihaz/ağ birleşimi mevcut SafeWeb kurulum yolu kapsamında değildir. Başka bir VPN, DNS istemcisi veya profil uydurmayın.

**ar (provisional):** هذا المزيج من الجهاز/الشبكة غير مشمول بمسار إعداد SafeWeb الحالي. لا تستخدم مسار VPN أو عميل DNS أو ملف تعريف بديل غير معتمد.

### Common recovery

**en-GB:** If the SafeWeb DNS change materially breaks intended connectivity, use the current platform-specific SafeWeb removal/reset path. After removal, SafeWeb must stop claiming DNS protection. Do not silently fall back to plaintext DNS while displaying SafeWeb as active.

**tr-TR (provisional):** SafeWeb DNS değişikliği bağlantıyı önemli ölçüde bozarsa mevcut platforma özel SafeWeb kaldırma/sıfırlama yolunu kullanın. Kaldırmadan sonra SafeWeb DNS koruması iddiasını durdurmalıdır.

**ar (provisional):** إذا أدى تغيير SafeWeb DNS إلى تعطيل الاتصال المقصود بشكل ملموس، فاستخدم مسار الإزالة/إعادة الضبط الحالي الخاص بالمنصة. بعد الإزالة يجب أن يتوقف SafeWeb عن ادعاء حماية DNS.

## 7. Acceptance reconciliation

All nine current instruction classes retain every ACC-0307 field: official source, platform/version/region, owner, last verification, review trigger, localized variants, known limits and test reference. Current review updates the last-verification date to 2026-09-02 and binds source-sensitive rows to the current first-party platform documents above.

The historical catalogue remains provenance only where compatible. Its generic visible `UseSafeWeb` parent-facing wording is superseded; exact `usesafeweb.com` technical endpoints remain unchanged. No account/dashboard implementation or support claim is added by this catalogue.

## 8. Non-inference

This is internal L4 content/instruction definition only. It does not distribute a production Apple profile, implement account/session/dashboard behavior, prove native-speaker/representative-parent comprehension, authorize legal/privacy completion, public publication, participant processing, payment, market activation, LG-06 or launch.

**TSK-0307 current result candidate: PASS subject to independent VER-0307, durable EVD-0307, guarded runtime reconciliation and exact read-back.**
