# TSK-0307 — Source-Backed Instruction and Content Catalogue

**Task:** `TSK-0307 — Create the source-backed instruction/content catalogue with applicability and review triggers`  
**Acceptance:** `ACC-0307`  
**Lifecycle:** L4 — Product Definition, Requirements & Experience Design  
**Authority:** TSK-0317 PASS + TSK-0408/TSK-0409 platform contracts + TSK-0320 truth-state contract + TSK-0316 friction contract + DEC-0050/CR-0003  
**Status:** **PROVISIONAL INTERNAL L4 CATALOGUE / IMPLEMENTATION AND PUBLICATION NOT AUTHORIZED**  
**Date:** 2026-08-28

## 1. Scope and authority boundary

This catalogue freezes the smallest current source-backed instruction set needed for the accepted accountless Android/iPhone encrypted-DNS setup, verification, conflict handling, removal and recovery design. It does not create a new support claim, build UI, generate/distribute a production Apple profile, activate telemetry, recruit participants, or authorize publication/launch.

`RSK-0002` remains OPEN: no representative-parent evidence proves that this copy is easy, understood, preferred or low-support. `REQ-0022` remains unresolved. LG-03/LG-04/LG-05/LG-06 remain non-PASS. Turkish and Arabic variants below are **provisional language variants**, not market activation and not native-speaker/representative-user validation; TSK-0311 retains ownership of final translation-file/fallback architecture.

## 2. Source hierarchy used by this catalogue

1. Current canonical UseSafeWeb platform/support/truth contracts and direct technical evidence.
2. Current first-party platform documentation already rechecked and accepted on 2026-08-28 by TSK-0408/TSK-0409.
3. No third-party blog or remembered UI path may override those sources.

### Current first-party source set

- **ANDROID-HELP-PRIVATE-DNS** — Google Android Help, Private DNS / advanced network settings: `https://support.google.com/android/answer/9654714?hl=en`
- **ANDROID-DPM-PRIVATE-DNS** — Android Developers, DevicePolicyManager specified-host Private DNS / DNS-over-TLS semantics: `https://developer.android.com/reference/android/app/admin/DevicePolicyManager`
- **ANDROID-LINKPROPERTIES-DNS** — Android Developers, LinkProperties Private DNS/certificate semantics: `https://developer.android.com/reference/android/net/LinkProperties`
- **APPLE-DNS-SETTINGS** — Apple Platform Deployment, DNS Settings payload: `https://support.apple.com/en-gb/guide/deployment/dep86469ba99/1/web/1.0`
- **APPLE-PROFILE-REMOVE** — Apple Support/Personal Safety, review/delete configuration profiles: `https://support.apple.com/en-gb/guide/personal-safety/ips327569a75/1.0/web/1.0`

### Canonical UseSafeWeb source/evidence set

- `TSK_0317_PLATFORM_INSTALL_VERIFICATION_REMOVAL_RECOVERY_DESIGN_CANDIDATE_2026-08-28.md`, approved blob `d44daf376d0e8ed1d5839cc3b6b2ac10d090828d`.
- `TSK_0408_USESAFEWEB_DNS_IDENTITY_PLATFORM_ENDPOINT_PROFILE_CONTRACT_2026-08-28.md`, blob `52860ce167fc8a31962cd412772e428d280c8184`.
- `TSK_0409_SUPPORTED_OS_DEVICE_NETWORK_LIMIT_MATRIX_2026-08-28.md`, current runtime PASS.
- TSK-0320 accepted protection-state/copy contract.
- TSK-0511 supported-device encrypted-DNS verification evidence.
- TSK-0514 external-network/removal-recovery evidence.
- TSK-0207 privacy-persistence evidence.

## 3. Catalogue-wide rules

