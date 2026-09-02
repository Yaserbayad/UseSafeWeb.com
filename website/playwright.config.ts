import { defineConfig } from "@playwright/test";

const isCI = Boolean(process.env.CI);

const desktop = { width: 1440, height: 900 };
const mobile = { width: 390, height: 844 };

export default defineConfig({
  testDir: "./tests",
  testMatch: "tsk0361-e2e.spec.ts",
  fullyParallel: true,
  forbidOnly: isCI,
  retries: isCI ? 1 : 0,
  workers: isCI ? 2 : undefined,
  reporter: isCI ? [["line"], ["html", { open: "never" }]] : "line",
  use: {
    baseURL: "http://127.0.0.1:3000",
    trace: "retain-on-failure",
    screenshot: "only-on-failure",
    video: "retain-on-failure",
  },
  webServer: {
    command: "npm run start -- --hostname 127.0.0.1",
    url: "http://127.0.0.1:3000/en",
    reuseExistingServer: !isCI,
    timeout: 120_000,
    env: {
      ...process.env,
      NEXT_TELEMETRY_DISABLED: "1",
    },
  },
  projects: [
    { name: "chromium-desktop", use: { browserName: "chromium", viewport: desktop } },
    { name: "chromium-mobile", use: { browserName: "chromium", viewport: mobile } },
    { name: "firefox-desktop", use: { browserName: "firefox", viewport: desktop } },
    { name: "firefox-mobile", use: { browserName: "firefox", viewport: mobile } },
    { name: "webkit-desktop", use: { browserName: "webkit", viewport: desktop } },
    { name: "webkit-mobile", use: { browserName: "webkit", viewport: mobile } },
  ],
});
