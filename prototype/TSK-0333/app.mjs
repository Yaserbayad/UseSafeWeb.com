import { createJourney, transition, stateCopy, SCREEN, EVIDENCE_STATE } from './model.mjs';

const app = document.querySelector('#app');
const announcer = document.querySelector('#prototype-announcer');
const rtlToggle = document.querySelector('[data-global-action="TOGGLE_RTL"]');
let journey = createJourney();

const eventMarker = (action) => `data-event-key="${action.toLowerCase()}"`;
const actionButton = (label, action, attrs = '') =>
  `<button class="sw-button prototype-choice" type="button" data-action="${action}" data-testid="action-${action.toLowerCase().replaceAll('_','-')}" ${eventMarker(action)} ${attrs}>${label}</button>`;
const secondaryButton = (label, action, attrs = '') =>
  `<button class="sw-button sw-button--secondary prototype-choice" type="button" data-action="${action}" data-testid="action-${action.toLowerCase().replaceAll('_','-')}" ${eventMarker(action)} ${attrs}>${label}</button>`;

function stateAction(layer, value) {
  if (layer === 'Phone' && value === EVIDENCE_STATE.ACTION_NEEDED) return secondaryButton('Review phone step', 'REVIEW_NATIVE');
  if (layer !== 'Internet') return '';
  if ([EVIDENCE_STATE.ACTION_NEEDED, EVIDENCE_STATE.UNCERTAIN].includes(value)) return secondaryButton('Troubleshoot Internet', 'OPEN_TROUBLESHOOT');
  if (value === EVIDENCE_STATE.NOT_COVERED) return secondaryButton('Review limitations', 'OPEN_LIMITS');
  if (value === EVIDENCE_STATE.REMOVED) return actionButton('Set up SafeWeb DNS again', 'RECONFIGURE');
  if (journey.dnsConfigured) return secondaryButton('Remove SafeWeb DNS', 'REMOVE_DNS');
  return '';
}

function stateCard(layer, value) {
  const copy = stateCopy(value);
  const id = layer.toLowerCase();
  return `<section class="sw-ds-state-item prototype-state-card" data-testid="map-${id}" data-evidence-layer="${id}" data-evidence-state="${value}">
    <h2>${layer}</h2>
    <p class="sw-ds-state-item__label" data-testid="map-${id}-label">${copy.label}</p>
    <p class="sw-ds-state-item__evidence">${copy.supporting}</p>
    ${stateAction(layer, value)}
  </section>`;
}

function home() {
  return `<section class="sw-ds-screen prototype-screen" data-screen="home" data-testid="screen-home">
    <div class="sw-ds-screen__header">
      <p class="sw-kicker">First Phone Safety Setup</p>
      <h1>Set up clearer guardrails without creating a SafeWeb account.</h1>
    </div>
    <div class="sw-ds-public-layout">
      <div class="sw-ds-long-copy">
        <p>SafeWeb guides you through three independent layers: the phone’s native safeguard, the supported encrypted-DNS internet path, and zero or one currently approved service safeguard.</p>
        <div class="sw-callout"><strong>Evidence, not a safety score</strong><p>The Protection Map shows what SafeWeb can verify, what you confirmed, and what is still uncertain or not covered. It never promises complete safety.</p></div>
      </div>
      <aside class="sw-card" aria-label="Privacy baseline">
        <h2>Accountless by default</h2>
        <p>No SafeWeb login, parent/child identity, browsing history, raw DNS history, payment, or persistent device dashboard is required for this setup.</p>
      </aside>
    </div>
    <div class="prototype-actions">${actionButton('Start setup', 'START')}${secondaryButton('Compatibility & limitations', 'OPEN_LIMITS')}</div>
  </section>`;
}

