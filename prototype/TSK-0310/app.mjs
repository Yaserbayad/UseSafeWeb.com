import { createJourney, transition, stateCopy, SCREEN, EVIDENCE_STATE } from './model.mjs';

const app = document.querySelector('#app');
let journey = createJourney();

const actionButton = (label, action, attrs = '') =>
  `<button class="sw-button prototype-choice" type="button" data-action="${action}" ${attrs}>${label}</button>`;
const secondaryButton = (label, action, attrs = '') =>
  `<button class="sw-button sw-button--secondary prototype-choice" type="button" data-action="${action}" ${attrs}>${label}</button>`;

function stateCard(title, value) {
  const copy = stateCopy(value);
  return `<section class="sw-status" data-evidence-state="${value}">
    <h2>${title}</h2>
    <div class="sw-status__label">${copy.label}</div>
    <p class="sw-status__evidence">${copy.supporting}</p>
  </section>`;
}

function discovery() {
  return `<section class="prototype-screen" data-screen="discovery">
    <p class="sw-kicker">First-phone safety setup</p>
    <h1>Clear guardrails for safer first-phone independence.</h1>
    <p>SafeWeb guides you through the applicable phone safeguard, a supported encrypted-DNS internet baseline, and at most one relevant service safeguard.</p>
    <div class="sw-callout"><strong>What this does not mean</strong><p>SafeWeb does not promise complete safety, monitor browsing history, or make every layer technically verifiable.</p></div>
    <div class="prototype-actions">${actionButton('Start setup', 'START')}${secondaryButton('Review compatibility & limits', 'SHOW_LIMITATIONS')}</div>
  </section>`;
}

function router() {
  return `<section class="prototype-screen" data-screen="router">
    <p class="sw-kicker">Route this device</p>
    <h1>Which supported phone are you setting up?</h1>
    <p>SafeWeb chooses the approved mechanism for the platform. You do not choose DoH versus DoT.</p>
    <div class="prototype-actions">
      ${actionButton('Android 9+ phone with Private DNS control', 'CHOOSE_PLATFORM', 'data-platform="android"')}
      ${actionButton('iPhone / iOS 14+ with approved DNS profile path', 'CHOOSE_PLATFORM', 'data-platform="iphone"')}
      ${secondaryButton('Another device or a managed/blocked setup', 'CHOOSE_PLATFORM', 'data-platform="other"')}
    </div>
    <p class="prototype-meta">No login, parent/child identity, payment, persistent device profile, or browsing history is required for this prototype route.</p>
  </section>`;
}

function nativeSafeguard() {
  return `<section class="prototype-screen" data-screen="native">
    <p class="sw-kicker">Phone safeguard</p>
    <h1>Check the phone’s native family safeguard</h1>
    <p>Use the current platform-owned parental-control guidance for this phone. SafeWeb does not claim to independently verify this setting in the current baseline.</p>
    <div class="prototype-actions">
      ${actionButton('I confirmed the native safeguard is set up', 'NATIVE_CONFIRMED')}
      ${secondaryButton('Continue — this still needs attention', 'NATIVE_ACTION_NEEDED')}
    </div>
  </section>`;
}

function dnsSetup() {
  if (journey.platform === 'android') {
    return `<section class="prototype-screen" data-screen="dns">
      <p class="sw-kicker">Internet safeguard · Android</p>
      <h1>Configure Android Private DNS</h1>
      <p>Open the phone’s current Private DNS settings, choose the custom/provider-hostname mode, and enter exactly:</p>
      <code class="prototype-code">dns.usesafeweb.com</code>
      <p>The parent performs the OS-required save/apply action. This web prototype does not silently change Android system DNS.</p>
      <div class="prototype-actions">${actionButton('I completed the Android setting', 'DNS_CONFIGURED')}</div>
    </section>`;
  }
  return `<section class="prototype-screen" data-screen="dns">
    <p class="sw-kicker">Internet safeguard · iPhone</p>
    <h1>Use the approved iPhone DNS profile path</h1>
    <p>The supported design uses a separately verified DNS Settings profile with the approved DoH Server URL:</p>
    <code class="prototype-code">https://dns.usesafeweb.com/dns-query</code>
    <p>This prototype does not distribute or fabricate a <code>.mobileconfig</code> file. Profile installation remains an explicit iOS/user authorization action.</p>
    <div class="prototype-actions">${actionButton('I completed the approved profile flow', 'DNS_CONFIGURED')}</div>
  </section>`;
}

