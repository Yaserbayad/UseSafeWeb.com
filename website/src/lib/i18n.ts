export const locales = ["en", "tr", "ar"] as const;
export type Locale = (typeof locales)[number];
export const defaultLocale: Locale = "en";

export function isLocale(value: string): value is Locale {
  return locales.includes(value as Locale);
}

export function directionFor(locale: Locale): "ltr" | "rtl" {
  return locale === "ar" ? "rtl" : "ltr";
}

export const localeLabels: Record<Locale, string> = {
  en: "English",
  tr: "Türkçe",
  ar: "العربية",
};

export const sharedCopy: Record<Locale, {
  languageNavLabel: string;
  footer: string;
  setupKicker: string;
  howItWorks: string;
  protectionMap: string;
  protectionMapTitle: string;
  protectionVerified: string;
  setupConfirmed: string;
  actionNeeded: string;
  notCovered: string;
  threeAreas: string;
  journeyTitle: string;
}> = {
  en: {
    languageNavLabel: "Language",
    footer: "SafeWeb · First phone safety setup · No browsing-history product data.",
    setupKicker: "SafeWeb setup",
    howItWorks: "How it works",
    protectionMap: "Protection Map",
    protectionMapTitle: "Truthful status, not a safety score",
    protectionVerified: "Protection verified",
    setupConfirmed: "Setup confirmed",
    actionNeeded: "Action needed",
    notCovered: "Not covered",
    threeAreas: "Three focused areas",
    journeyTitle: "Phone → Internet → Services",
  },
  tr: {
    languageNavLabel: "Dil",
    footer: "SafeWeb · İlk telefon güvenlik kurulumu · Tarama geçmişi ürün verisi yok.",
    setupKicker: "SafeWeb kurulumu",
    howItWorks: "Nasıl çalışır",
    protectionMap: "Koruma Haritası",
    protectionMapTitle: "Güvenlik puanı değil, gerçeğe dayalı durum",
    protectionVerified: "Koruma doğrulandı",
    setupConfirmed: "Kurulum onaylandı",
    actionNeeded: "Eylem gerekli",
    notCovered: "Kapsam dışı",
    threeAreas: "Üç odak alanı",
    journeyTitle: "Telefon → İnternet → Hizmetler",
  },
  ar: {
    languageNavLabel: "اللغة",
    footer: "SafeWeb · إعداد أمان الهاتف الأول · لا توجد بيانات منتج لسجل التصفح.",
    setupKicker: "إعداد SafeWeb",
    howItWorks: "كيف يعمل",
    protectionMap: "خريطة الحماية",
    protectionMapTitle: "حالة واقعية، وليست درجة أمان",
    protectionVerified: "تم التحقق من الحماية",
    setupConfirmed: "تم تأكيد الإعداد",
    actionNeeded: "يلزم اتخاذ إجراء",
    notCovered: "خارج التغطية",
    threeAreas: "ثلاثة مجالات مركزة",
    journeyTitle: "الهاتف ← الإنترنت ← الخدمات",
  },
};
