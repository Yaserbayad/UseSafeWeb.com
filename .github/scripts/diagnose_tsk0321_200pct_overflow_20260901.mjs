import { createRequire } from 'module';
const require = createRequire(import.meta.url);
const { chromium } = require(process.env.TSK0321_PLAYWRIGHT_MODULE || 'playwright');
const base = process.env.TSK0321_BASE_URL || 'http://127.0.0.1:8033/prototype/TSK-0333/index.html';
const browser = await chromium.launch({ headless: true });
const page = await browser.newPage({ viewport: { width: 320, height: 900 } });
await page.goto(base, { waitUntil: 'networkidle' });
await page.evaluate(() => { document.documentElement.style.fontSize = '200%'; });
const result = await page.evaluate(() => {
  const vw = document.documentElement.clientWidth;
  const rows = [...document.querySelectorAll('html,body,body *')].map((el) => {
    const r = el.getBoundingClientRect();
    const s = getComputedStyle(el);
    return {
      tag: el.tagName,
      id: el.id || '',
      cls: typeof el.className === 'string' ? el.className : '',
      text: (el.textContent || '').trim().replace(/\s+/g, ' ').slice(0, 80),
      left: Math.round(r.left * 10) / 10,
      right: Math.round(r.right * 10) / 10,
      width: Math.round(r.width * 10) / 10,
      clientWidth: el.clientWidth,
      scrollWidth: el.scrollWidth,
      minWidth: s.minWidth,
      maxWidth: s.maxWidth,
      whiteSpace: s.whiteSpace,
      overflowWrap: s.overflowWrap,
      display: s.display,
      flexWrap: s.flexWrap,
      flexShrink: s.flexShrink,
      paddingInline: `${s.paddingInlineStart} ${s.paddingInlineEnd}`
    };
  });
  const offenders = rows.filter(x => x.right > vw + 1 || x.left < -1 || x.scrollWidth > x.clientWidth + 1);
  return {
    viewport: vw,
    documentScrollWidth: document.documentElement.scrollWidth,
    bodyScrollWidth: document.body.scrollWidth,
    offenders: offenders.slice(0, 40),
    key: rows.filter(x => ['prototype-frame','prototype-topbar','prototype-topbar__tools','prototype-main','prototype-screen','prototype-actions','prototype-footer'].some(c => x.cls.split(/\s+/).includes(c)))
  };
});
console.log(JSON.stringify(result, null, 2));
if (result.documentScrollWidth <= result.viewport + 1) throw new Error('Diagnostic did not reproduce overflow');
console.log('TSK0321_200PCT_OVERFLOW_REPRODUCED=PASS');
await browser.close();
