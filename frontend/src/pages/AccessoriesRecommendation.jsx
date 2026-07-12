import { useState } from 'react';
import Hero from '../components/Hero.jsx';
import EquipmentSelect from '../components/EquipmentSelect.jsx';
import ResultCard from '../components/ResultCard.jsx';
import MarkdownBlock from '../components/MarkdownBlock.jsx';
import { recommendAccessories } from '../api/client.js';

export default function AccessoriesRecommendation() {
  const [equipment, setEquipment] = useState('Football');
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(false);

  async function submit() {
    setLoading(true);
    try { setData(await recommendAccessories(equipment)); } finally { setLoading(false); }
  }

  return (
    <div>
      <Hero eyebrow="Smart Recommendation" title="Accessories Recommendation" subtitle="Find essential, safety, and maintenance accessories for each equipment." />
      <section className="glass-card form-card">
        <EquipmentSelect value={equipment} onChange={setEquipment} />
        <button onClick={submit}>{loading ? 'Generating...' : 'Recommend Accessories'}</button>
      </section>
      {data && <ResultCard title={`Accessories for ${data.equipment}`}>
        <div className="tag-row">{data.accessories.map((a) => <span key={a}>{a}</span>)}</div>
        <MarkdownBlock text={data.ai_response} />
      </ResultCard>}
    </div>
  );
}