- **Content owner:** UX/Content unless a row names a more specific technical owner.
- **Technical owner:** Network Engineering for resolver/mechanism correctness; Product/UX for routing and copy.
- **Last verification:** 2026-08-28 for every entry in this v1 catalogue.
- **Review is trigger-based, not assumed current forever.** Re-verify an affected entry before use after any source/platform/support/endpoint/profile/truth-state change listed in its row.
- **Localized copy never broadens support.** A Turkish/Arabic variant can exist while the market/region remains inactive.
- **Platform menu labels are source-owned.** Where Android OEM/iOS wording can vary, the instruction describes the semantic setting/action and the delivery layer must use the current source/version-specific label rather than inventing one immutable route.
- **Verification copy is evidence-bounded.** Parent confirmation/profile presence cannot produce `Verified`.
- **No browsing/query history is requested.** Verification and recovery use controlled/synthetic checks.

## 4. Registry

| ID | Purpose | Platform/version | Region/locale applicability | Official/current source | Owner | Last verified | Review trigger | Known limits | Test reference |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `INS-AND-SETUP-01` | Configure native UseSafeWeb DNS | Android phone, Android 9+, usable Private DNS provider-hostname control | Mechanism global where capability exists; active copy baseline en-GB; tr-TR/ar variants provisional; no market activation implied | ANDROID-HELP-PRIVATE-DNS; ANDROID-DPM-PRIVATE-DNS; TSK-0408/0409 | UX + Network Engineering | 2026-08-28 | Android major/settings change; OEM path materially affects supported flow; endpoint/cert/support-row change; contradictory target evidence | Android tablets/ChromeOS/managed or missing/locked setting are not silently supported; network may block DoT/TCP 853 | TSK-0511; TSK-0514; TSK-0409 assertions 1,2,7,8,13 |
| `INS-AND-VERIFY-01` | Verify Android UseSafeWeb DNS state | Same as `INS-AND-SETUP-01` after configuration | Same | ANDROID-LINKPROPERTIES-DNS; TSK-0320; TSK-0408/0409 | Network Engineering + UX | 2026-08-28 | Verifier logic/endpoint/support/conflict model changes; VPN/browser/app resolver evidence changes | Setting presence/parent confirmation is not verification; VPN/custom resolver/blocked network can make state uncertain | TSK-0511; TSK-0207; TSK-0409 assertions 6,9,11,16,17 |
| `INS-AND-REMOVE-01` | Remove/recover Android UseSafeWeb DNS | Supported Android phone path | Same | ANDROID-HELP-PRIVATE-DNS; TSK-0317/0409 | UX + Network Engineering | 2026-08-28 | Android settings/removal semantics change; recovery test regression; support-row change | Normal recovery target is platform normal policy, normally `Automatic`; removal ends UseSafeWeb protection claim | TSK-0514; TSK-0409 assertion 13 |
| `INS-IOS-SETUP-01` | Configure UseSafeWeb DNS profile | iPhone, iOS 14+, approved manual DNS Settings profile path | Mechanism global where allowed; en-GB active copy baseline; tr-TR/ar variants provisional; no market activation implied | APPLE-DNS-SETTINGS; TSK-0408/0409 | UX + Network Engineering | 2026-08-28 | iOS/profile-security/install path changes; profile format/signing/distribution changes; endpoint/cert/support-row change | Exact production `.mobileconfig` must be separately verified before delivery; managed/supervised/unaccepted Apple families not silently supported | TSK-0511; TSK-0514; TSK-0409 assertions 3,4,5 |
| `INS-IOS-VERIFY-01` | Verify iPhone UseSafeWeb DNS state | Same as `INS-IOS-SETUP-01` after profile installation | Same | APPLE-DNS-SETTINGS; TSK-0320; TSK-0408/0409 | Network Engineering + UX | 2026-08-28 | Verifier/profile/endpoint/support/conflict model changes; new Private Relay/VPN coexistence evidence | Profile presence is not verification; VPN/Private Relay/custom resolver coexistence is not assumed | TSK-0511; TSK-0207; TSK-0409 assertions 6,9,10,11,16,17 |
| `INS-IOS-REMOVE-01` | Remove/recover iPhone UseSafeWeb DNS | Supported iPhone profile path | Same | APPLE-PROFILE-REMOVE; TSK-0317/0409 | UX + Network Engineering | 2026-08-28 | Apple profile-removal path/semantics change; recovery regression; support-row change | Remove the exact UseSafeWeb profile; removal ends UseSafeWeb protection claim | TSK-0514; TSK-0409 assertion 14 |
| `INS-COMMON-UNCERTAIN-01` | Truthful conflict/uncertainty state | Any current supported phone path with unresolved VPN/Private Relay/browser/app/network/managed conflict | All locales; copy variant only, not support expansion | TSK-0320; TSK-0409 | UX + Network Engineering | 2026-08-28 | Any conflict becomes directly proven compatible/incompatible; state taxonomy changes | Must not instruct disabling required employer/school/security controls merely to turn status green | TSK-0409 assertions 9,10,11,15,17 |
| `INS-COMMON-NOTCOVERED-01` | Truthful unsupported/not-yet-supported state | Unaccepted OS/device/network/profile combination | All locales; copy variant only | TSK-0409 | Product/UX | 2026-08-28 | Support matrix adds/removes a combination | Do not improvise another VPN/client/profile path; no positive protection claim | TSK-0409 assertions 5,12,15 |
| `INS-COMMON-RECOVERY-01` | Connectivity failure safe recovery | Supported path where UseSafeWeb configuration materially breaks intended resolution | All locales; platform-specific removal instruction selected underneath | TSK-0317; TSK-0408/0409 | UX + Network Engineering | 2026-08-28 | Recovery path or resolver behavior changes; removal regression | No silent plaintext fallback while continuing UseSafeWeb protection claim | TSK-0514; TSK-0317 acceptance assertions 10-12 |