function router() {
  return `<section class="sw-ds-screen prototype-screen" data-screen="router" data-testid="screen-router">
    <div class="sw-ds-screen__header"><p class="sw-kicker">Setup start</p><h1>Which phone are you setting up?</h1></div>
    <p>SafeWeb selects the current approved platform path. The parent does not need to choose a DNS protocol.</p>
    <div class="prototype-actions">
      ${actionButton('Android 9+ with usable Private DNS control', 'CHOOSE_PLATFORM', 'data-platform="android"')}
      ${actionButton('iPhone / iOS 14+ with approved DNS profile path', 'CHOOSE_PLATFORM', 'data-platform="iphone"')}
      ${secondaryButton('Another or managed/blocked device', 'CHOOSE_PLATFORM', 'data-platform="other"')}
    </div>
  </section>`;
}

function nativeSafeguard() {
  const platform = journey.platform === 'iphone' ? 'Apple Screen Time / Content & Privacy Restrictions' : 'the current Google/Android family safeguard';
  return `<section class="sw-ds-screen prototype-screen" data-screen="native" data-testid="screen-native">
    <div class="sw-ds-screen__header"><p class="sw-kicker">Phone</p><h1>Check the phone’s native safeguard</h1></div>
    <p>Use ${platform} when it is applicable to this exact device/account context. SafeWeb does not collect platform credentials or silently change these settings.</p>
    <div class="sw-callout"><strong>Truth rule</strong><p>When you tell SafeWeb this step is complete, the state is <em>You confirmed this is set up</em> — not <em>Verified</em>.</p></div>
    <div class="prototype-actions">
      ${actionButton('I confirmed this is set up', 'NATIVE_CONFIRMED')}
      ${secondaryButton('This still needs attention', 'NATIVE_ACTION_NEEDED')}
    </div>
  </section>`;
}

function dnsSetup() {
  if (journey.platform === 'android') {
    return `<section class="sw-ds-screen prototype-screen" data-screen="dns" data-testid="screen-dns-android" data-instruction-id="DEV-AND-DNS-INSTALL">
      <div class="sw-ds-screen__header"><p class="sw-kicker">Internet · Android</p><h1>Set Android Private DNS to SafeWeb</h1></div>
      <ol class="prototype-steps">
        <li>Open Android Private DNS using the phone’s current Settings wording or search.</li>
        <li>Choose the provider-hostname/custom Private DNS option.</li>
        <li>Enter exactly <code class="sw-ds-tech" data-testid="android-dns-value">dns.usesafeweb.com</code></li>
        <li>Save using Android’s own control, then return here.</li>
      </ol>
      <p>Do not enter <code>https://</code> or <code>:853</code>. SafeWeb cannot silently change system DNS.</p>
      <div class="prototype-actions">
        ${actionButton('I completed the Android setting', 'DNS_CONFIGURED')}
        ${secondaryButton('It was already configured', 'DNS_ALREADY_CONFIGURED')}
      </div>
    </section>`;
  }
  return `<section class="sw-ds-screen prototype-screen" data-screen="dns" data-testid="screen-dns-iphone" data-instruction-id="DEV-IOS-DNS-INSTALL">
    <div class="sw-ds-screen__header"><p class="sw-kicker">Internet · iPhone</p><h1>Use the approved SafeWeb DNS profile path</h1></div>
    <p>The supported design uses the separately verified DNS Settings profile and this exact DoH Server URL:</p>
    <code class="sw-ds-tech" data-testid="iphone-doh-value">https://dns.usesafeweb.com/dns-query</code>
    <p>iOS must show and obtain explicit user permission for profile installation. Profile presence alone does not prove the SafeWeb path is active.</p>
    <div class="prototype-actions">
      ${actionButton('I completed the approved profile flow', 'DNS_CONFIGURED')}
      ${secondaryButton('The profile was already present', 'DNS_ALREADY_CONFIGURED')}
    </div>
  </section>`;
}

