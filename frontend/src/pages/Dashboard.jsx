import { Link } from 'react-router-dom';
import Hero from '../components/Hero.jsx';
import StatCard from '../components/StatCard.jsx';

const modules = [
  ['Equipment Detection', '/detect', 'Upload an image and identify sports equipment using MobileNetV3 Large.'],
  ['Equipment Details', '/details', 'View material, usage, safety, brands, and AI-generated explanation.'],
  ['Accessories Recommendation', '/accessories', 'Get essential and optional accessories for each item.'],
  ['Size Recommendation', '/size', 'Generate size guidance using player details.'],
  ['Maintenance Guide', '/maintenance', 'Receive cleaning, storage, and repair guidance.'],
  ['Condition Checker', '/condition', 'Analyze damage observations and safety risk.'],
  ['Fake Equipment Detector', '/fake-detector', 'Check counterfeit warning signs using RAG + AI.'],
  ['AI Equipment Assistant', '/assistant', 'Ask questions about equipment, rules, and buying decisions.'],
];

export default function Dashboard() {
  return (
    <div>
      <Hero
        eyebrow="CNN + Gemini + RAG"
        title="AI-Based Sports Equipment Recognition and Recommendation System"
        subtitle="A complete full-stack final year project for recognizing equipment and generating intelligent recommendations."
      />
      <section className="stats-grid">
        <StatCard number="15" label="Equipment Classes" />
        <StatCard number="9" label="Frontend Pages" />
        <StatCard number="8" label="Backend APIs" />
        <StatCard number="3" label="AI Modules" />
      </section>
      <section className="module-grid">
        {modules.map(([title, path, desc]) => (
          <Link to={path} className="module-card glass-card" key={title}>
            <h3>{title}</h3>
            <p>{desc}</p>
          </Link>
        ))}
      </section>
    </div>
  );
}