## 5. Instruction variants

### INS-AND-SETUP-01 — Android setup

**en-GB — baseline**

> Open Android's Private DNS setting and choose the custom provider-hostname option. Enter `dns.usesafeweb.com` and save. Use the hostname exactly as shown — not an `https://` address. Return to UseSafeWeb so protection can be checked.

**tr-TR — provisional language variant**

> Android'da Özel DNS ayarını açın ve özel sağlayıcı ana bilgisayar adı seçeneğini seçin. `dns.usesafeweb.com` adresini girip kaydedin. Ana bilgisayar adını gösterildiği gibi kullanın; `https://` adresi girmeyin. Korumanın kontrol edilebilmesi için UseSafeWeb'e geri dönün.

**ar — provisional language variant**

> افتح إعداد DNS الخاص في Android واختر خيار اسم مضيف المزوّد المخصّص. أدخل `dns.usesafeweb.com` ثم احفظ. استخدم اسم المضيف كما هو ظاهر ولا تُدخل عنوانًا يبدأ بـ `https://`. ارجع إلى UseSafeWeb حتى يمكن التحقق من الحماية.

**Known-limit note:** OEM wording/navigation can differ. If the provider-hostname control is absent, locked or unusable, stop and show Not covered/uncertain rather than inventing another setup method.

### INS-AND-VERIFY-01 — Android verification

**en-GB — baseline**

> Checking UseSafeWeb DNS… A saved Private DNS setting is not enough on its own. UseSafeWeb shows **Verified** only when the approved technical check confirms the intended encrypted DNS path. If another VPN, app, browser or network may control DNS, the result can stay **Status uncertain**.

**tr-TR — provisional language variant**

> UseSafeWeb DNS kontrol ediliyor… Özel DNS ayarının kaydedilmiş olması tek başına yeterli değildir. UseSafeWeb yalnızca onaylı teknik kontrol amaçlanan şifreli DNS yolunu doğruladığında **Doğrulandı** durumunu gösterir. Başka bir VPN, uygulama, tarayıcı veya ağ DNS'i kontrol ediyor olabilir; bu durumda sonuç **Durum belirsiz** kalabilir.

**ar — provisional language variant**

> جارٍ التحقق من UseSafeWeb DNS… حفظ إعداد DNS الخاص وحده لا يكفي. يعرض UseSafeWeb حالة **تم التحقق** فقط عندما يؤكد الفحص التقني المعتمد أن مسار DNS المشفّر المقصود يعمل. إذا كان VPN أو تطبيق أو متصفح أو شبكة أخرى قد تتحكم في DNS فقد تبقى الحالة **غير مؤكدة**.

