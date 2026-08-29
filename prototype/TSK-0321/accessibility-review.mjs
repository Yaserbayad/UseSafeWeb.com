import { chromium } from 'playwright';

const BASE = 'http://127.0.0.1:4176/prototype/TSK-0310/';
const results = [];
const findings = [];
const externalRequests = [];
const consoleErrors = [];
const pageErrors = [];

function record(id, pass, detail = '', severity = 'acceptance') {
  results.push({ id, pass, detail, severity });
  console.log(`A11Y ${id}=${pass ? 'PASS' : 'FAIL'}${detail ? ` | ${detail}` : ''}`);
}
function note(id, severity, detail, remediation) {
  findings.push({ id, severity, detail, remediation });
  console.log(`FINDING ${id}|${severity}|${detail}|REMEDIATION=${remediation}`);
}
function rgb(value) {
  const m = value.match(/rgba?\((\d+)[, ]+(\d+)[, ]+(\d+)/);
  if (!m) throw new Error(`Unsupported color ${value}`);
  return [Number(m[1]), Number(m[2]), Number(m[3])];
}
function luminance([r,g,b]) {
  const c=[r,g,b].map(v=>{v/=255;return v<=0.04045?v/12.92:((v+0.055)/1.055)**2.4});
  return 0.2126*c[0]+0.7152*c[1]+0.0722*c[2];
}
function contrast(a,b) {
  const [l1,l2]=[luminance(rgb(a)),luminance(rgb(b))].sort((x,y)=>y-x);
  return (l1+0.05)/(l2+0.05);
}
async function visibleControls(page) {
  return page.locator('button:visible,a[href]:visible');
}
async function auditScreen(page, expected, label) {
  const root=page.locator(`[data-screen="${expected}"]`);
  await root.waitFor({state:'visible'});
  record(`${label}:screen`, await root.count()===1, expected);
  record(`${label}:one-h1`, await root.locator('h1').count()===1);
  record(`${label}:focused-h1`, await page.evaluate(()=>document.activeElement?.tagName==='H1'));
  const headings=await root.locator('h1,h2,h3,h4,h5,h6').evaluateAll(nodes=>nodes.map(n=>Number(n.tagName.slice(1))));
  record(`${label}:heading-starts-h1`, headings[0]===1, headings.join(','));
  record(`${label}:no-positive-tabindex`, await root.locator('[tabindex]:not([tabindex="-1"]):not([tabindex="0"])').count()===0);
  record(`${label}:button-type`, await root.locator('button:not([type="button"])').count()===0);
  const overflow=await page.evaluate(()=>document.documentElement.scrollWidth-window.innerWidth);
  record(`${label}:no-page-overflow`, overflow<=1, String(overflow));
  const controls=await visibleControls(page);
  const count=await controls.count();
  for(let i=0;i<count;i++){
    const c=controls.nth(i);
    const name=(await c.innerText()).trim() || (await c.getAttribute('aria-label')) || '';
    record(`${label}:control-${i+1}-name`, name.length>0, name);
    const box=await c.boundingBox();
    if((await c.evaluate(el=>el.tagName))==='BUTTON') record(`${label}:control-${i+1}-target`, !!box && box.width>=24 && box.height>=24, box?`${box.width.toFixed(1)}x${box.height.toFixed(1)}`:'none');
    await c.focus();
    const f=await c.evaluate(el=>{const s=getComputedStyle(el);return {style:s.outlineStyle,width:parseFloat(s.outlineWidth)||0,color:s.outlineColor,bg:s.backgroundColor}});
    record(`${label}:control-${i+1}-focus-visible`, f.style!=='none' && f.width>=1, `${f.style}/${f.width}`);
  }
  if(await root.locator('[data-evidence-state]').count()){
    for(const card of await root.locator('[data-evidence-state]').all()){
      const state=await card.getAttribute('data-evidence-state');
      const labelText=(await card.locator('.sw-status__label').innerText()).trim();
      const evidence=(await card.locator('.sw-status__evidence').innerText()).trim();
      record(`${label}:state-${state}-textual`, labelText.length>0 && evidence.length>0, `${labelText}|${evidence}`);
    }
  }
  await root.locator('h1').focus();
}
async function action(page, selector, expected, label) {
  const c=page.locator(selector);
  await c.focus();
  await page.keyboard.press('Enter');
  await auditScreen(page,expected,label);
}
async function reset(page,label='reset') {
  await action(page,'[data-global-action="RESET"]','discovery',label);
}
async function textResizeCheck(page,label) {
  await page.evaluate(()=>{document.documentElement.style.fontSize='200%'});
  const v=await page.evaluate(()=>({overflow:document.documentElement.scrollWidth-window.innerWidth, clipped:[...document.querySelectorAll('h1,h2,p,li,button,code')].filter(el=>{const s=getComputedStyle(el);return s.overflow==='hidden' && (el.scrollWidth>el.clientWidth+1 || el.scrollHeight>el.clientHeight+1)}).length}));
  record(`${label}:200pct-no-overflow`,v.overflow<=1,String(v.overflow));
  record(`${label}:200pct-no-clipped-critical-text`,v.clipped===0,String(v.clipped));
  await page.evaluate(()=>{document.documentElement.style.fontSize='' });
}
async function rtlTechnicalCheck(page,label) {
  await page.evaluate(()=>{document.documentElement.dir='rtl';document.documentElement.lang='ar'});
  const code=page.locator('.prototype-code');
  if(await code.count()){
    const v=await code.evaluate(el=>{const s=getComputedStyle(el);return {direction:s.direction,bidi:s.unicodeBidi,overflow:document.documentElement.scrollWidth-window.innerWidth}});
    const pass=v.direction==='ltr' && ['isolate','isolate-override'].includes(v.bidi) && v.overflow<=1;
    record(`${label}:technical-value-ltr-isolated`,pass,`${v.direction}/${v.bidi}/overflow=${v.overflow}`,'design-conformance');
    if(!pass) note('A11Y-RTL-TECH-001','prototype-deviation','TSK-0310 technical value inherits RTL when the older internal prototype is mechanically mirrored.','Current approved TSK-0308 DS-13/TSK-0324 already requires technical values to be LTR-isolated; L6 implementation must consume that rule and verify it.');
  }
  await page.evaluate(()=>{document.documentElement.removeAttribute('dir');document.documentElement.lang='en'});
}

let browser;
try {
  browser=await chromium.launch({headless:true,channel:'chromium'});
  console.log(`BROWSER_VERSION=${browser.version()}`);
  const context=await browser.newContext({viewport:{width:320,height:800}});
  await context.route('**/*',async route=>{
    const u=new URL(route.request().url());
    if(['127.0.0.1','localhost'].includes(u.hostname)) return route.continue();
    externalRequests.push(route.request().url()); return route.abort('blockedbyclient');
  });
  const page=await context.newPage();
  page.on('console',m=>{if(m.type()==='error')consoleErrors.push(m.text())});
  page.on('pageerror',e=>pageErrors.push(String(e)));
  await page.goto(BASE,{waitUntil:'networkidle'});

  // Static semantics and current token contrast.
  record('document:lang-en',await page.locator('html').getAttribute('lang')==='en');
  record('document:main-landmark',await page.locator('main#app').count()===1);
  record('document:logo-alt',await page.locator('img[alt="SafeWeb"]').count()===1);
  record('document:no-data-entry-controls',await page.locator('form,input,textarea,select').count()===0);
  record('document:no-positive-tabindex',await page.locator('[tabindex]:not([tabindex="-1"]):not([tabindex="0"])').count()===0);
  const pairs=await page.evaluate(()=>{
    const get=s=>getComputedStyle(document.querySelector(s));
    return {
      body:[get('body').color,get('body').backgroundColor],
      heading:[get('h1').color,get('body').backgroundColor],
      kicker:[get('.sw-kicker').color,get('body').backgroundColor],
      primary:[get('.sw-button').color,get('.sw-button').backgroundColor],
      focus:[getComputedStyle(document.documentElement).getPropertyValue('--sw-color-focus').trim(),get('body').backgroundColor]
    };
  });
  for(const [name,[fg,bg]] of Object.entries(pairs)){
    const ratio=contrast(fg.startsWith('#')?await page.evaluate(c=>{const e=document.createElement('span');e.style.color=c;document.body.appendChild(e);const r=getComputedStyle(e).color;e.remove();return r},fg):fg,bg);
    const threshold=name==='focus'?3:4.5;
    record(`contrast:${name}`,ratio>=threshold,ratio.toFixed(2));
  }

  await auditScreen(page,'discovery','discovery');
  await textResizeCheck(page,'discovery');
  await action(page,'[data-global-action="OPEN_HELP"]','troubleshooting','help-global');
  await action(page,'[data-action="RETURN"]','discovery','help-return');
  await action(page,'[data-action="START"]','router','router');
  await textResizeCheck(page,'router');
  await action(page,'[data-platform="android"]','native','android-native');
  await action(page,'[data-action="NATIVE_CONFIRMED"]','dns','android-dns');
  await rtlTechnicalCheck(page,'android-dns');
  await textResizeCheck(page,'android-dns');
  await action(page,'[data-action="DNS_CONFIGURED"]','verify','verify');
  record('verify:fieldset-legend',await page.locator('fieldset legend').count()===1,(await page.locator('fieldset legend').innerText()).trim());
  await action(page,'[data-result="verified"]','service','service');
  await action(page,'[data-action="SERVICE_NONE"]','map','map-verified');
  record('states:verified-visible',(await page.locator('body').innerText()).includes('Verified'));
  record('states:parent-confirmed-visible',(await page.locator('body').innerText()).includes('You confirmed this is set up'));
  record('states:not-covered-visible',(await page.locator('body').innerText()).includes('Not covered'));
  await textResizeCheck(page,'map');
  await action(page,'[data-action="REMOVE_DNS"]','removal','removal');
  await action(page,'[data-action="CONFIRM_REMOVED"]','recovery','recovery');
  await action(page,'[data-action="RECOVERY_OK"]','map','map-removed');
  record('states:removed-visible',(await page.locator('body').innerText()).includes('Removed'));

  await reset(page,'negative-reset');
  await action(page,'[data-action="START"]','router','negative-router');
  await action(page,'[data-platform="android"]','native','negative-native');
  await action(page,'[data-action="NATIVE_ACTION_NEEDED"]','dns','negative-dns');
  await action(page,'[data-action="DNS_CONFIGURED"]','verify','negative-verify');
  await action(page,'[data-result="action-needed"]','troubleshooting','action-needed');
  record('states:action-needed-visible',(await page.locator('h1').innerText()).trim()==='Action needed');
  await action(page,'[data-action="RETRY_AFTER_CHANGE"]','verify','uncertain-retry-source');
  await action(page,'[data-result="uncertain"]','troubleshooting','uncertain');
  record('states:uncertain-visible',(await page.locator('h1').innerText()).trim()==='Status uncertain');
  await action(page,'[data-action="RETRY_AFTER_CHANGE"]','verify','not-covered-retry-source');
  await action(page,'[data-result="not-covered"]','limitations','not-covered');
  await textResizeCheck(page,'limitations');

  // iPhone exact technical-value RTL stress.
  await reset(page,'iphone-reset');
  await action(page,'[data-action="START"]','router','iphone-router');
  await action(page,'[data-platform="iphone"]','native','iphone-native');
  await action(page,'[data-action="NATIVE_CONFIRMED"]','dns','iphone-dns');
  await rtlTechnicalCheck(page,'iphone-dns');

  // Viewport/reflow matrix on representative discovery state.
  await reset(page,'viewport-reset');
  for(const width of [320,768,1024,1440]){
    await page.setViewportSize({width,height:900});
    const v=await page.evaluate(()=>({overflow:document.documentElement.scrollWidth-window.innerWidth,frame:document.querySelector('.prototype-frame').getBoundingClientRect().width}));
    record(`viewport:${width}:no-overflow`,v.overflow<=1,String(v.overflow));
    if(width>=768) record(`viewport:${width}:bounded-frame`,v.frame<=514,String(v.frame));
  }

  await page.setViewportSize({width:320,height:800});
  await page.emulateMedia({reducedMotion:'reduce'});
  const motion=await page.evaluate(()=>[...document.querySelectorAll('*')].filter(el=>{const s=getComputedStyle(el);return s.animationName!=='none' || (parseFloat(s.transitionDuration)||0)>0}).length);
  record('motion:reduced-no-authored-motion',motion===0,String(motion));

  const mainLive=await page.locator('main#app').getAttribute('aria-live');
  if(mainLive==='polite') note('A11Y-LIVE-001','noncritical-review-note','The entire dynamic main region is aria-live=polite while screen changes also focus h1, which may cause duplicate announcements in some assistive technologies.','Keep h1 focus behavior; in production scope live announcements to asynchronous feedback/status regions unless manual screen-reader review proves the broad live region beneficial.');
  if(await page.locator('a[href^="#main"],a[href="#app"]').count()===0) note('A11Y-SKIP-001','noncritical-production-note','The internal prototype has no visible skip link.','Production repeated-navigation shells should provide a keyboard bypass/skip mechanism; the current main target already exists as #app.');

  record('privacy:no-external-requests',externalRequests.length===0,externalRequests.join(','));
  record('runtime:no-console-errors',consoleErrors.length===0,consoleErrors.join(' | '));
  record('runtime:no-page-errors',pageErrors.length===0,pageErrors.join(' | '));

  const failures=results.filter(r=>!r.pass);
  const acceptanceFailures=failures.filter(r=>r.severity==='acceptance');
  console.log(`A11Y_CHECKS=${results.length}`);
  console.log(`A11Y_FAILURES=${failures.length}`);
  console.log(`A11Y_ACCEPTANCE_FAILURES=${acceptanceFailures.length}`);
  console.log(`A11Y_FINDINGS=${findings.length}`);
  console.log(`A11Y_REPORT_JSON=${JSON.stringify({checks:results.length,failures:failures.map(x=>x.id),acceptanceFailures:acceptanceFailures.map(x=>x.id),findings})}`);
  console.log('TSK0321_AUTOMATED_REVIEW=COMPLETE');
  await context.close(); await browser.close(); browser=undefined;
  if(acceptanceFailures.length) process.exitCode=2;
} catch(error){
  console.error(`TSK0321_AUTOMATED_REVIEW=ERROR\n${error?.stack||error}`);
  if(browser) await browser.close().catch(()=>{});
  process.exitCode=1;
}
