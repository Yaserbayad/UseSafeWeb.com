export type IntakeChoice = 'android' | 'iphone' | 'other';
export type IntakeRouteDecision =
  | { state: 'supported'; deviceFamily: 'android' | 'iphone'; href: string }
  | { state: 'unsupported'; deviceFamily: null; href: string };

const locales = new Set(['en-GB', 'tr-TR', 'ar']);
const choices = new Set<IntakeChoice>(['android', 'iphone', 'other']);
const expectedKeys = ['choice', 'locale'];

export function resolveIntakeRoute(value: unknown): IntakeRouteDecision {
  if (!value || typeof value !== 'object' || Array.isArray(value)) {
    throw new TypeError('invalid intake routing input');
  }

  const candidate = value as Record<string, unknown>;
  const keys = Object.keys(candidate).sort();
  if (keys.length !== expectedKeys.length || keys.some((key, index) => key !== expectedKeys[index])) {
    throw new TypeError('invalid intake routing input');
  }

  const locale = candidate.locale;
  const choice = candidate.choice;
  if (typeof locale !== 'string' || !locales.has(locale) || typeof choice !== 'string' || !choices.has(choice as IntakeChoice)) {
    throw new TypeError('invalid intake routing input');
  }

  if (choice === 'other') {
    return { state: 'unsupported', deviceFamily: null, href: `/${locale}/compatibility` };
  }

  const deviceFamily = choice as 'android' | 'iphone';
  return { state: 'supported', deviceFamily, href: `/${locale}/setup/native?platform=${deviceFamily}` };
}