**Known-limit note:** no real browsing/domain history is requested or stored to perform this check.

### INS-AND-REMOVE-01 — Android removal/recovery

**en-GB — baseline**

> To remove UseSafeWeb DNS, leave the custom Private DNS provider-hostname mode and return Android to its normal DNS policy, normally **Automatic**. After removal, UseSafeWeb no longer claims DNS protection. UseSafeWeb may run a neutral connectivity check to confirm recovery.

**tr-TR — provisional language variant**

> UseSafeWeb DNS'i kaldırmak için özel Özel DNS sağlayıcı ana bilgisayar adı modundan çıkın ve Android'i normal DNS politikasına, genellikle **Otomatik** seçeneğine döndürün. Kaldırmadan sonra UseSafeWeb DNS koruması iddiasında bulunmaz. Bağlantının geri geldiğini doğrulamak için tarafsız bir bağlantı kontrolü yapılabilir.

**ar — provisional language variant**

> لإزالة UseSafeWeb DNS، اخرج من وضع اسم مضيف مزوّد DNS الخاص المخصّص وأعد Android إلى سياسة DNS العادية، وعادةً إلى **تلقائي**. بعد الإزالة لا يدّعي UseSafeWeb استمرار حماية DNS. قد يجري UseSafeWeb فحص اتصال محايد للتأكد من عودة الاتصال.

### INS-IOS-SETUP-01 — iPhone setup

**en-GB — baseline**

> Get the exact verified UseSafeWeb DNS profile for this environment, then follow iPhone's profile-installation flow and approve the installation in iOS. The profile uses UseSafeWeb's encrypted DNS endpoint. Installing the profile requires your explicit iPhone approval; UseSafeWeb does not install it silently. Return to UseSafeWeb after installation so protection can be checked.

**tr-TR — provisional language variant**

> Bu ortam için doğrulanmış tam UseSafeWeb DNS profilini alın, ardından iPhone'un profil yükleme akışını izleyin ve yüklemeyi iOS'ta onaylayın. Profil UseSafeWeb'in şifreli DNS uç noktasını kullanır. Profilin yüklenmesi iPhone'da açık onayınızı gerektirir; UseSafeWeb profili sessizce yüklemez. Kurulumdan sonra korumanın kontrol edilebilmesi için UseSafeWeb'e geri dönün.

**ar — provisional language variant**

> احصل على ملف تعريف UseSafeWeb DNS الدقيق والمتحقق منه لهذه البيئة، ثم اتبع مسار تثبيت ملف التعريف في iPhone ووافق على التثبيت داخل iOS. يستخدم الملف نقطة DNS المشفّرة الخاصة بـ UseSafeWeb. يتطلب التثبيت موافقتك الصريحة على iPhone؛ ولا يقوم UseSafeWeb بتثبيته بصمت. ارجع إلى UseSafeWeb بعد التثبيت حتى يمكن التحقق من الحماية.

**Known-limit note:** this catalogue does not generate or authorize a production `.mobileconfig`; delivery is allowed only for an exact separately verified artifact. Managed/supervised restrictions remain outside the current self-service support baseline.

### INS-IOS-VERIFY-01 — iPhone verification

**en-GB — baseline**

> Checking UseSafeWeb DNS… An installed profile is not enough on its own. UseSafeWeb shows **Verified** only when the approved technical check confirms the intended encrypted DNS path. If VPN, iCloud Private Relay or another resolver path cannot be ruled out, the result stays **Status uncertain** or **Not covered** as applicable.

**tr-TR — provisional language variant**

> UseSafeWeb DNS kontrol ediliyor… Yüklü bir profil tek başına yeterli değildir. UseSafeWeb yalnızca onaylı teknik kontrol amaçlanan şifreli DNS yolunu doğruladığında **Doğrulandı** durumunu gösterir. VPN, iCloud Private Relay veya başka bir çözümleyici yolunun etkisi dışlanamıyorsa sonuç uygun şekilde **Durum belirsiz** veya **Kapsanmıyor** olarak kalır.

**ar — provisional language variant**