function verify() {
  return `<section class="sw-ds-screen prototype-screen" data-screen="verify" data-testid="screen-verify">
    <div class="sw-ds-screen__header"><p class="sw-kicker">Internet verification</p><h1>Check what the current evidence actually proves</h1></div>
    <p>Configuration presence and parent confirmation cannot produce <strong>Verified</strong>. The production implementation must use the approved controlled verifier.</p>
    <fieldset class="prototype-test-controls" data-testid="verification-fixture">
      <legend>Internal deterministic outcome fixture</legend>
      <p class="prototype-meta">These controls exist only to exercise every accepted state. They transmit nothing and are not the production verifier.</p>
      <div class="prototype-actions">
        ${actionButton('Qualifying verification succeeds', 'VERIFY_RESULT', 'data-result="verified"')}
        ${secondaryButton('Known repair is needed', 'VERIFY_RESULT', 'data-result="action-needed"')}
        ${secondaryButton('Evidence is conflicting or inconclusive', 'VERIFY_RESULT', 'data-result="uncertain"')}
        ${secondaryButton('This path is not supported', 'VERIFY_RESULT', 'data-result="not-covered"')}
      </div>
    </fieldset>
  </section>`;
}

function serviceSafeguard() {
  return `<section class="sw-ds-screen prototype-screen" data-screen="service" data-testid="screen-service">
    <div class="sw-ds-screen__header"><p class="sw-kicker">Service</p><h1>Add only a currently approved relevant service safeguard</h1></div>
    <p>The current catalogue hard-codes no external service. Zero applicable services is a valid completed result; SafeWeb must not infer service use from browsing, DNS, or app history.</p>
    <div class="prototype-actions">
      ${actionButton('No approved relevant service applies', 'SERVICE_NONE')}
      ${secondaryButton('Test future one-approved-service confirmation', 'SERVICE_CONFIRMED')}
    </div>
  </section>`;
}

function protectionMap() {
  return `<section class="sw-ds-screen prototype-screen" data-screen="map" data-testid="screen-map">
    <div class="sw-ds-screen__header"><p class="sw-kicker">Protection Map</p><h1>Current evidence, layer by layer</h1></div>
    <p data-testid="map-no-score">This is an evidence map, not a safety score. Mixed states are a valid completed journey and material gaps stay visible.</p>
    <div class="sw-ds-state-grid prototype-map" data-layout="three" data-testid="protection-map">
      ${stateCard('Phone', journey.nativeState)}
      ${stateCard('Internet', journey.dnsState)}
      ${stateCard('Service', journey.serviceState)}
    </div>
    <div class="prototype-actions">
      ${secondaryButton('A site or service seems blocked', 'OPEN_FALSE_POSITIVE')}
      ${secondaryButton('Help with this setup', 'OPEN_HELP')}
      ${secondaryButton('Review limitations', 'OPEN_LIMITS')}
    </div>
    <p class="sw-template-note">There is no extra “success” acknowledgement that hides unresolved gaps, and no seventh completion state.</p>
  </section>`;
}

function troubleshooting() {
  const copy = stateCopy(journey.dnsState);
  const retryRelevant = [EVIDENCE_STATE.ACTION_NEEDED, EVIDENCE_STATE.UNCERTAIN].includes(journey.dnsState);
  return `<section class="sw-ds-screen prototype-screen" data-screen="troubleshoot" data-testid="screen-troubleshoot">
    <div class="sw-ds-screen__header"><p class="sw-kicker">Troubleshoot Internet</p><h1>${copy.label}</h1></div>
    <p>${copy.supporting}</p>
    <div class="sw-card"><h2>Smallest safe next check</h2><p>Check the relevant changed condition: VPN, Private Relay, browser/app secure DNS, managed policy, captive portal, or encrypted-DNS transport availability. Do not weaken employer, school, or device-management controls just to obtain a positive state.</p></div>
    <div class="prototype-actions">
      ${retryRelevant && !journey.changedCondition ? actionButton('I changed the relevant condition', 'MARK_CONDITION_CHANGED') : ''}
      ${retryRelevant && journey.changedCondition ? actionButton('Check again', 'RETRY_AFTER_CHANGE') : ''}
      ${journey.dnsConfigured ? secondaryButton('Remove SafeWeb DNS', 'REMOVE_DNS') : ''}
      ${secondaryButton('Back', 'RETURN')}
    </div>
  </section>`;
}

