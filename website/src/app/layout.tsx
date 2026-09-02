import type { Metadata } from 'next';
import type { ReactNode } from 'react';
import './globals.css';

export const metadata: Metadata = {
  metadataBase: new URL('https://usesafeweb.com'),
  title: { default: 'SafeWeb', template: '%s | SafeWeb' },
};

export default function RootLayout({ children }: { children: ReactNode }) {
  return <html lang="en-GB"><body>{children}</body></html>;
}