> جارٍ التحقق من UseSafeWeb DNS… وجود ملف تعريف مثبّت وحده لا يكفي. يعرض UseSafeWeb حالة **تم التحقق** فقط عندما يؤكد الفحص التقني المعتمد مسار DNS المشفّر المقصود. إذا تعذّر استبعاد تأثير VPN أو iCloud Private Relay أو مسار محلّل آخر فتبقى الحالة **غير مؤكدة** أو **غير مشمولة** حسب الحالة.

### INS-IOS-REMOVE-01 — iPhone removal/recovery

**en-GB — baseline**

> To remove UseSafeWeb DNS, remove the exact UseSafeWeb DNS profile from iPhone's profile-management settings. Removing the profile removes its UseSafeWeb DNS settings. After removal, UseSafeWeb no longer claims DNS protection and may run a neutral connectivity check to confirm recovery.

**tr-TR — provisional language variant**

> UseSafeWeb DNS'i kaldırmak için iPhone'un profil yönetimi ayarlarından tam UseSafeWeb DNS profilini kaldırın. Profilin kaldırılması ona bağlı UseSafeWeb DNS ayarlarını da kaldırır. Kaldırmadan sonra UseSafeWeb DNS koruması iddiasında bulunmaz ve bağlantının geri geldiğini doğrulamak için tarafsız bir bağlantı kontrolü yapabilir.

**ar — provisional language variant**

> لإزالة UseSafeWeb DNS، احذف ملف تعريف UseSafeWeb DNS المحدد من إعدادات إدارة ملفات التعريف في iPhone. تؤدي إزالة الملف إلى إزالة إعدادات UseSafeWeb DNS المرتبطة به. بعد الإزالة لا يدّعي UseSafeWeb استمرار حماية DNS وقد يجري فحص اتصال محايد للتأكد من عودة الاتصال.

### INS-COMMON-UNCERTAIN-01 — uncertain/conflict state

**en-GB — baseline:** `UseSafeWeb cannot currently confirm which DNS path this traffic is using. Protection status is uncertain. Do not change a required work, school or security VPN just to make this status green.`  
**tr-TR — provisional:** `UseSafeWeb şu anda bu trafiğin hangi DNS yolunu kullandığını doğrulayamıyor. Koruma durumu belirsiz. Yalnızca bu durumu yeşile çevirmek için gerekli bir iş, okul veya güvenlik VPN'ini değiştirmeyin.`  
**ar — provisional:** `لا يستطيع UseSafeWeb حاليًا تأكيد مسار DNS الذي تستخدمه هذه الحركة. حالة الحماية غير مؤكدة. لا تغيّر VPN مطلوبًا للعمل أو المدرسة أو الأمان لمجرد جعل الحالة خضراء.`

### INS-COMMON-NOTCOVERED-01 — unsupported state

**en-GB — baseline:** `This device or network path is not currently covered by the UseSafeWeb setup baseline. UseSafeWeb will not guess another DNS client or claim protection without accepted evidence.`  
**tr-TR — provisional:** `Bu cihaz veya ağ yolu şu anda UseSafeWeb kurulum kapsamına dahil değildir. UseSafeWeb kabul edilmiş kanıt olmadan başka bir DNS istemcisi tahmin etmez veya koruma iddiasında bulunmaz.`  
**ar — provisional:** `هذا الجهاز أو مسار الشبكة غير مشمول حاليًا بخط إعداد UseSafeWeb المعتمد. لن يخمّن UseSafeWeb عميل DNS آخر ولن يدّعي الحماية من دون دليل مقبول.`

### INS-COMMON-RECOVERY-01 — connectivity recovery

