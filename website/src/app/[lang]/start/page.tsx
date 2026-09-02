import Link from "next/link";
import { notFound } from "next/navigation";
import { isLocale, type Locale } from "@/lib/i18n";

const copy: Record<Locale, { title: string; intro: string; accountless: string; legend: string; iphone: string; android: string; continue: string; selected: string; back: string }> = {
  en: { title: "Start first-phone safety setup", intro: "Begin with the phone you are setting up. SafeWeb keeps this core path available without an account.", accountless: "No account, payment card, child name, or browsing history is required for the core setup.", legend: "Which phone are you setting up?", iphone: "iPhone", android: "Android phone", continue: "Continue", selected: "Phone type selected. The next guided phone-settings step follows from this accountless start state.", back: "Back to overview" },
  tr: { title: "İlk telefon güvenlik kurulumunu başlatın", intro: "Kurulum yaptığınız telefonla başlayın. SafeWeb temel yolu hesap olmadan kullanılabilir tutar.", accountless: "Temel kurulum için hesap, ödeme kartı, çocuğun adı veya tarama geçmişi gerekmez.", legend: "Hangi telefonu kuruyorsunuz?", iphone: "iPhone", android: "Android telefon", continue: "Devam et", selected: "Telefon türü seçildi. Sonraki yönlendirilmiş telefon ayarları adımı bu hesapsız başlangıç durumundan devam eder.", back: "Genel bakışa dön" },
  ar: { title: "ابدأ إعداد أمان الهاتف الأول", intro: "ابدأ بالهاتف الذي تقوم بإعداده. يبقى المسار الأساسي في SafeWeb متاحًا دون حساب.", accountless: "لا يتطلب الإعداد الأساسي حسابًا أو بطاقة دفع أو اسم الطفل أو سجل التصفح.", legend: "ما نوع الهاتف الذي تقوم بإعداده؟", iphone: "iPhone", android: "هاتف Android", continue: "متابعة", selected: "تم اختيار نوع الهاتف. تبدأ الخطوة الإرشادية التالية لإعدادات الهاتف من حالة البدء هذه دون حساب.", back: "العودة إلى النظرة العامة" },
};

export default async function StartPage({ params, searchParams }: { params: Promise<{ lang: string }>; searchParams: Promise<{ platform?: string }> }) {
  const { lang } = await params;
  if (!isLocale(lang)) notFound();
  const { platform } = await searchParams;
  const selected = platform === "iphone" || platform === "android" ? platform : undefined;
  const text = copy[lang];

  return (
    <main id="main-content" className="sw-stack">
      <div className="sw-copy sw-stack">
        <p className="sw-kicker">SafeWeb setup</p>
        <h1 className="sw-title">{text.title}</h1>
        <p>{text.intro}</p>
        <div className="sw-callout"><strong>{text.accountless}</strong></div>
      </div>

      <form className="sw-card usw-start-form" method="get" action={`/${lang}/start`}>
        <fieldset>
          <legend><strong>{text.legend}</strong></legend>
          <label className="usw-choice"><input type="radio" name="platform" value="iphone" defaultChecked={selected === "iphone"} required /><span>{text.iphone}</span></label>
          <label className="usw-choice"><input type="radio" name="platform" value="android" defaultChecked={selected === "android"} required /><span>{text.android}</span></label>
          <button className="sw-button" type="submit">{text.continue}</button>
        </fieldset>
      </form>

      {selected ? <div className="sw-panel" role="status"><p>{text.selected}</p></div> : null}
      <p><Link href={`/${lang}`}>← {text.back}</Link></p>
    </main>
  );
}
