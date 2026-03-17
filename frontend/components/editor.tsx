"use client";

import { useState } from "react";

const LANGS = ["python", "javascript", "java", "csharp", "sql"];

export function EditorPanel() {
  const [language, setLanguage] = useState("python");
  const [prompt, setPrompt] = useState("Créer une fonction hello world");
  const [code, setCode] = useState("");
  const [result, setResult] = useState("");

  const api = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000";

  const generate = async () => {
    const response = await fetch(`${api}/api/v1/ai/generate`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ language, prompt }),
    });
    const data = await response.json();
    setCode(data.code || "");
  };

  const run = async () => {
    const response = await fetch(`${api}/api/v1/execution/run`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ language, code }),
    });
    const data = await response.json();
    setResult(JSON.stringify(data, null, 2));
  };

  return (
    <section className="card">
      <h2>Éditeur MVP</h2>
      <select value={language} onChange={(e) => setLanguage(e.target.value)}>
        {LANGS.map((lang) => (
          <option key={lang} value={lang}>{lang}</option>
        ))}
      </select>
      <textarea value={prompt} onChange={(e) => setPrompt(e.target.value)} rows={3} />
      <div className="actions">
        <button onClick={generate}>Générer</button>
        <button onClick={run}>Exécuter</button>
      </div>
      <textarea value={code} onChange={(e) => setCode(e.target.value)} rows={10} />
      <pre>{result}</pre>
    </section>
  );
}