**en-GB — baseline:** `If UseSafeWeb DNS is preventing normal connectivity, remove/reset the UseSafeWeb DNS configuration using the platform-specific removal steps. Restoring normal DNS ends the UseSafeWeb protection claim until setup is completed and verified again.`  
**tr-TR — provisional:** `UseSafeWeb DNS normal bağlantıyı engelliyorsa platforma özel kaldırma adımlarını kullanarak UseSafeWeb DNS yapılandırmasını kaldırın veya sıfırlayın. Normal DNS'e dönüş, kurulum yeniden tamamlanıp doğrulanana kadar UseSafeWeb koruma iddiasını sona erdirir.`  
**ar — provisional:** `إذا كان UseSafeWeb DNS يمنع الاتصال الطبيعي، فأزل أو أعد ضبط إعداد UseSafeWeb DNS باستخدام خطوات الإزالة الخاصة بالمنصة. تؤدي العودة إلى DNS العادي إلى إنهاء ادعاء حماية UseSafeWeb إلى أن يكتمل الإعداد ويُتحقق منه من جديد.`

## 6. Applicability and routing rules

1. Show `INS-AND-*` only for the accepted Android-phone support tuple from TSK-0409.
2. Show `INS-IOS-*` only for the accepted iPhone support tuple and only after the exact profile artifact is independently accepted for the current environment.
3. Never substitute Android hostname input with the DoH URL or Apple profile path with hostname-only Android instructions.
4. Do not show a protocol chooser.
5. If support cannot be established, route to `INS-COMMON-NOTCOVERED-01` or `INS-COMMON-UNCERTAIN-01` instead of optimistic setup.
6. Conflict copy cannot instruct the parent to weaken unrelated work/school/security controls merely to get a positive status.
7. Verification copy cannot infer protection from an installed profile, saved setting, parent confirmation, ordinary browsing success or DNS resolution alone.
8. Removal copy always ends the active UseSafeWeb DNS protection claim.

## 7. Review-trigger matrix

| Change/evidence event | Entries that must be re-verified before reuse |
| --- | --- |
| Android major release or Private DNS UI/semantics change | `INS-AND-SETUP-01`, `INS-AND-VERIFY-01`, `INS-AND-REMOVE-01` |
| iOS major release or profile install/remove/security behavior change | `INS-IOS-SETUP-01`, `INS-IOS-VERIFY-01`, `INS-IOS-REMOVE-01` |
| Resolver hostname, DoH path, certificate, transport or port change | All affected setup/verify entries |
| New verified Apple profile artifact/format/signing/distribution path | `INS-IOS-SETUP-01`, `INS-IOS-VERIFY-01`, `INS-IOS-REMOVE-01` |
| Support matrix expands/retracts device/network combination | All entries whose applicability changes |
| VPN/Private Relay/browser/app resolver evidence changes | Verification + uncertain/not-covered entries |
| Protection-state taxonomy/evidence rule changes | Both verify entries + common state copy |
| Direct target evidence contradicts an instruction | The contradicted entry is immediately stale until corrected/reverified |
| Translation architecture or reviewed locale wording changes | Affected localized variant; English source semantics remain the comparison baseline |
| Public-release decision occurs | Entire catalogue requires release-current source/read-back verification; this L4 artifact alone cannot authorize publication |

## 8. Localization status and ownership

| Locale | Current status | Meaning |
| --- | --- | --- |
| `en-GB` | **SOURCE-ALIGNED BASELINE** | English semantic copy is the current authoritative content baseline for this catalogue. |
| `tr-TR` | **PROVISIONAL LANGUAGE VARIANT** | Translation exists for design/localization readiness; not native-user validated and does not activate Turkey. |
| `ar` | **PROVISIONAL LANGUAGE VARIANT** | Translation exists for design/localization readiness; not native-user validated and does not activate any Arabic-speaking market. |

TSK-0311 will own externalized translation keys/files, locale metadata, plural/date rules, fallback and content-version mechanics after its HUMAN_ONLY dependency path is satisfied. This catalogue owns the instruction semantics and source/applicability metadata, not the final localization architecture.

## 9. Acceptance result

ACC-0307 requires every instruction to have an official source, platform/version/region, owner, last verification, review trigger, localized variants, known limits and test reference.

This catalogue provides those fields for all nine current instruction classes, includes en-GB plus explicit provisional tr-TR/ar language variants, binds each instruction to current accepted platform/canonical sources, defines applicability and review triggers, and preserves current support/privacy/truth/recovery boundaries.

**TSK-0307 result: PASS candidate subject to independent verification and canonical runtime read-back.**