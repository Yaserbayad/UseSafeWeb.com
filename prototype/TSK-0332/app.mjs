const view = document.querySelector('#state-view');
const title = document.querySelector('#state-title');
const live = document.querySelector('#live-status');

const copy = {
  en: { page: 'Your devices', add: 'Add device' },
  tr: { page: 'Cihazlarınız', add: 'Cihaz ekle' },
  ar: { page: 'أجهزتك', add: 'إضافة جهاز' },
};

const params = new URLSearchParams(location.search);
const lang = ['en','tr','ar'].includes(params.get('lang')) ? params.get('lang') : 'en';
document.documentElement.lang = lang;
document.documentElement.dir = lang === 'ar' ? 'rtl' : 'ltr';

function button(label, state, cls='') {
  return `<button class="${cls}" data-state="${state}">${label}</button>`;
}
function status(label, tone='') { return `<span class="status ${tone}">${label}</span>`; }
function mapRows(states) {
  return `<div class="map" aria-label="Protection Map">
    ${states.map(([layer,label,tone]) => `<div class="map-row"><strong>${layer}</strong>${status(label,tone)}</div>`).join('')}
  </div>`;
}
function manage() {
  return `<aside class="card" aria-labelledby="manage-title"><h2 id="manage-title">Manage</h2><div class="manage-list">
    ${button('Rename device','device-protected')}
    ${button('Continue setup','continue-setup')}
    ${button('Check again','verify')}
    ${button('Reinstall or reconfigure','reconfigure')}
    ${button('Replace device','replace')}
    ${button('Unlink from dashboard','unlink')}
    ${button('Remove UseSafeWeb protection','remove-protection')}
    ${button('Remove from dashboard','remove-record','danger')}
    ${button('Help','help')}
  </div></aside>`;
}

const states = {
  empty: () => `<section class="card empty"><h2>No saved devices yet</h2><p class="muted">Add a device only if you want to return to its setup and protection status later. You can still use UseSafeWeb without saving a device.</p><div class="actions">${button('Add device','add-device','primary')}${button('Start setup without saving','continue-setup')}</div><p><button class="quiet" data-state="help">What does saving a device do?</button></p></section>`,
  'device-protected': () => device('Family iPhone','Protected','', [['Phone','Set up — parent confirmed','neutral'],['Internet','Protected',''],['Services','Set up — parent confirmed','neutral']], 'View Protection Map','device-protected'),
  'device-parent-confirmed': () => device('Family iPhone','Set up — parent confirmed','neutral', [['Phone','Set up — parent confirmed','neutral'],['Internet','Set up — parent confirmed','neutral'],['Services','Set up — parent confirmed','neutral']], 'View Protection Map','device-parent-confirmed'),
  'device-action-needed': () => device('Family iPhone','Needs attention','warning', [['Phone','Set up — parent confirmed','neutral'],['Internet','Needs attention','warning'],['Services','Set up — parent confirmed','neutral']], 'Continue setup','continue-setup'),
  'device-not-covered': () => device('Family iPhone','Not covered','neutral', [['Phone','Set up — parent confirmed','neutral'],['Internet','Not covered','neutral'],['Services','Set up — parent confirmed','neutral']], 'Get help','help'),
  'device-uncertain': () => device('Family iPhone','Status uncertain','warning', [['Phone','Set up — parent confirmed','neutral'],['Internet','Status uncertain','warning'],['Services','Set up — parent confirmed','neutral']], 'Check again','verify'),
  'device-removed': () => device('Family iPhone','Removed','danger', [['Phone','Set up — parent confirmed','neutral'],['Internet','Removed','danger'],['Services','Set up — parent confirmed','neutral']], 'Set up again','continue-setup'),
  'add-device': () => `<section class="stack"><div class="card"><h2>Add a device</h2><p>Choose the device type you want to manage. Saving a device does not mean protection is already set up.</p><div class="choice-grid">${button('<strong>iPhone</strong><br><span class="muted">Supported setup path</span>','continue-setup','choice')}${button('<strong>Android phone</strong><br><span class="muted">Supported setup path</span>','continue-setup','choice')}</div></div><div class="card"><h2>Name</h2><p class="muted">A device nickname is optional. You do not need to enter a child name.</p><label for="nickname">Device nickname</label><input id="nickname" autocomplete="off" maxlength="60" placeholder="Family iPhone"></div></section>`,
  'continue-setup': () => actionPage('Continue setup','Finish the supported setup steps for this device. A saved record does not replace the protection check.','Continue setup','verify'),
  verify: () => actionPage('Check protection','UseSafeWeb will check the supported protection signal needed for this device.','Check now','device-protected'),
  reconfigure: () => actionPage('Reinstall or reconfigure','An earlier protection result may no longer be current while you change setup. Check protection again when you finish.','Continue reconfiguration','verify'),
  replace: () => actionPage('Replace this device','The new device starts with its own setup and protection status. It does not inherit this device’s confirmed state.','Start replacement','add-device'),
  unlink: () => actionPage('Unlink this device from your dashboard?','This ends this account’s management link. It does not remove UseSafeWeb protection from the physical device.','Unlink device','empty',true),
  'remove-protection': () => actionPage('Remove UseSafeWeb protection','Follow the supported steps on the physical device. Removing protection is separate from removing this saved dashboard record.','Show removal steps','device-removed',true),
  'remove-record': () => actionPage('Remove from dashboard?','This removes the saved device record from your account. It does not remove UseSafeWeb protection from the physical device.','Remove from dashboard','empty',true),
  help: () => `<section class="card"><h2>How can we help?</h2><p class="muted">Choose the issue that best matches what you are seeing.</p><div class="manage-list">${['Finish setup','Protection check failed','Status uncertain','Device or network not covered','Reinstall or reconfigure','Site blocked unexpectedly','Remove protection','Account or session problem','Device record problem'].map(x=>`<button>${x}</button>`).join('')}</div><div class="notice"><strong>Privacy-minimal help</strong><p>Routine help asks only for what is needed to diagnose the current setup or status.</p></div></section>`,
  'session-expired': () => `<section class="card"><h2>Sign in again to manage saved devices</h2><p>Your account session ended. This does not mean protection stopped on your devices.</p><div class="actions">${button('Continue with Google','empty','primary')}${button('Start setup without account','continue-setup')}${button('Help','help')}</div></section>`,
  'account-error': () => `<section class="card"><h2>We could not open your saved devices</h2><div class="notice warning"><strong>Account access needs attention</strong><p>Your device protection status has not been changed by this account problem.</p></div><div class="actions">${button('Get help','help','primary')}${button('Start setup without account','continue-setup')}</div></section>`,
};