function verify() {
  return `<section class="prototype-screen" data-screen="verify">
    <p class="sw-kicker">Verification</p>
    <h1>Check the current protection path</h1>
    <p>Configuration presence or parent confirmation alone cannot produce <strong>Protection verified</strong>. A future implementation must use the approved controlled verifier.</p>
    <fieldset class="prototype-test-controls">
      <legend>Internal prototype outcome controls</legend>
      <p class="prototype-meta">These controls simulate verifier outcomes for design coverage; they are not a production verifier.</p>
      <div class="prototype-actions">
        ${actionButton('Simulate qualifying verification success', 'VERIFY_RESULT', 'data-result="verified"')}
        ${secondaryButton('Simulate known repair needed', 'VERIFY_RESULT', 'data-result="action-needed"')}
        ${secondaryButton('Simulate uncertain / conflicting path', 'VERIFY_RESULT', 'data-result="uncertain"')}
        ${secondaryButton('Simulate unsupported / not covered', 'VERIFY_RESULT', 'data-result="not-covered"')}
      </div>
    </fieldset>
  </section>`;
}

function serviceSafeguard() {
  return `<section class="prototype-screen" data-screen="service">
    <p class="sw-kicker">Service safeguard</p>
    <h1>Add at most one relevant approved service safeguard</h1>
    <p>SafeWeb does not infer a service from popularity or child behavior. This prototype keeps the service generic because applicability must come from the current approved rule and parent-declared context.</p>
    <div class="prototype-actions">
      ${actionButton('No approved relevant safeguard applies', 'SERVICE_NONE')}
      ${secondaryButton('I set up the one relevant safeguard', 'SERVICE_CONFIRMED')}
    </div>
  </section>`;
}

function protectionMap() {
  return `<section class="prototype-screen" data-screen="map">
    <p class="sw-kicker">Protection Map</p>
    <h1>Current evidence, layer by layer</h1>
    <p>This is an evidence map, not a safety score. A completed journey does not force every layer into a positive state.</p>
    <div class="prototype-map">
      ${stateCard('Phone', journey.nativeState)}
      ${stateCard('Internet', journey.dnsState)}
      ${stateCard('Service', journey.serviceState)}
    </div>
    <div class="prototype-actions">
      ${secondaryButton('Remove SafeWeb DNS', 'REMOVE_DNS')}
      ${secondaryButton('Review limitations', 'SHOW_LIMITATIONS')}
    </div>
    <p class="sw-template-note">You can exit without an extra confirmation. Gaps remain visible; SafeWeb does not convert this map into an overall “safe / unsafe” result.</p>
  </section>`;
}

function troubleshooting() {
  const copy = stateCopy(journey.dnsState);
  const retry = [EVIDENCE_STATE.ACTION_NEEDED, EVIDENCE_STATE.UNCERTAIN].includes(journey.dnsState)
    ? actionButton('Recheck after the relevant condition changed', 'RETRY_AFTER_CHANGE', 'data-changed-condition="true"')
    : '';
  return `<section class="prototype-screen" data-screen="troubleshooting">
    <p class="sw-kicker">Help & recovery</p>
    <h1>${copy.label}</h1>
    <p>${copy.supporting}</p>
    <div class="sw-card">
      <h2>Smallest safe next step</h2>
      <p>Check the current device/network condition that caused the failure or uncertainty. VPN, browser/app custom DNS, Private Relay, managed controls, captive portals, and transport blocking can bound or invalidate a protection claim.</p>
    </div>
    <div class="prototype-actions">
      ${retry}
      ${secondaryButton('Remove SafeWeb DNS', 'REMOVE_DNS')}
      ${secondaryButton('Back', 'RETURN')}
    </div>
  </section>`;
}

