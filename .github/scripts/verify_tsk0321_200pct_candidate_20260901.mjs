import { createRequire } from 'module';
const require = createRequire(import.meta.url);
const { chromium } = require(process.env.TSK0321_PLAYWRIGHT_MODULE || 'playwright');
const base = process.env.TSK0321_BASE_URL || 'http://127.0.0.1:8033/prototype/TSK-0333/index.html';
const browser = await chromium.launch({ headless: true });
const page = await browser.newPage({ viewport: { width: 320, height: 900 } });
await page.goto(base, { waitUntil: 'networkidle' });
await page.evaluate(() => { document.documentElement.style.fontSize = '200%'; });
const result = await page.evaluate(() => ({
  viewport: document.documentElement.clientWidth,
  documentScrollWidth: document.documentElement.scrollWidth,
  bodyScrollWidth: document.body.scrollWidth,
  actionWidths: [...document.querySelectorAll('.prototype-actions .sw-button')].map(el => ({ text: el.textContent.trim(), width: el.getBoundingClientRect().width, right: el.getBoundingClientRect().right }))
}));
if (result.documentScrollWidth > result.viewport + 1 || result.bodyScrollWidth > result.viewport + 1) {
  throw new Error(`200pct-overflow:${JSON.stringify(result)}`);
}
for (const action of result.actionWidths) {
  if (action.right > result.viewport + 1 || action.width > result.viewport + 1) throw new Error(`action-overflow:${JSON.stringify(action)}`);
}
console.log(`TSK0321_200PCT_VIEWPORT=${result.viewport}`);
console.log(`TSK0321_200PCT_SCROLLWIDTH=${result.documentScrollWidth}`);
console.log('TSK0321_200PCT_REMEDIATION=PASS');
await browser.close();
