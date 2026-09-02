import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: { default: "SafeWeb", template: "%s | SafeWeb" },
  description: "Practical first-phone safety setup for parents and caregivers, with clear protection limits and no browsing surveillance.",
};

export default function RootLayout({ children }: Readonly<{ children: React.ReactNode }>) {
  return (
    <html lang="en">
      <body>
        <a className="usw-skip-link" href="#main-content">Skip to main content</a>
        {children}
      </body>
    </html>
  );
}
