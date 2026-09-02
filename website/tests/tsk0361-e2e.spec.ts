import AxeBuilder from "@axe-core/playwright";
import { expect, test, type Page } from "@playwright/test";

const locales = [
  { lang: "en", dir: "ltr" },
  { lang: "tr", dir: "ltr" },
  { lang: "ar", dir: "rtl" },
] as const;

async function expectNoHorizontalOverflow(page: Page) {
  const overflow = await page.evaluate(() => document.documentElement.scrollWidth - document.documentElement.clientWidth);
  expect(overflow).toBeLessThanOrEqual(1);
}

async function expectNoSeriousAccessibilityViolations(page: Page) {
  const result = await new AxeBuilder({ page })
    .withTags(["wcag2a", "wcag2aa", "wcag21a", "wcag21aa", "wcag22aa"])
    .analyze();
  expect(result.violations, JSON.stringify(result.violations, null, 2)).toEqual([]);
}

for (const locale of locales) {
  test(`${locale.lang} public home is truthful, responsive, directional and WCAG-clean`, async ({ page }) => {
    const errors: string[] = [];
    page.on("pageerror", (error) => errors.push(error.message));
    page.on("console", (message) => {
      if (message.type() === "error") errors.push(message.text());
    });

    const response = await page.goto(`/${locale.lang}`);
    expect(response?.status()).toBe(200);

    const site = page.locator(`.usw-site[lang="${locale.lang}"]`);
    await expect(site).toHaveAttribute("dir", locale.dir);
    await expect(page.getByRole("heading", { level: 1 })).toBeVisible();
    await expect(page.locator("main#main-content")).toBeVisible();
    await expect(page.locator(".sw-callout")).toBeVisible();
    await expect(page.locator("a.sw-button")).toBeVisible();

    await expectNoHorizontalOverflow(page);
    await expectNoSeriousAccessibilityViolations(page);
    expect(errors).toEqual([]);
  });
}

test("security headers are emitted on the public application boundary", async ({ page }) => {
  const response = await page.goto("/en");
  expect(response).not.toBeNull();
  const headers = response!.headers();
  expect(headers["x-content-type-options"]).toBe("nosniff");
  expect(headers["referrer-policy"]).toBe("no-referrer");
  expect(headers["x-frame-options"]).toBe("DENY");
  expect(headers["permissions-policy"]).toContain("camera=()");
  expect(headers["permissions-policy"]).toContain("microphone=()");
  expect(headers["permissions-policy"]).toContain("geolocation=()");
});

test("English core start flow remains accountless and produces an explicit selected state", async ({ page }) => {
  await page.goto("/en");
  await page.getByRole("link", { name: "Start setup" }).click();
  await expect(page).toHaveURL(/\/en\/start$/);
  await expect(page.getByText(/No account, payment card, child name, or browsing history/i)).toBeVisible();

  await page.getByRole("radio", { name: "Android phone" }).check();
  await page.getByRole("button", { name: "Continue" }).click();
  await expect(page).toHaveURL(/\/en\/start\?platform=android$/);
  await expect(page.getByRole("status")).toContainText("Phone type selected");
  await expect(page.getByRole("radio", { name: "Android phone" })).toBeChecked();
  await expectNoSeriousAccessibilityViolations(page);
});

test("Keystatic editor route is present without becoming product-state authority", async ({ page }) => {
  const response = await page.goto("/keystatic");
  expect(response?.status()).toBe(200);
  await expect(page.locator("body")).not.toBeEmpty();
});
