import "./globals.css";
import type { ReactNode } from "react";

export const metadata = {
  title: "AI Code Studio",
  description: "MVP plateforme IA pour génération et test de code",
};

export default function RootLayout({ children }: { children: ReactNode }) {
  return (
    <html lang="fr">
      <body>{children}</body>
    </html>
  );
}
