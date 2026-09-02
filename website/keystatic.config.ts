import { config, fields, singleton } from "@keystatic/core";

const homeSchema = {
  eyebrow: fields.text({ label: "Eyebrow" }),
  title: fields.text({ label: "Title" }),
  intro: fields.text({ label: "Introduction", multiline: true }),
  accountless: fields.text({ label: "Accountless promise", multiline: true }),
  privacy: fields.text({ label: "Privacy boundary", multiline: true }),
  limitation: fields.text({ label: "Protection limitation", multiline: true }),
  ctaLabel: fields.text({ label: "Start button label" }),
  detailsTitle: fields.text({ label: "Limits heading" }),
  detailsBody: fields.text({ label: "Limits detail", multiline: true }),
};

const storage = process.env.NEXT_PUBLIC_KEYSTATIC_STORAGE === "github"
  ? {
      kind: "github" as const,
      repo: { owner: "Yaserbayad", name: "UseSafeWeb.com" },
      branchPrefix: "content/",
    }
  : { kind: "local" as const };

export default config({
  storage,
  singletons: {
    homeEn: singleton({ label: "Homepage — English", path: "src/content/home/en", format: { data: "json" }, schema: homeSchema }),
    homeTr: singleton({ label: "Homepage — Türkçe", path: "src/content/home/tr", format: { data: "json" }, schema: homeSchema }),
    homeAr: singleton({ label: "Homepage — العربية", path: "src/content/home/ar", format: { data: "json" }, schema: homeSchema }),
  },
});
