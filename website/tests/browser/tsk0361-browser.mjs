import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';
import { createRequire } from 'node:module';
import { chromium } from 'playwright';

const require = createRequire(import.meta.url);
const axeSource = readFileSync(require.resolve('axe-core/axe.min.js'), 'utf8');
const base = process.env.BASE_URL ?? 'http://127.0.0.1:3000';
const locales = [
  { id: 'en-GB', dir: 'ltr' },
  { id: 'tr-TR', dir: 'ltr' },
  { id: 'ar', dir: 'rtl' },
];
const publicPaths = ['', '/how-it-works', '/compatibility', '/protection-and-limits', '/privacy', '/help'];
const operationalPaths = [
  '/start',
  '/setup/route',
  '/setup/native?platform=android',
  '/setup/native?platform=iphone',
  '/setup/dns?platform=android',
  '/setup/dns?platform=iphone',
  '/status',
];
const invalidPlatformPaths = [
  '/setup/native',
  '/setup/native?platform=invalid',
  '/setup/dns',
  '/setup/dns?platform=invalid',
];
const viewports = [
  { width: 320, height: 720 },
  { width: 768, height: 900 },
  { width: 1024, height: 900 },
  { width: 1440, height: 1000 },
];

const browser = await chromium.launch({ headless: true });
const failures = [];

function record(label, fn) {
  return Promise.resolve()
    .then(fn)
    .catch((error) => failures.push(`${label}: ${error.stack ?? error}`));
}

async function openChecked(page, urlPath, expectedLocale, expectedDir) {
  const response = await page.goto(`${base}${urlPath}`, { waitUntil: 'networkidle' });
  assert.ok(response, 'missing HTTP response');
  assert.equal(response.status(), 200, `HTTP ${response.status()}`);
  assert.equal(await page.locator('h1').count(), 1, 'page must have exactly one h1');
  assert.equal(
    await page.locator('[data-locale-root]').getAttribute('lang'),
    expectedLocale,
    'locale root lang mismatch',
  );
  assert.equal(await page.locator('[data-locale-root]').getAttribute('dir'), expectedDir, 'locale root dir mismatch');
  assert.equal(await page.locator('html').getAttribute('lang'), expectedLocale, 'document language mismatch');
  assert.equal((await page.locator('html').getAttribute('dir')) ?? 'ltr', expectedDir, 'document direction mismatch');
  const overflow = await page.evaluate(() => ({
    document: document.documentElement.scrollWidth - document.documentElement.clientWidth,
    body: document.body.scrollWidth - document.body.clientWidth,
  }));
  assert.ok(overflow.document <= 1 && overflow.body <= 1, `horizontal overflow ${JSON.stringify(overflow)}`);
  const headers = response.headers();
  for (const name of [
    'content-security-policy',
    'x-content-type-options',
    'referrer-policy',
    'permissions-policy',
    'strict-transport-security',
  ]) {
    assert.ok(headers[name], `missing security header ${name}`);
  }
  assert.equal(headers['x-powered-by'], undefined, 'X-Powered-By must be disabled');
  const bodyText = (await page.locator('body').innerText()).toLowerCase();
  for (const forbidden of ['100% safe', 'completely safe', 'fully protected'])
    assert.equal(bodyText.includes(forbidden), false, `premature claim ${forbidden}`);
}

