import { useState } from 'react';
import Hero from '../components/Hero.jsx';
import EquipmentSelect from '../components/EquipmentSelect.jsx';
import ResultCard from '../components/ResultCard.jsx';
import MarkdownBlock from '../components/MarkdownBlock.jsx';
import { postJson } from '../api/client.js';

export default function ConditionChecker() {
  const [form, setForm] = useState({ equipment: 'Helmet', observed_damage: '', age_months: '', usage_frequency: 'weekly' });
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(false);
  const update = (key, value) => setForm((prev) => ({ ...prev, [key]: value }));
  async function submit() {
    setLoading(true);
    try { setData(await postJson('/condition', { ...form, age_months: form.age_months ? Number(form.age_months) : null })); }
    finally { setLoading(false); }
  }

  return (
    <div>
      <Hero eyebrow="Safety Analysis" title="Equipment Condition Checker" subtitle="Classify condition based on observed damage, age, and usage frequency." />
      <section className="glass-card form-card grid-form">
        <EquipmentSelect value={form.equipment} onChange={(v) => update('equipment', v)} />
        <input placeholder="Age in months" value={form.age_months} onChange={(e) => update('age_months', e.target.value)} />
        <input placeholder="Usage frequency" value={form.usage_frequency} onChange={(e) => update('usage_frequency', e.target.value)} />
        <textarea placeholder="Describe observed damage" value={form.observed_damage} onChange={(e) => update('observed_damage', e.target.value)} />
        <button onClick={submit}>{loading ? 'Checking...' : 'Check Condition'}</button>
      </section>
      {data && <ResultCard title={`Condition Analysis for ${data.equipment}`}><MarkdownBlock text={data.condition_analysis} /></ResultCard>}
    </div>
  );
}
