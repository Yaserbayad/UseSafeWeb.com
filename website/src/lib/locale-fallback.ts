export type LocaleResolution<T> = {
  value: T;
  sourceLocale: string;
};

function fallbackChain(start: string, fallbackMap: Record<string, string | null | undefined>): string[] {
  const chain: string[] = [];
  const seen = new Set<string>();
  let current: string | null | undefined = start;

  while (current) {
    if (seen.has(current)) throw new Error(`locale fallback cycle at ${current}`);
    seen.add(current);
    chain.push(current);
    current = fallbackMap[current];
  }

  return chain;
}

export function resolveLocaleValue<T>(
  requestedLocale: string,
  values: Partial<Record<string, T>>,
  fallbackMap: Record<string, string | null | undefined>,
  defaultLocale: string,
): LocaleResolution<T> {
  const requestedChain = fallbackChain(requestedLocale, fallbackMap);
  const defaultChain = requestedChain.includes(defaultLocale) ? [] : fallbackChain(defaultLocale, fallbackMap);
  const candidates = [...requestedChain, ...defaultChain.filter((locale) => !requestedChain.includes(locale))];

  for (const locale of candidates) {
    const value = values[locale];
    if (value !== undefined) return { value, sourceLocale: locale };
  }

  throw new Error(`missing localized value for ${requestedLocale}`);
}
