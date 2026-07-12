import { useState } from 'react';
import Hero from '../components/Hero.jsx';
import EquipmentSelect from '../components/EquipmentSelect.jsx';
import ResultCard from '../components/ResultCard.jsx';
import MarkdownBlock from '../components/MarkdownBlock.jsx';
import { postJson } from '../api/client.js';

export default function MaintenanceGuide() {
  const [form, setForm] = useState({ equipment: 'Cricket Bat', usage_frequency: 'weekly', material: '', issue: '' });
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(false);
  const update = (key, value) => setForm((prev) => ({ ...prev, [key]: value }));
  async function submit() { setLoading(true); try { setData(await postJson('/maintenance', form)); } finally { setLoading(false); } }

  return (
    <div>
      <Hero eyebrow="Care and Durability" title="Maintenance Guide" subtitle="Create care routines for cleaning, storage, inspection, and repair." />
      <section className="glass-card form-card grid-form">
        <EquipmentSelect value={form.equipment} onChange={(v) => update('equipment', v)} />
        <input placeholder="Usage frequency" value={form.usage_frequency} onChange={(e) => update('usage_frequency', e.target.value)} />
        <input placeholder="Material" value={form.material} onChange={(e) => update('material', e.target.value)} />
        <input placeholder="Current issue" value={form.issue} onChange={(e) => update('issue', e.target.value)} />
        <button onClick={submit}>{loading ? 'Generating...' : 'Generate Guide'}</button>
      </section>
      {data && <ResultCard title={`Maintenance for ${data.equipment}`}><MarkdownBlock text={data.guide} /></ResultCard>}
    </div>
  );
}
