import { chromium } from 'playwright';

const base = process.env.TSK0332_BASE_URL || 'http://127.0.0.1:8032/prototype/TSK-0332/index.html';
const browser = await chromium.launch({headless:true});
const page = await browser.newPage({viewport:{width:320,height:800}});
const errors=[];
page.on('console',m=>{ if(m.type()==='error') errors.push(`console:${m.text()}`); });
page.on('pageerror',e=>errors.push(`page:${e.message}`));

function req(cond,msg){ if(!cond) throw new Error(msg); }

await page.goto(`${base}#empty`,{waitUntil:'networkidle'});
req(await page.locator('h1').textContent()==='Your devices','heading');
req((await page.locator('#state-view').getAttribute('data-state'))==='empty','empty-state');
req(await page.getByText('No saved devices yet').isVisible(),'empty-copy');
req(await page.getByRole('button',{name:'Add device'}).first().isVisible(),'add-device');
const overflow = await page.evaluate(()=>document.documentElement.scrollWidth > document.documentElement.clientWidth);
req(!overflow,'320px-horizontal-overflow');

await page.getByRole('button',{name:'Add device'}).first().click();
await page.waitForFunction(()=>document.querySelector('#state-view')?.dataset.state==='add-device');
req(await page.getByText('You do not need to enter a child name.').isVisible(),'minimal-nickname-copy');

await page.goto(`${base}#device-action-needed`,{waitUntil:'networkidle'});
req(await page.getByText('Needs attention').first().isVisible(),'action-needed-copy');
req(await page.getByText('Protection Map').isVisible(),'protection-map');
req(await page.getByRole('button',{name:'Continue setup'}).first().isVisible(),'next-action');

await page.goto(`${base}#device-uncertain`,{waitUntil:'networkidle'});
req(await page.getByText('Status uncertain').first().isVisible(),'uncertain-copy');

await page.goto(`${base}#device-removed`,{waitUntil:'networkidle'});
req(await page.getByText('Removed').first().isVisible(),'removed-copy');
req(await page.getByRole('button',{name:'Remove from dashboard'}).isVisible(),'record-removal-distinct');

await page.goto(`${base}#session-expired`,{waitUntil:'networkidle'});
req(await page.getByText('This does not mean protection stopped on your devices.').isVisible(),'session-vs-protection');
req(await page.getByRole('button',{name:'Start setup without account'}).isVisible(),'accountless-fallback');

await page.goto(`${base}#remove-record`,{waitUntil:'networkidle'});
req(await page.getByText('It does not remove UseSafeWeb protection from the physical device.').isVisible(),'record-vs-physical-removal');

await page.goto(`${base}?lang=ar#empty`,{waitUntil:'networkidle'});
req(await page.locator('html').getAttribute('dir')==='rtl','rtl-dir');
req(await page.locator('html').getAttribute('lang')==='ar','arabic-lang');

await page.goto(`${base}#empty`,{waitUntil:'networkidle'});
await page.keyboard.press('Tab');
req(await page.locator('.skip-link').evaluate(el=>el===document.activeElement),'skip-link-first-focus');
await page.keyboard.press('Enter');
req(await page.locator('#main').evaluate(el=>el===document.activeElement),'skip-link-target');

for (const width of [320,768,1024,1440]) {
  await page.setViewportSize({width,height:900});
  await page.goto(`${base}#device-protected`,{waitUntil:'networkidle'});
  const over=await page.evaluate(()=>document.documentElement.scrollWidth > document.documentElement.clientWidth);
  req(!over,`horizontal-overflow-${width}`);
}

const bodyText=(await page.locator('body').innerText()).toLowerCase();
for(const forbidden of ['top sites','query history','child profile']) req(!bodyText.includes(forbidden),`forbidden-surface-${forbidden}`);
req(errors.length===0,errors.join(';'));

console.log('TSK0332_BROWSER_320=PASS');
console.log('TSK0332_BROWSER_RESPONSIVE=PASS');
console.log('TSK0332_BROWSER_KEYBOARD=PASS');
console.log('TSK0332_BROWSER_RTL=PASS');
console.log('TSK0332_BROWSER_STATE_SEMANTICS=PASS');
console.log('TSK0332_BROWSER_NO_CONSOLE_ERRORS=PASS');
await browser.close();