function falsePositive() {
  return `<section class="sw-ds-screen prototype-screen" data-screen="false-positive" data-testid="screen-false-positive">
    <div class="sw-ds-screen__header"><p class="sw-kicker">False positive</p><h1>A legitimate site or service seems blocked</h1></div>
    <p>A DNS-path <strong>Verified</strong> state means only that qualifying current evidence confirms the intended SafeWeb DNS path. It does not guarantee zero false positives.</p>
    <div class="sw-card"><h2>Minimal diagnostic boundary</h2><p>A future approved report may use only the single destination/service the parent voluntarily identifies plus the minimum current platform/state/reference context. It must not request browsing history, raw DNS logs, child identity, credentials, or a persistent account.</p></div>
    <p>Acknowledgement is not evidence and does not upgrade any Protection Map state. This prototype does not invent an arbitrary allowlist or bypass.</p>
    <div class="prototype-actions">
      ${journey.dnsConfigured ? secondaryButton('Remove SafeWeb DNS instead', 'REMOVE_DNS') : ''}
      ${secondaryButton('Back', 'RETURN')}
    </div>
  </section>`;
}

function help() {
  return `<section class="sw-ds-screen prototype-screen" data-screen="help" data-testid="screen-help">
    <div class="sw-ds-screen__header"><p class="sw-kicker">Help</p><h1>Choose the issue you are trying to solve</h1></div>
    <p>Ordinary support is self-service. Opening Help does not change any protection state.</p>
    <div class="prototype-actions">
      ${[EVIDENCE_STATE.ACTION_NEEDED, EVIDENCE_STATE.UNCERTAIN].includes(journey.dnsState) ? actionButton('Verification or setup is not working', 'OPEN_TROUBLESHOOT') : ''}
      ${journey.platform && journey.platform !== 'other' ? secondaryButton('A site or service seems blocked', 'OPEN_FALSE_POSITIVE') : ''}
      ${journey.dnsConfigured ? secondaryButton('Remove SafeWeb DNS', 'REMOVE_DNS') : ''}
      ${secondaryButton('Compatibility & limitations', 'OPEN_LIMITS')}
      ${secondaryButton('Back', 'RETURN')}
    </div>
    <p class="prototype-meta">Exceptional human escalation, if separately authorized for a material unresolved issue, remains bounded and is not a routine prerequisite for setup success.</p>
  </section>`;
}

function limits() {
  return `<section class="sw-ds-screen prototype-screen" data-screen="limits" data-testid="screen-limits">
    <div class="sw-ds-screen__header"><p class="sw-kicker">Compatibility & limitations</p><h1>Know what is unsupported or cannot be proven</h1></div>
    <ul class="prototype-limits">
      <li>Unsupported device/platform/network tuples stop with <strong>Not covered</strong>; no speculative client workaround is offered.</li>
      <li>Managed controls, VPNs, Private Relay, browser/app secure DNS, captive portals, and network transport blocks can make status <strong>uncertain</strong>.</li>
      <li>Parent confirmation, profile presence, and configuration presence are not system verification.</li>
      <li>One protected layer never compensates for another uncovered layer unless current evidence directly proves it.</li>
      <li>SafeWeb does not promise complete safety or create an overall safe/unsafe score.</li>
    </ul>
    <div class="prototype-actions">
      ${journey.dnsConfigured ? secondaryButton('Remove SafeWeb DNS', 'REMOVE_DNS') : ''}
      ${secondaryButton('Back', 'RETURN')}
    </div>
  </section>`;
}

function removal() {
  const instructions = journey.platform === 'android'
    ? 'Use the current Android Private DNS settings to leave the custom SafeWeb provider-hostname mode, normally restoring the platform’s normal Automatic policy.'
    : journey.platform === 'iphone'
      ? 'Remove the exact SafeWeb DNS profile through the current iOS profile-management route. If the device/profile is management-owned, stop and follow that authority.'
      : 'Use only the current supported platform removal path.';
  return `<section class="sw-ds-screen prototype-screen" data-screen="remove" data-testid="screen-remove">
    <div class="sw-ds-screen__header"><p class="sw-kicker">Removal</p><h1>Remove SafeWeb DNS</h1></div>
    <p>${instructions}</p>
    <p>Removal withdraws the active SafeWeb DNS protection claim. Normal DNS afterward is a recovery result, not SafeWeb verification.</p>
    <div class="prototype-actions">${actionButton('I completed the removal step', 'CONFIRM_REMOVED')}</div>
  </section>`;
}

