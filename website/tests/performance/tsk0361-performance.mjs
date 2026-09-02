import assert from 'node:assert/strict';
import { chromium } from 'playwright';

const base = process.env.BASE_URL ?? 'http://127.0.0.1:3000';
const routes = [
  '/en-GB',
  '/en-GB/start',
  '/en-GB/setup/route',
  '/en-GB/setup/native?platform=android',
  '/en-GB/setup/dns?platform=android',
  '/ar',
];
const samplesPerRoute = 5;

function percentile(values, p) {
  const ordered = [...values].sort((a, b) => a - b);
  const rank = Math.max(0, Math.ceil((p / 100) * ordered.length) - 1);
  return ordered[rank];
}

const browser = await chromium.launch({ headless: true });
const context = await browser.newContext({ viewport: { width: 390, height: 844 } });
const page = await context.newPage();

await page.addInitScript(() => {
  window.__tsk0361Perf = { lcp: 0, cls: 0, events: [] };
  try {
    new PerformanceObserver((list) => {
      for (const entry of list.getEntries()) window.__tsk0361Perf.lcp = Math.max(window.__tsk0361Perf.lcp, entry.startTime || 0);
    }).observe({ type: 'largest-contentful-paint', buffered: true });
  } catch {}
  try {
    new PerformanceObserver((list) => {
      for (const entry of list.getEntries()) {
        if (!entry.hadRecentInput) window.__tsk0361Perf.cls += entry.value || 0;
      }
    }).observe({ type: 'layout-shift', buffered: true });
  } catch {}
  try {
    new PerformanceObserver((list) => {
      for (const entry of list.getEntries()) {
        if (entry.interactionId > 0) window.__tsk0361Perf.events.push(entry.duration || 0);
      }
    }).observe({ type: 'event', buffered: true, durationThreshold: 16 });
  } catch {}
});

const navigationDurations = [];
const lcps = [];
const clss = [];
let successes = 0;

for (const route of routes) {
  for (let i = 0; i < samplesPerRoute; i += 1) {
    const response = await page.goto(`${base}${route}`, { waitUntil: 'networkidle' });
    assert.ok(response, `missing response for ${route}`);
    assert.equal(response.status(), 200, `HTTP ${response.status()} for ${route}`);
    await page.waitForTimeout(100);
    const result = await page.evaluate(() => {
      const nav = performance.getEntriesByType('navigation')[0];
      return {
        navigationDuration: nav?.duration ?? Number.POSITIVE_INFINITY,
        lcp: window.__tsk0361Perf?.lcp ?? Number.POSITIVE_INFINITY,
        cls: window.__tsk0361Perf?.cls ?? Number.POSITIVE_INFINITY,
      };
    });
    assert.ok(Number.isFinite(result.navigationDuration), `invalid navigation duration for ${route}`);
    assert.ok(Number.isFinite(result.lcp), `invalid LCP for ${route}`);
    assert.ok(Number.isFinite(result.cls), `invalid CLS for ${route}`);
    navigationDurations.push(result.navigationDuration);
    lcps.push(result.lcp);
    clss.push(result.cls);
    successes += 1;
  }
}

await page.goto(`${base}/en-GB`, { waitUntil: 'networkidle' });
await page.evaluate(() => {
  const link = document.querySelector('a[href="/en-GB/start"]');
  if (!link) throw new Error('representative Start setup link missing');
  link.addEventListener('click', (event) => event.preventDefault(), { once: true, capture: true });
});
await page.locator('a[href="/en-GB/start"]').first().click();
await page.waitForTimeout(250);
const interactionDurations = await page.evaluate(() => window.__tsk0361Perf?.events ?? []);
const interactionUpperBound = interactionDurations.length ? Math.max(...interactionDurations) : 16;

const navP95 = percentile(navigationDurations, 95);
const navP99 = percentile(navigationDurations, 99);
const maxLcp = Math.max(...lcps);
const maxCls = Math.max(...clss);

assert.equal(successes, routes.length * samplesPerRoute, 'all bounded synthetic requests must succeed');
assert.ok(navP95 <= 1000, `synthetic critical-route navigation p95 ${navP95.toFixed(1)}ms exceeds 1000ms`);
assert.ok(navP99 <= 2000, `synthetic critical-route navigation p99 ${navP99.toFixed(1)}ms exceeds 2000ms`);
assert.ok(maxLcp <= 2500, `synthetic LCP ${maxLcp.toFixed(1)}ms exceeds 2500ms`);
assert.ok(maxCls <= 0.1, `synthetic CLS ${maxCls.toFixed(4)} exceeds 0.1`);
assert.ok(interactionUpperBound <= 200, `synthetic representative interaction duration ${interactionUpperBound.toFixed(1)}ms exceeds 200ms`);

console.log(`TSK0361_PERF_BROWSER=${browser.version()}`);
console.log(`TSK0361_PERF_SAMPLE_COUNT=${successes}`);
console.log(`TSK0361_NAV_P95_MS=${navP95.toFixed(1)}`);
console.log(`TSK0361_NAV_P99_MS=${navP99.toFixed(1)}`);
console.log(`TSK0361_LCP_MAX_MS=${maxLcp.toFixed(1)}`);
console.log(`TSK0361_CLS_MAX=${maxCls.toFixed(4)}`);
console.log(`TSK0361_INTERACTION_EVENT_UPPER_BOUND_MS=${interactionUpperBound.toFixed(1)}`);
console.log('TSK0361_PERF_SCOPE=synthetic-lab-full-page-and-representative-interaction');
console.log('TSK0361_FIELD_P75_CLAIM=NONE');
console.log('TSK0361_OPERATIONAL_99_9_SLO_CLAIM=NONE');
console.log('TSK0361_LOAD_ENVELOPE_1X_2X_CLAIM=NONE_EXPECTED_LIVE_LOAD_UNFROZEN');
console.log('TSK0361_PERFORMANCE_ACCEPTANCE=PASS');

await context.close();
await browser.close();
