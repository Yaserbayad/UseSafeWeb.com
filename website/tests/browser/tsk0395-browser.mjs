import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';
import { createRequire } from 'node:module';
import { chromium } from 'playwright';

const require = createRequire(import.meta.url);
const axeSource = readFileSync(require.resolve('axe-core/axe.min.js'), 'utf8');
const base = process.env.BASE_URL ?? 'http://127.0.0.1:3000';
const baseOrigin = new URL(base).origin;
const locales = [
  { id: 'en-GB', dir: 'ltr' },
  { id: 'tr-TR', dir: 'ltr' },
  { id: 'ar', dir: 'rtl' },
];
const viewports = [
  { width: 320, height: 720 },
  { width: 768, height: 900 },
  { width: 1024, height: 900 },
  { width: 1440, height: 1000 },
];
const content = Object.fromEntries(
  locales.map(({ id }) => [
    id,
    JSON.parse(readFileSync(new URL(`../../src/content/${id}.json`, import.meta.url), 'utf8')),
  ]),
);

const browser = await chromium.launch({ headless: true });
const failures = [];
const performanceObservations = [];

function record(label, fn) {
  return Promise.resolve()
    .then(fn)
    .catch((error) => failures.push(`${label}: ${error.stack ?? error}`));
}

function assertApprovedEnglishLandingCopy(bundle) {
  assert.equal(bundle.home.kicker, 'First phone safety setup');
  assert.equal(bundle.home.title, 'Set up sensible first-phone safeguards');
  assert.equal(bundle.home.primaryLabel, 'Start setup');
  assert.equal(bundle.home.secondaryLabel, 'See how it works');
  assert.doesNotMatch(bundle.home.title, /dns/i, 'DNS must not become the landing proposition');
  assert.doesNotMatch(bundle.home.kicker, /dns/i, 'DNS must not become the landing category');
  assert.doesNotMatch(bundle.home.primaryLabel, /dns/i, 'DNS must not become the primary CTA');

  const visibleCopy = [
    bundle.home.kicker,
    bundle.home.title,
    bundle.home.summary,
    ...bundle.home.cards.flatMap((card) => [card.title, card.body]),
    bundle.home.noteTitle,
    bundle.home.noteBody,
  ].join(' ');

  for (const prohibited of [
    /complete protection/i,
    /fully protected/i,
    /your child is safe/i,
    /100% safe/i,
    /blocks everything harmful/i,
    /impossible to bypass/i,
    /we collect nothing/i,
    /completely anonymous/i,
    /monitor browsing/i,
    /track your child/i,
  ]) {
    assert.doesNotMatch(visibleCopy, prohibited, `landing copy contains prohibited claim: ${prohibited}`);
  }
}

assertApprovedEnglishLandingCopy(content['en-GB']);

