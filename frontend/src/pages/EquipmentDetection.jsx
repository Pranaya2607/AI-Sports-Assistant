import { useState } from 'react';
import Hero from '../components/Hero.jsx';
import UploadBox from '../components/UploadBox.jsx';
import ResultCard from '../components/ResultCard.jsx';
import MarkdownBlock from '../components/MarkdownBlock.jsx';
import { predictEquipment } from '../api/client.js';

export default function EquipmentDetection() {
  const [file, setFile] = useState(null);
  const [preview, setPreview] = useState('');
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  function handleChange(event) {
    const selected = event.target.files[0];
    setFile(selected);
    setResult(null);
    setError('');
    if (selected) setPreview(URL.createObjectURL(selected));
  }

  async function handlePredict() {
    if (!file) {
      setError('Please select an image first.');
      return;
    }
    setLoading(true);
    setError('');
    try {
      const data = await predictEquipment(file);
      setResult(data);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  }

  return (
    <div>
      <Hero eyebrow="Image Recognition" title="Equipment Detection" subtitle="Upload a sports equipment image and detect the equipment class with confidence score." />
      <section className="two-column">
        <UploadBox file={file} preview={preview} onChange={handleChange} />
        <div className="glass-card form-card">
          <h2>Prediction</h2>
          <p>The backend uses MobileNetV3 Large transfer learning after you train the model with your dataset.</p>
          <button onClick={handlePredict} disabled={loading}>{loading ? 'Analyzing...' : 'Predict Equipment'}</button>
          {error && <p className="error-text">{error}</p>}
        </div>
      </section>
      {result && (
        <ResultCard title="Detection Result">
          <div className="prediction-main">
            <h3>{result.equipment || 'Model not trained yet'}</h3>
            <span>{result.confidence}% confidence</span>
          </div>
          <p>{result.message}</p>
          {result.top_predictions?.length > 0 && (
            <div className="prediction-list">
              {result.top_predictions.map((item) => (
                <div key={item.equipment}>
                  <span>{item.equipment}</span>
                  <strong>{item.confidence}%</strong>
                </div>
              ))}
            </div>
          )}
          <MarkdownBlock text={result.ai_summary} />
        </ResultCard>
      )}
    </div>
  );
}
