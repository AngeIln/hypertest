import { EditorPanel } from "../components/editor";

export default function HomePage() {
  return (
    <main className="container">
      <h1>AI Code Studio</h1>
      <p>Générer, expliquer, exécuter et tester du code en ligne.</p>
      <EditorPanel />
    </main>
  );
}
