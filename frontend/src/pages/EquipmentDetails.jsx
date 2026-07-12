import { useState } from 'react';
import Hero from '../components/Hero.jsx';
import EquipmentSelect from '../components/EquipmentSelect.jsx';
import ResultCard from '../components/ResultCard.jsx';
import MarkdownBlock from '../components/MarkdownBlock.jsx';
import { getEquipmentInfo } from '../api/client.js';

export default function EquipmentDetails() {
  const [equipment, setEquipment] = useState('Cricket Bat');
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(false);

  async function loadDetails() {
    setLoading(true);
    try {
      setData(await getEquipmentInfo(equipment));
    } finally {
      setLoading(false);
    }
  }

  return (
    <div>
      <Hero eyebrow="Knowledge + Gemini" title="Equipment Details" subtitle="Generate description, material, usage, safety tips, brands, and FAQs." />
      <section className="glass-card form-card">
        <EquipmentSelect value={equipment} onChange={setEquipment} />
        <button onClick={loadDetails}>{loading ? 'Loading...' : 'Get Details'}</button>
      </section>
      {data && (
        <ResultCard title={data.equipment}>
          <p>{data.data.description}</p>
          <div className="tag-row">{data.data.materials.map((m) => <span key={m}>{m}</span>)}</div>
          <MarkdownBlock text={data.ai_response} />
        </ResultCard>
      )}
    </div>
  );
}
