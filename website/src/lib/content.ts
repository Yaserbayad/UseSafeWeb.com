import { createReader } from "@keystatic/core/reader";
import keystaticConfig from "../../keystatic.config";
import type { Locale } from "./i18n";

const reader = createReader(process.cwd(), keystaticConfig);

export async function getHomeContent(locale: Locale) {
  const content = locale === "tr"
    ? await reader.singletons.homeTr.read()
    : locale === "ar"
      ? await reader.singletons.homeAr.read()
      : await reader.singletons.homeEn.read();

  if (!content) throw new Error(`Missing homepage content for ${locale}`);
  return content;
}
