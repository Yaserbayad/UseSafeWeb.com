import { createRequire } from 'module';

const require = createRequire(import.meta.url);
const playwrightModule = process.env.TSK0333_PLAYWRIGHT_MODULE || 'playwright';
const { chromium } = require(playwrightModule);
const base = process.env.TSK0333_BASE_URL || 'http://127.0.0.1:8033/prototype/TSK-0333/index.html';
const browser = await chromium.launch({headless:true});
const page = await browser.newPage({viewport:{width:320,height:900}});
const errors=[];
const external=[];
page.on('console',m=>{ if(m.type()==='error') errors.push(`console:${m.text()}`); });
page.on('pageerror',e=>errors.push(`page:${e.message}`));
page.on('request',r=>{ const u=new URL(r.url()); if(!['127.0.0.1','localhost'].includes(u.hostname)) external.push(r.url()); });
function req(c,m){ if(!c) throw new Error(m); }
const testid=(id)=>page.getByTestId(id);
const action=(name)=>page.locator(`[data-action="${name}"]`).first();
const globalAction=(name)=>page.locator(`[data-global-action="${name}"]`).first();
async function clickAction(name){ await action(name).click(); }
async function reset(){ await globalAction('RESET').click(); await testid('screen-home').waitFor(); }
async function startAndroidToMap(){
  await reset(); await clickAction('START');
  await page.locator('[data-action="CHOOSE_PLATFORM"][data-platform="android"]').click();
  await clickAction('NATIVE_CONFIRMED'); await clickAction('DNS_CONFIGURED');
  await page.locator('[data-action="VERIFY_RESULT"][data-result="verified"]').click();
  await clickAction('SERVICE_NONE'); await testid('screen-map').waitFor();
}
async function signInReturning(){
  await reset(); await clickAction('OPEN_ACCOUNT_ENTRY');
  await page.locator('[data-action="START_GOOGLE_SIGNIN"][data-mode="returning"]').click();
  await clickAction('PROVIDER_SUCCESS_RETURNING'); await testid('screen-dashboard').waitFor();
}

await page.goto(base,{waitUntil:'networkidle'});
req(await testid('screen-home').isVisible(),'home-visible');
req(await page.getByRole('button',{name:'Start setup'}).first().isVisible(),'accountless-start-visible');
req(await page.getByRole('button',{name:/Sign in/}).first().isVisible(),'optional-signin-visible');
let s=await page.evaluate(()=>window.__TSK0333_TEST__.getState());
req(s.authStatus==='signed-out','initial-signed-out');

// Keyboard / skip-link from true default load.
await page.keyboard.press('Tab');
req(await page.locator('#skip-link').evaluate(el=>el===document.activeElement),'skip-link-first-focus');
await page.keyboard.press('Enter');
req(await page.locator('#main-content').evaluate(el=>el===document.activeElement),'skip-link-target-main');
console.log('TSK0333_BROWSER_KEYBOARD=PASS');

// A. Accountless Android normal path.
await startAndroidToMap();
req((await testid('map-phone').getAttribute('data-evidence-state'))==='parent-confirmed','android-phone-parent-confirmed');
req((await testid('map-internet').getAttribute('data-evidence-state'))==='verified','android-internet-verified');
req((await testid('map-service').getAttribute('data-evidence-state'))==='not-covered','android-service-not-covered');
req(await testid('map-no-score').isVisible(),'map-no-score');
s=await page.evaluate(()=>window.__TSK0333_TEST__.getState());
req(s.authStatus==='signed-out','accountless-map-still-signed-out');
console.log('TSK0333_BROWSER_ACCOUNTLESS_ANDROID=PASS');

// D. False-positive support does not rewrite technical state.
const beforeFalsePositive=s.dnsState;
await clickAction('OPEN_FALSE_POSITIVE');
req(await testid('screen-false-positive').isVisible(),'false-positive-screen');
await clickAction('RETURN');
s=await page.evaluate(()=>window.__TSK0333_TEST__.getState());
req(s.dnsState===beforeFalsePositive,'false-positive-state-mutation');
console.log('TSK0333_BROWSER_FALSE_POSITIVE_TRUTH=PASS');

