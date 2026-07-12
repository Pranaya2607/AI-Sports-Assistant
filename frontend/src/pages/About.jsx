import Hero from '../components/Hero.jsx';

export default function About() {
  return (
    <div>
      <Hero eyebrow="About Project" title="Final Year Engineering Project" subtitle="A professional AI full-stack application combining computer vision and generative AI." />
      <section className="glass-card content-card">
        <h2>Project Objective</h2>
        <p>This project recognizes sports equipment, not sports activities. It uses a CNN for image classification and RAG with Gemini AI for recommendation and explanation.</p>
        <h2>Modules</h2>
        <ul>
          <li>React + Vite frontend with dark theme and glassmorphism UI</li>
          <li>FastAPI backend with REST APIs</li>
          <li>MobileNetV3 Large transfer learning using PyTorch</li>
          <li>FAISS vector database and Sentence Transformers embeddings</li>
          <li>Gemini AI response generation</li>
        </ul>
      </section>
    </div>
  );
}