for (const locale of locales) {
  await record(`${locale.id} public routes`, async () => {
    const context = await browser.newContext({ viewport: { width: 1440, height: 1000 } });
    const page = await context.newPage();
    const consoleErrors = [];
    page.on('console', (message) => {
      if (message.type() === 'error') consoleErrors.push(message.text());
    });
    page.on('pageerror', (error) => consoleErrors.push(String(error)));
    for (const path of publicPaths) {
      const urlPath = `/${locale.id}${path}`;
      await openChecked(page, urlPath, locale.id, locale.dir);
      const canonical = await page.locator('link[rel="canonical"]').getAttribute('href');
      assert.equal(canonical, `https://usesafeweb.com${urlPath}`, `canonical mismatch for ${urlPath}`);
      const robots = (await page.locator('meta[name="robots"]').getAttribute('content')) ?? '';
      assert.equal(/noindex/i.test(robots), false, `public page unexpectedly noindex: ${urlPath}`);
    }
    assert.deepEqual(consoleErrors, [], `console/page errors: ${consoleErrors.join(' | ')}`);
    await context.close();
  });

  await record(`${locale.id} operational routes`, async () => {
    const context = await browser.newContext({ viewport: { width: 320, height: 720 } });
    const page = await context.newPage();
    for (const path of operationalPaths) {
      const urlPath = `/${locale.id}${path}`;
      await openChecked(page, urlPath, locale.id, locale.dir);
      const robots = (await page.locator('meta[name="robots"]').getAttribute('content')) ?? '';
      assert.match(robots, /noindex/i, `operational page must be noindex: ${urlPath}`);
    }
    await context.close();
  });

  await record(`${locale.id} responsive home/start`, async () => {
    const context = await browser.newContext();
    const page = await context.newPage();
    for (const viewport of viewports) {
      await page.setViewportSize(viewport);
      await openChecked(page, `/${locale.id}`, locale.id, locale.dir);
      await openChecked(page, `/${locale.id}/start`, locale.id, locale.dir);
    }
    await context.close();
  });
}

await record('invalid or missing platform query fails closed', async () => {
  const context = await browser.newContext({ viewport: { width: 390, height: 844 } });
  const page = await context.newPage();
  for (const path of invalidPlatformPaths) {
    const response = await page.goto(`${base}/en-GB${path}`, { waitUntil: 'networkidle' });
    assert.ok(response, `missing HTTP response for ${path}`);
    assert.equal(response.status(), 404, `invalid/missing platform must return 404 for ${path}`);
  }
  await context.close();
});

await record('keyboard skip-link and accountless journey links', async () => {
  const context = await browser.newContext({ viewport: { width: 320, height: 720 } });
  const page = await context.newPage();
  await page.goto(`${base}/en-GB`, { waitUntil: 'networkidle' });
  await page.keyboard.press('Tab');
  assert.equal(await page.locator(':focus').getAttribute('href'), '#main-content', 'first tab stop must be skip link');
  await page.keyboard.press('Enter');
  assert.equal(await page.locator('#main-content').count(), 1);
  await page.goto(`${base}/en-GB/start`, { waitUntil: 'networkidle' });
  assert.equal(await page.locator('a[href="/en-GB/setup/route"]').count(), 1, 'start must link to phone choice');
  await page.goto(`${base}/en-GB/setup/route`, { waitUntil: 'networkidle' });
  assert.equal(await page.locator('a[href="/en-GB/setup/native?platform=android"]').count(), 1);
  assert.equal(await page.locator('a[href="/en-GB/setup/native?platform=iphone"]').count(), 1);
  await context.close();
});

for (const sample of ['/en-GB', '/en-GB/start', '/ar', '/ar/setup/dns?platform=android']) {
  await record(`axe WCAG 2.2 AA ${sample}`, async () => {
    const context = await browser.newContext({ viewport: { width: 320, height: 720 } });
    const page = await context.newPage();
    await page.goto(`${base}${sample}`, { waitUntil: 'networkidle' });
    await page.addScriptTag({ content: axeSource });
    const result = await page.evaluate(
      async () =>
        await window.axe.run(document, {
          runOnly: { type: 'tag', values: ['wcag2a', 'wcag2aa', 'wcag21aa', 'wcag22aa'] },
        }),
    );
    assert.deepEqual(
      result.violations.map((v) => ({ id: v.id, impact: v.impact, nodes: v.nodes.length })),
      [],
      'axe violations',
    );
    await context.close();
  });
}

await browser.close();

if (failures.length) {
  console.error(`TSK0361_BROWSER_FAILURES=${failures.length}`);
  for (const failure of failures) console.error(`---\n${failure}`);
  process.exit(1);
}

console.log('TSK0361_BROWSER_ACCEPTANCE=PASS');