// E. Physical removal, neutral recovery, reconfigure.
await clickAction('REMOVE_DNS'); await clickAction('CONFIRM_REMOVED');
s=await page.evaluate(()=>window.__TSK0333_TEST__.getState());
req(s.dnsState==='removed' && s.dnsConfigured===false,'physical-removal-state');
await clickAction('RECOVERY_OK');
s=await page.evaluate(()=>window.__TSK0333_TEST__.getState());
req(s.dnsState==='removed','neutral-recovery-cannot-restore-verified');
await clickAction('RECONFIGURE');
s=await page.evaluate(()=>window.__TSK0333_TEST__.getState());
req(s.dnsState==='action-needed' && s.screen==='dns','reconfigure-fresh-state');
console.log('TSK0333_BROWSER_REMOVAL_RECOVERY=PASS');

// B. iPhone exact DoH endpoint.
await reset(); await clickAction('START');
await page.locator('[data-action="CHOOSE_PLATFORM"][data-platform="iphone"]').click();
await clickAction('NATIVE_CONFIRMED');
req((await testid('iphone-doh-value').textContent()).trim()==='https://dns.usesafeweb.com/dns-query','iphone-doh-endpoint');
console.log('TSK0333_BROWSER_IPHONE=PASS');

// C. Unsupported path truthfully stops.
await reset(); await clickAction('START');
await page.locator('[data-action="CHOOSE_PLATFORM"][data-platform="other"]').click();
req(await testid('screen-limits').isVisible(),'unsupported-limits');
s=await page.evaluate(()=>window.__TSK0333_TEST__.getState());
req(s.dnsState==='not-covered','unsupported-not-covered');
console.log('TSK0333_BROWSER_UNSUPPORTED=PASS');

// F. First account creation is explicit and creates no device automatically.
await reset(); await clickAction('OPEN_ACCOUNT_ENTRY');
await page.locator('[data-action="START_GOOGLE_SIGNIN"][data-mode="new"]').click();
await clickAction('PROVIDER_SUCCESS_NEW');
req(await testid('screen-first-session').isVisible(),'first-session');
await clickAction('CREATE_ACCOUNT');
req(await testid('screen-dashboard').isVisible(),'new-account-dashboard');
req(await testid('dashboard-empty').isVisible(),'new-account-no-device');
s=await page.evaluate(()=>window.__TSK0333_TEST__.getState());
req(s.accountExists===true && s.device.exists===false,'new-account-no-auto-device');
console.log('TSK0333_BROWSER_NEW_ACCOUNT=PASS');

// Explicit device saving requires the setup path and never makes record presence evidence.
await clickAction('ADD_DEVICE');
await page.locator('[data-action="CHOOSE_PLATFORM"][data-platform="android"]').click();
await clickAction('NATIVE_CONFIRMED'); await clickAction('DNS_CONFIGURED');
await page.locator('[data-action="VERIFY_RESULT"][data-result="verified"]').click(); await clickAction('SERVICE_NONE');
await clickAction('SAVE_DEVICE_EXPLICIT');
req(await testid('screen-device-detail').isVisible(),'explicit-save-device-detail');
s=await page.evaluate(()=>window.__TSK0333_TEST__.getState());
req(s.device.exists===true && s.dnsState==='verified','explicit-save-preserves-owned-current-evidence');
console.log('TSK0333_BROWSER_EXPLICIT_DEVICE_SAVE=PASS');

// G. Returning account fixture: stored record is explicitly not current proof.
await signInReturning();
req(await testid('device-card').isVisible(),'returning-device-card');
req(await page.getByText('Saved record presence is not technical verification.').isVisible(),'saved-record-not-verification');
await clickAction('OPEN_DEVICE');
req(await page.getByText('Account ownership and saved-record presence do not establish current protection.').isVisible(),'device-detail-not-verification');
console.log('TSK0333_BROWSER_RETURNING_DASHBOARD=PASS');

// K/O. Replacement starts fresh; revoke/delete-record are narrow account-side lifecycles.
await clickAction('OPEN_MANAGE');
for(const name of ['REVERIFY_DEVICE','REINSTALL_DEVICE','REPLACE_DEVICE','REVOKE_DEVICE','DELETE_DEVICE_RECORD']) req(await action(name).isVisible(),`manage-action-${name}`);
await clickAction('REPLACE_DEVICE');
req(await testid('screen-lifecycle-confirm').isVisible(),'replace-confirm');
await clickAction('CONFIRM_LIFECYCLE');
s=await page.evaluate(()=>window.__TSK0333_TEST__.getState());
req(s.device.nickname==='Replacement phone' && s.dnsState==='action-needed' && s.lastVerification===null,'replacement-fresh-unverified');
console.log('TSK0333_BROWSER_DEVICE_REPLACEMENT=PASS');

