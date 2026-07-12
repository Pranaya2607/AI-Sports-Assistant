import { useState } from 'react';
import Hero from '../components/Hero.jsx';
import EquipmentSelect from '../components/EquipmentSelect.jsx';
import ResultCard from '../components/ResultCard.jsx';
import MarkdownBlock from '../components/MarkdownBlock.jsx';
import { postJson } from '../api/client.js';

export default function SizeRecommendation() {
  const [form, setForm] = useState({ equipment: 'Tennis Racket', age: '', height_cm: '', weight_kg: '', skill_level: 'beginner', sport_context: '' });
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(false);

  function update(key, value) { setForm((prev) => ({ ...prev, [key]: value })); }
  async function submit() {
    setLoading(true);
    try {
      setData(await postJson('/size-guide', {
        ...form,
        age: form.age ? Number(form.age) : null,
        height_cm: form.height_cm ? Number(form.height_cm) : null,
        weight_kg: form.weight_kg ? Number(form.weight_kg) : null,
      }));
    } finally { setLoading(false); }
  }

  return (
    <div>
      <Hero eyebrow="Personalized Guidance" title="Size Recommendation" subtitle="Generate size guidance using age, height, weight, and skill level." />
      <section className="glass-card form-card grid-form">
        <EquipmentSelect value={form.equipment} onChange={(v) => update('equipment', v)} />
        <input placeholder="Age" value={form.age} onChange={(e) => update('age', e.target.value)} />
        <input placeholder="Height in cm" value={form.height_cm} onChange={(e) => update('height_cm', e.target.value)} />
        <input placeholder="Weight in kg" value={form.weight_kg} onChange={(e) => update('weight_kg', e.target.value)} />
        <select value={form.skill_level} onChange={(e) => update('skill_level', e.target.value)}>
          <option>beginner</option><option>intermediate</option><option>advanced</option>
        </select>
        <input placeholder="Sport context" value={form.sport_context} onChange={(e) => update('sport_context', e.target.value)} />
        <button onClick={submit}>{loading ? 'Generating...' : 'Generate Size Guide'}</button>
      </section>
      {data && <ResultCard title={`Size Guide for ${data.equipment}`}><MarkdownBlock text={data.recommendation} /></ResultCard>}
    </div>
  );
}