for (const locale of locales) {
  for (const viewport of viewports) {
    await record(`${locale.id} ${viewport.width}px landing acceptance`, async () => {
      const context = await browser.newContext({ viewport });
      const page = await context.newPage();
      const pageErrors = [];
      const consoleErrors = [];
      const failedRequests = [];
      const requestedUrls = [];

      page.on('pageerror', (error) => pageErrors.push(error.message));
      page.on('console', (message) => {
        if (message.type() === 'error') consoleErrors.push(message.text());
      });
      page.on('request', (request) => requestedUrls.push(request.url()));
      page.on('requestfailed', (request) => failedRequests.push(`${request.method()} ${request.url()}`));

      const response = await page.goto(`${base}/${locale.id}`, { waitUntil: 'networkidle' });
      assert.ok(response, 'landing navigation did not return a response');
      assert.equal(response.status(), 200);
      assert.equal(await page.locator('html').getAttribute('lang'), locale.id);
      assert.equal(await page.locator('html').getAttribute('dir'), locale.dir);

      const bundle = content[locale.id];
      const article = page.locator('main article');
      assert.equal((await article.locator('h1').innerText()).trim(), bundle.home.title);
      assert.equal((await article.locator('.sw-lede').innerText()).trim(), bundle.home.summary);

      const primary = article.getByRole('link', { name: bundle.home.primaryLabel, exact: true });
      const secondary = article.getByRole('link', { name: bundle.home.secondaryLabel, exact: true });
      assert.equal(await primary.getAttribute('href'), `/${locale.id}/start`);
      assert.equal(await secondary.getAttribute('href'), `/${locale.id}/how-it-works`);

      for (const [path, label] of [
        ['protection-and-limits', bundle.common.nav.limits],
        ['privacy', bundle.common.nav.privacy],
        ['help', bundle.common.nav.help],
      ]) {
        const link = page.locator('header').getByRole('link', { name: label, exact: true });
        assert.equal(await link.getAttribute('href'), `/${locale.id}/${path}`);
      }

      for (const action of [primary, secondary]) {
        const box = await action.boundingBox();
        assert.ok(box, 'CTA has no rendered box');
        assert.ok(box.width >= 24 && box.height >= 24, `CTA target is ${box.width}x${box.height}, below WCAG AA minimum`);
      }

      const overflow = await page.evaluate(
        () => document.documentElement.scrollWidth - document.documentElement.clientWidth,
      );
      assert.ok(overflow <= 1, `horizontal overflow ${overflow}px at ${viewport.width}px`);

      if (viewport.width === 320) {
        await page.evaluate(() => {
          document.documentElement.style.fontSize = '200%';
        });
        const zoomOverflow = await page.evaluate(
          () => document.documentElement.scrollWidth - document.documentElement.clientWidth,
        );
        assert.ok(zoomOverflow <= 1, `200% text resize causes ${zoomOverflow}px horizontal overflow`);

        await page.addScriptTag({ content: axeSource });
        const axeResult = await page.evaluate(
          async () =>
            await window.axe.run(document, {
              runOnly: { type: 'tag', values: ['wcag2a', 'wcag2aa', 'wcag21aa', 'wcag22aa'] },
            }),
        );
        assert.deepEqual(
          axeResult.violations.map((violation) => ({
            id: violation.id,
            impact: violation.impact,
            nodes: violation.nodes.length,
          })),
          [],
        );
      }

      assert.equal(await page.locator('form, input, textarea, select').count(), 0, 'public landing collects user input');
      const storage = await page.evaluate(() => ({
        local: Object.keys(localStorage),
        session: Object.keys(sessionStorage),
      }));
      assert.deepEqual(storage, { local: [], session: [] }, 'landing creates persistent or journey storage before setup');
      assert.deepEqual(await context.cookies(), [], 'landing creates cookies before setup');
      assert.deepEqual(pageErrors, [], 'landing emitted page errors');
      assert.deepEqual(consoleErrors, [], 'landing emitted console errors');
      assert.deepEqual(failedRequests, [], 'landing emitted failed network requests');

      const offOrigin = requestedUrls.filter((url) => {
        const protocol = new URL(url).protocol;
        return (protocol === 'http:' || protocol === 'https:') && new URL(url).origin !== baseOrigin;
      });
      assert.deepEqual(offOrigin, [], 'landing made an off-origin runtime request');

      const timing = await page.evaluate(() => {
        const navigation = performance.getEntriesByType('navigation')[0];
        return navigation
          ? {
              duration: navigation.duration,
              domContentLoaded: navigation.domContentLoadedEventEnd,
              transferSize: navigation.transferSize,
            }
          : null;
      });
      assert.ok(timing, 'navigation performance entry is missing');
      assert.ok(Number.isFinite(timing.duration) && timing.duration >= 0, 'invalid navigation duration');
      assert.ok(
        Number.isFinite(timing.domContentLoaded) && timing.domContentLoaded >= 0,
        'invalid DOMContentLoaded timing',
      );
      assert.ok(Number.isFinite(timing.transferSize) && timing.transferSize >= 0, 'invalid navigation transfer size');
      performanceObservations.push({ locale: locale.id, width: viewport.width, ...timing });

      await context.close();
    });
  }
}

await record('unsupported locale fails closed', async () => {
  const context = await browser.newContext({ viewport: { width: 390, height: 844 } });
  const page = await context.newPage();
  const response = await page.goto(`${base}/fr`, { waitUntil: 'domcontentloaded' });
  assert.ok(response);
  assert.equal(response.status(), 404);
  assert.equal(await page.locator('main article').count(), 0, 'unsupported locale rendered the SafeWeb landing');
  await context.close();
});

await browser.close();

for (const observation of performanceObservations) {
  console.log(
    `TSK0395_PERF locale=${observation.locale} width=${observation.width} duration_ms=${observation.duration.toFixed(1)} dom_content_loaded_ms=${observation.domContentLoaded.toFixed(1)} transfer_bytes=${observation.transferSize}`,
  );
}

if (failures.length) {
  console.error(`TSK0395_BROWSER_FAILURES=${failures.length}`);
  for (const failure of failures) console.error(`---\n${failure}`);
  process.exit(1);
}

console.log('TSK0395_BROWSER_ACCEPTANCE=PASS');