function device(name, label, tone, map, primaryLabel, primaryState) {
  return `<div class="detail-grid"><section class="card device-card"><div class="device-title"><div><h2>${name}</h2><p class="muted">iPhone</p></div>${status(label,tone)}</div><p class="muted">Saved status is a management reference. Current protection is determined by the evidence shown below.</p><h3>Protection Map</h3>${mapRows(map)}<div class="actions">${button(primaryLabel,primaryState,'primary')}${button('Check again','verify')}${button('Help','help')}</div></section>${manage()}</div>`;
}
function actionPage(heading, body, primaryLabel, successState, destructive=false) {
  return `<section class="card"><h2>${heading}</h2><p>${body}</p>${destructive?'<div class="notice warning"><strong>Check the consequence before continuing.</strong></div>':''}<div class="actions">${button(primaryLabel,successState,destructive?'danger':'primary')}${button('Cancel','device-protected')}${button('Help','help')}</div></section>`;
}

function stateFromHash() {
  const key = location.hash.replace(/^#/,'') || 'empty';
  return states[key] ? key : 'empty';
}
function render({focus=false}={}) {
  const key=stateFromHash();
  title.textContent=copy[lang].page;
  view.innerHTML=states[key]();
  view.dataset.state=key;
  live.textContent=`Dashboard state: ${key.replaceAll('-',' ')}`;
  if (focus) {
    const h2=view.querySelector('h2');
    if (h2) { h2.tabIndex=-1; h2.focus(); }
  }
}

document.addEventListener('click', e => {
  const control=e.target.closest('[data-state]');
  if (!control) return;
  const next=control.dataset.state;
  if (!states[next]) return;
  if (location.hash === `#${next}`) render({focus:true});
  else location.hash=next;
});
window.addEventListener('hashchange',()=>{
  const key=location.hash.replace(/^#/,'');
  if (states[key]) render({focus:true});
});
render();
