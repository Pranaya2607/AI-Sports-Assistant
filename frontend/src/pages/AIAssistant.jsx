import { useState } from 'react';
import Hero from '../components/Hero.jsx';
import EquipmentSelect from '../components/EquipmentSelect.jsx';
import ResultCard from '../components/ResultCard.jsx';
import MarkdownBlock from '../components/MarkdownBlock.jsx';
import { postJson } from '../api/client.js';

export default function AIAssistant() {
  const [equipment, setEquipment] = useState('Football');
  const [question, setQuestion] = useState('Which accessories should I buy for a beginner?');
  const [answer, setAnswer] = useState('');
  const [loading, setLoading] = useState(false);

  async function ask() {
    setLoading(true);
    try {
      const data = await postJson('/ask-ai', { equipment, question });
      setAnswer(data.answer);
    } finally { setLoading(false); }
  }

  return (
    <div>
      <Hero eyebrow="Gemini + RAG" title="AI Equipment Assistant" subtitle="Ask questions about sports equipment, maintenance, buying, usage, and safety." />
      <section className="glass-card form-card">
        <EquipmentSelect value={equipment} onChange={setEquipment} />
        <textarea value={question} onChange={(e) => setQuestion(e.target.value)} />
        <button onClick={ask}>{loading ? 'Thinking...' : 'Ask AI'}</button>
      </section>
      {answer && <ResultCard title="AI Answer"><MarkdownBlock text={answer} /></ResultCard>}
    </div>
  );
}