// L/N. Unknown destructive result blocks replay; record deletion never sets physical Removed.
await clickAction('OPEN_MANAGE'); await clickAction('DELETE_DEVICE_RECORD'); await clickAction('SIMULATE_LIFECYCLE_UNKNOWN');
req(await testid('screen-lifecycle-unknown').isVisible(),'unknown-result-screen');
req(!(await action('CONFIRM_LIFECYCLE').isVisible().catch(()=>false)),'unknown-result-no-repeat-confirm');
await page.locator('[data-action="RESOLVE_UNKNOWN"][data-result="applied"]').click();
s=await page.evaluate(()=>window.__TSK0333_TEST__.getState());
req(s.device.exists===false && s.dnsState!=='removed','record-delete-not-physical-removed');
console.log('TSK0333_BROWSER_UNKNOWN_AND_RECORD_DELETE=PASS');

// H. Provider error is account-only and core remains available.
await reset(); await clickAction('OPEN_ACCOUNT_ENTRY'); await page.locator('[data-action="START_GOOGLE_SIGNIN"][data-mode="returning"]').click(); await clickAction('PROVIDER_ERROR');
req(await testid('screen-account-error').isVisible(),'provider-error');
req(await page.getByRole('button',{name:'Start setup'}).isVisible(),'provider-error-core-fallback');
s=await page.evaluate(()=>window.__TSK0333_TEST__.getState());
req(s.dnsState==='action-needed','provider-error-no-protection-rewrite');
console.log('TSK0333_BROWSER_PROVIDER_ERROR=PASS');

// I/J/M. Session expiry/reauth/logout/account deletion remain lifecycle-distinct.
await signInReturning();
await page.evaluate(()=>window.__TSK0333_TEST__.dispatch('EXPIRE_SESSION'));
await testid('screen-reauth').waitFor();
req(await page.getByText('Session expiry does not change physical protection.').isVisible(),'session-expiry-copy');
req(await page.getByRole('button',{name:'Start setup without account'}).isVisible(),'reauth-core-fallback');
await clickAction('REAUTHENTICATE');
req(await testid('screen-account').isVisible(),'reauth-account');
await clickAction('OPEN_DELETE_ACCOUNT');
req(await page.getByText(/does not claim physical UseSafeWeb removal/i).isVisible(),'account-delete-physical-separation');
req(await page.getByText(/does not delete unrelated anonymous J0\/J1 state/i).isVisible(),'account-delete-j0j1-separation');
await clickAction('OPEN_ACCOUNT');
await clickAction('LOGOUT'); await clickAction('CONFIRM_LOGOUT');
s=await page.evaluate(()=>window.__TSK0333_TEST__.getState());
req(s.authStatus==='signed-out','logout-signed-out');
req(s.device.exists===true,'logout-does-not-delete-device-record');
console.log('TSK0333_BROWSER_SESSION_LOGOUT_DELETE_BOUNDARY=PASS');

// RTL and responsive behavior.
await reset(); await globalAction('TOGGLE_RTL').click();
req(await page.locator('html').getAttribute('dir')==='rtl','rtl-dir');
req(await page.locator('html').getAttribute('lang')==='ar','rtl-lang');
for (const width of [320,768,1024,1440]) {
  await page.setViewportSize({width,height:900});
  const over=await page.evaluate(()=>document.documentElement.scrollWidth > document.documentElement.clientWidth);
  req(!over,`horizontal-overflow-${width}`);
}
console.log('TSK0333_BROWSER_RTL_RESPONSIVE=PASS');

// Privacy / no transport or browser persistence.
await reset(); await clickAction('OPEN_DATA_USE');
const body=(await page.locator('body').innerText()).toLowerCase();
for(const phrase of ['no browsing history','no activity history','no raw dns','no child profile','no broad dns administration']) req(body.includes(phrase),`privacy-copy-${phrase}`);
const persisted=await page.evaluate(async()=>({cookies:document.cookie,ls:Object.keys(window.localStorage),ss:Object.keys(window.sessionStorage),idb:await indexedDB.databases()}));
req(persisted.cookies==='' && persisted.ls.length===0 && persisted.ss.length===0 && persisted.idb.length===0,'browser-persistence-created');
req(external.length===0,`external-requests:${external.join(',')}`);
req(errors.length===0,errors.join(';'));
console.log('TSK0333_BROWSER_PRIVACY_NO_TRANSPORT=PASS');
console.log('TSK0333_BROWSER_NO_CONSOLE_ERRORS=PASS');
console.log('TSK0333_POST_CR0007_BROWSER_VERIFICATION=PASS');
await browser.close();
