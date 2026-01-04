import "./globals.css"
import localFont from "next/font/local"
import type { Metadata } from "next"

const geistSans = localFont({
  src: [
    { path: "./fonts/Geist-Regular.woff2", weight: "400", style: "normal" },
    { path: "./fonts/Geist-Bold.woff2", weight: "700", style: "normal" }
  ],
  variable: "--font-geist-sans"
})

const geistMono = localFont({
  src: [
    { path: "./fonts/GeistMono-Regular.woff2", weight: "400", style: "normal" },
    { path: "./fonts/GeistMono-Bold.woff2", weight: "700", style: "normal" }
  ],
  variable: "--font-geist-mono"
})

export const metadata: Metadata = {
  title: "CANCAN Admin",
  description: "CANCAN Admin Panel",
}

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en" className={`${geistSans.variable} ${geistMono.variable}`}>
      <body>{children}</body>
    </html>
  )
}

