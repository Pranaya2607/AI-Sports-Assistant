export default function MarkdownBlock({ text }) {
  if (!text) return null;
  return (
    <div className="markdown-block">
      {text.split('\n').map((line, index) => {
        const trimmed = line.trim();
        if (!trimmed) return <br key={index} />;
        if (trimmed.startsWith('#')) return <h3 key={index}>{trimmed.replace(/^#+\s*/, '')}</h3>;
        if (trimmed.startsWith('-') || trimmed.startsWith('*')) return <p key={index} className="bullet">{trimmed.replace(/^[-*]\s*/, '• ')}</p>;
        return <p key={index}>{line}</p>;
      })}
    </div>
  );
}