function removal() {
  const instructions = journey.platform === 'android'
    ? 'Return to Android Private DNS and leave the custom SafeWeb provider-hostname mode, normally restoring the platform’s normal Automatic policy.'
    : journey.platform === 'iphone'
      ? 'Remove the exact SafeWeb DNS profile through the current iOS profile-management route.'
      : 'Remove or reset the applicable SafeWeb DNS configuration using the supported platform path.';
  return `<section class="prototype-screen" data-screen="removal">
    <p class="sw-kicker">Removal</p>
    <h1>Remove SafeWeb DNS</h1>
    <p>${instructions}</p>
    <p>Removal ends the SafeWeb DNS protection claim. Do not silently fall back to plaintext while continuing to show protection.</p>
    <div class="prototype-actions">${actionButton('I completed the removal step', 'CONFIRM_REMOVED')}</div>
  </section>`;
}

function recovery() {
  return `<section class="prototype-screen" data-screen="recovery">
    <p class="sw-kicker">Recovery check</p>
    <h1>Confirm normal connectivity separately</h1>
    <p>A normal-connectivity recovery check is not a protection verification. After removal, the DNS layer remains <strong>Removed</strong>.</p>
    <div class="prototype-actions">${actionButton('Simulate normal connectivity restored', 'RECOVERY_OK')}</div>
  </section>`;
}

function limitations() {
  return `<section class="prototype-screen" data-screen="limitations">
    <p class="sw-kicker">Compatibility & limits</p>
    <h1>Know what is not covered or cannot be verified</h1>
    <ul class="prototype-limits">
      <li>Unsupported or unaccepted device families are not given speculative client workarounds.</li>
      <li>Managed/locked DNS or profile controls may be Not covered, or their protection status may not be verifiable.</li>
      <li>VPN, iCloud Private Relay, browser/app custom DNS, captive portals, and network transport blocks can change or obscure the effective path.</li>
      <li>Parent confirmation and profile/settings presence do not equal system verification.</li>
      <li>No layer compensates for another uncovered layer unless current evidence directly proves it.</li>
    </ul>
    <div class="prototype-actions">
      ${secondaryButton('Back', 'RETURN')}
      ${journey.platform && journey.platform !== 'other' ? secondaryButton('Remove SafeWeb DNS', 'REMOVE_DNS') : ''}
    </div>
  </section>`;
}

function view() {
  switch (journey.screen) {
    case SCREEN.DISCOVERY: return discovery();
    case SCREEN.ROUTER: return router();
    case SCREEN.NATIVE: return nativeSafeguard();
    case SCREEN.DNS: return dnsSetup();
    case SCREEN.VERIFY: return verify();
    case SCREEN.SERVICE: return serviceSafeguard();
    case SCREEN.MAP: return protectionMap();
    case SCREEN.TROUBLESHOOTING: return troubleshooting();
    case SCREEN.REMOVAL: return removal();
    case SCREEN.RECOVERY: return recovery();
    case SCREEN.LIMITATIONS: return limitations();
    default: throw new Error(`No view for ${journey.screen}`);
  }
}

function render() {
  app.setAttribute('aria-busy', 'true');
  app.innerHTML = view();
  app.setAttribute('aria-busy', 'false');
  const heading = app.querySelector('h1');
  if (heading) {
    heading.tabIndex = -1;
    heading.focus({ preventScroll: true });
  }
}

function dispatch(action, payload = {}) {
  try {
    journey = transition(journey, action, payload);
    render();
  } catch (error) {
    app.insertAdjacentHTML('afterbegin', `<div class="sw-callout" role="alert"><strong>Prototype transition blocked:</strong> ${error.message}</div>`);
  }
}

document.addEventListener('click', event => {
  const target = event.target.closest('[data-action],[data-global-action]');
  if (!target) return;
  const action = target.dataset.action || target.dataset.globalAction;
  const payload = {};
  if (target.dataset.platform) payload.platform = target.dataset.platform;
  if (target.dataset.result) payload.result = target.dataset.result;
  if (target.dataset.changedCondition) payload.changedCondition = target.dataset.changedCondition === 'true';
  dispatch(action, payload);
});

render();
