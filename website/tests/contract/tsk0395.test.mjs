import test from 'node:test';
import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';
import { resolve } from 'node:path';

const root = resolve(import.meta.dirname, '../..');
const read = (path) => readFileSync(resolve(root, path), 'utf8');
const json = (path) => JSON.parse(read(path));

const locales = ['en-GB', 'tr-TR', 'ar'];

for (const locale of locales) {
  test(`TSK-0395 ${locale} landing proposition is first-phone-led rather than DNS-led`, () => {
    const content = json(`src/content/${locale}.json`);
    assert.ok(content.home.kicker, 'missing first-phone kicker');
    assert.doesNotMatch(content.home.title, /dns/i, 'landing headline must not make DNS the product proposition');
    assert.doesNotMatch(content.home.summary, /^.*dns/i, 'landing summary must lead with the user outcome, not DNS');
    assert.ok(content.home.primaryLabel, 'missing primary setup CTA');
    assert.ok(content.home.secondaryLabel, 'missing secondary explanation CTA');
  });
}

test('TSK-0395 landing page routes the primary CTA to accountless setup and exposes trust/support navigation', () => {
  const page = read('src/app/[locale]/page.tsx');
  const shell = read('src/components/site-shell.tsx');

  assert.match(page, /href: `\/\$\{locale\}\/start`/);
  assert.match(page, /href: `\/\$\{locale\}\/how-it-works`/);
  assert.match(shell, /\['protection-and-limits', common\.nav\.limits\]/);
  assert.match(shell, /\['privacy', common\.nav\.privacy\]/);
  assert.match(shell, /\['help', common\.nav\.help\]/);
});

test('TSK-0395 public landing retains semantic heading, keyboard-native links, and shared responsive design-system classes', () => {
  const page = read('src/components/content-page.tsx');
  const css = read('src/app/globals.css');

  assert.match(page, /<h1 className="sw-title">/);
  assert.match(page, /<Link[\s\S]*className=\{action\.secondary/);
  assert.match(css, /\.sw-actions/);
  assert.match(css, /@media\s*\(max-width:/);
  assert.doesNotMatch(css, /#[0-9a-fA-F]{6}/, 'landing must consume shared brand tokens rather than a parallel raw palette');
});
