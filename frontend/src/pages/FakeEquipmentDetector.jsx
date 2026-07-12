import { useState } from 'react';
import Hero from '../components/Hero.jsx';
import EquipmentSelect from '../components/EquipmentSelect.jsx';
import ResultCard from '../components/ResultCard.jsx';
import MarkdownBlock from '../components/MarkdownBlock.jsx';
import { postJson } from '../api/client.js';

export default function FakeEquipmentDetector() {
  const [form, setForm] = useState({ equipment: 'Sports Shoes', brand_claimed: '', price: '', seller_type: '', observations: '' });
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(false);
  const update = (key, value) => setForm((prev) => ({ ...prev, [key]: value }));
  async function submit() { setLoading(true); try { setData(await postJson('/fake-detection', form)); } finally { setLoading(false); } }

  return (
    <div>
      <Hero eyebrow="Counterfeit Risk" title="Fake Equipment Detector" subtitle="Analyze warning signs like price, seller, packaging, serial number, and product finish." />
      <section className="glass-card form-card grid-form">
        <EquipmentSelect value={form.equipment} onChange={(v) => update('equipment', v)} />
        <input placeholder="Claimed brand" value={form.brand_claimed} onChange={(e) => update('brand_claimed', e.target.value)} />
        <input placeholder="Price" value={form.price} onChange={(e) => update('price', e.target.value)} />
        <input placeholder="Seller type" value={form.seller_type} onChange={(e) => update('seller_type', e.target.value)} />
        <textarea placeholder="Observations: logo, stitching, packaging, serial number, invoice" value={form.observations} onChange={(e) => update('observations', e.target.value)} />
        <button onClick={submit}>{loading ? 'Analyzing...' : 'Analyze Fake Risk'}</button>
      </section>
      {data && <ResultCard title={`Fake Risk Analysis for ${data.equipment}`}><MarkdownBlock text={data.fake_risk_analysis} /></ResultCard>}
    </div>
  );
}
