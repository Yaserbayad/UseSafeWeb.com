import Link from "next/link";
import { notFound } from "next/navigation";
import { Accordion } from "radix-ui";
import { getHomeContent } from "@/lib/content";
import { isLocale, type Locale } from "@/lib/i18n";

const steps: Record<Locale, Array<{ title: string; body: string }>> = {
  en: [
    { title: "Phone", body: "Review the native safety settings that matter for a first independently used phone." },
    { title: "Internet", body: "Set up encrypted DNS protection and verify what the device is actually using." },
    { title: "Services", body: "Apply one relevant service safeguard, then see what is confirmed, verified, or not covered." },
  ],
  tr: [
    { title: "Telefon", body: "İlk kez bağımsız kullanılan telefon için önemli yerleşik güvenlik ayarlarını gözden geçirin." },
    { title: "İnternet", body: "Şifreli DNS korumasını kurun ve cihazın gerçekte ne kullandığını doğrulayın." },
    { title: "Hizmetler", body: "İlgili bir hizmet korumasını uygulayın; ardından neyin doğrulandığını, onaylandığını veya kapsam dışı olduğunu görün." },
  ],
  ar: [
    { title: "الهاتف", body: "راجع إعدادات الأمان المدمجة المهمة لهاتف يُستخدم بشكل مستقل لأول مرة." },
    { title: "الإنترنت", body: "أعد حماية DNS المشفرة وتحقق مما يستخدمه الجهاز فعليًا." },
    { title: "الخدمات", body: "طبّق وسيلة حماية لخدمة ذات صلة، ثم اعرف ما تم التحقق منه أو تأكيده أو ما هو خارج التغطية." },
  ],
};

export default async function HomePage({ params }: { params: Promise<{ lang: string }> }) {
  const { lang } = await params;
  if (!isLocale(lang)) notFound();
  const content = await getHomeContent(lang);

  return (
    <main id="main-content" className="sw-stack">
      <section className="usw-hero" aria-labelledby="home-title">
        <div className="usw-hero-copy">
          <p className="sw-kicker">{content.eyebrow}</p>
          <h1 id="home-title" className="sw-title">{content.title}</h1>
          <p className="sw-copy">{content.intro}</p>
          <div className="usw-hero-actions">
            <Link className="sw-button" href={`/${lang}/start`}>{content.ctaLabel}</Link>
            <a className="sw-button sw-button--secondary" href="#how-it-works">How it works</a>
          </div>
          <div className="usw-trust-note">
            <p><strong>{content.accountless}</strong></p>
            <p>{content.privacy}</p>
            <p>{content.limitation}</p>
          </div>
        </div>
        <aside className="sw-panel" aria-labelledby="protection-map-heading">
          <p className="sw-kicker">Protection Map</p>
          <h2 id="protection-map-heading">Truthful status, not a safety score</h2>
          <div className="sw-stack">
            <span className="sw-status__label">Protection verified</span>
            <span className="sw-status__label">Setup confirmed</span>
            <span className="sw-status__label">Action needed</span>
            <span className="sw-status__label">Not covered</span>
          </div>
        </aside>
      </section>

      <section id="how-it-works" className="sw-stack" aria-labelledby="how-title">
        <div>
          <p className="sw-kicker">Three focused areas</p>
          <h2 id="how-title">Phone → Internet → Services</h2>
        </div>
        <div className="usw-grid usw-grid--3">
          {steps[lang].map((step, index) => (
            <article className="sw-card" key={step.title}>
              <span className="usw-step-number" aria-hidden="true">{index + 1}</span>
              <h3>{step.title}</h3>
              <p>{step.body}</p>
            </article>
          ))}
        </div>
      </section>

      <section className="sw-card" aria-labelledby="limits-title">
        <Accordion.Root type="single" collapsible>
          <Accordion.Item value="limits">
            <Accordion.Header>
              <Accordion.Trigger className="usw-accordion-trigger" id="limits-title">
                {content.detailsTitle}<span aria-hidden="true">+</span>
              </Accordion.Trigger>
            </Accordion.Header>
            <Accordion.Content className="usw-accordion-content">
              <p className="sw-copy">{content.detailsBody}</p>
            </Accordion.Content>
          </Accordion.Item>
        </Accordion.Root>
      </section>
    </main>
  );
}