function recovery() {
  return `<section class="sw-ds-screen prototype-screen" data-screen="recovery" data-testid="screen-recovery">
    <div class="sw-ds-screen__header"><p class="sw-kicker">Recovery</p><h1>Check ordinary connectivity separately</h1></div>
    <p>The SafeWeb Internet state remains <strong>Removed</strong>. A successful ordinary-connectivity check does not restore a protection claim.</p>
    <div class="prototype-actions">
      ${actionButton('Ordinary connectivity works', 'RECOVERY_OK')}
      ${secondaryButton('Set SafeWeb DNS up again', 'RECONFIGURE')}
    </div>
  </section>`;
}

function resetLost() {
  return `<section class="sw-ds-screen prototype-screen" data-screen="reset-lost" data-testid="screen-reset-lost">
    <div class="sw-ds-screen__header"><p class="sw-kicker">Transient state lost</p><h1>Start the setup route again</h1></div>
    <p>This accountless prototype does not pretend it can restore a persistent device journey. Website state was cleared, but this action does not change any DNS or native setting on the phone.</p>
    <div class="sw-callout"><strong>Important</strong><p>If SafeWeb DNS may still be configured on the device, the new journey must inspect or re-verify it rather than assuming either protection or removal.</p></div>
    <div class="prototype-actions">${actionButton('Route this phone again', 'START')}</div>
  </section>`;
}

function view() {
  switch (journey.screen) {
    case SCREEN.HOME: return home();
    case SCREEN.ROUTER: return router();
    case SCREEN.NATIVE: return nativeSafeguard();
    case SCREEN.DNS: return dnsSetup();
    case SCREEN.VERIFY: return verify();
    case SCREEN.SERVICE: return serviceSafeguard();
    case SCREEN.MAP: return protectionMap();
    case SCREEN.TROUBLESHOOT: return troubleshooting();
    case SCREEN.FALSE_POSITIVE: return falsePositive();
    case SCREEN.HELP: return help();
    case SCREEN.LIMITS: return limits();
    case SCREEN.REMOVE: return removal();
    case SCREEN.RECOVERY: return recovery();
    case SCREEN.RESET_LOST: return resetLost();
    default: throw new Error(`No view for ${journey.screen}`);
  }
}

function render(announce = true) {
  app.setAttribute('aria-busy', 'true');
  app.innerHTML = view();
  app.setAttribute('aria-busy', 'false');
  const heading = app.querySelector('h1');
  if (heading && announce) {
    heading.tabIndex = -1;
    heading.focus({ preventScroll: true });
    announcer.textContent = heading.textContent;
  }
  document.body.dataset.screen = journey.screen;
  document.body.dataset.platform = journey.platform || 'none';
}

function dispatch(action, payload = {}) {
  try {
    journey = transition(journey, action, payload);
    render();
  } catch (error) {
    const alert = document.createElement('div');
    alert.className = 'sw-callout prototype-error';
    alert.setAttribute('role', 'alert');
    alert.textContent = `Prototype transition blocked: ${error.message}`;
    app.prepend(alert);
  }
}

function toggleRTL() {
  const rtl = document.documentElement.dir !== 'rtl';
  document.documentElement.dir = rtl ? 'rtl' : 'ltr';
  rtlToggle.setAttribute('aria-pressed', String(rtl));
  rtlToggle.textContent = rtl ? 'LTR structure' : 'RTL structure';
  announcer.textContent = rtl ? 'Right-to-left structural preview on' : 'Left-to-right structural preview on';
}

document.addEventListener('click', event => {
  const target = event.target.closest('[data-action],[data-global-action]');
  if (!target) return;
  event.preventDefault();
  const action = target.dataset.action || target.dataset.globalAction;
  if (action === 'TOGGLE_RTL') return toggleRTL();
  const payload = {};
  if (target.dataset.platform) payload.platform = target.dataset.platform;
  if (target.dataset.result) payload.result = target.dataset.result;
  dispatch(action, payload);
});

render(false);
