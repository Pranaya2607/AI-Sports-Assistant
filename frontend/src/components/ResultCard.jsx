export default function ResultCard({ title, children }) {
  return (
    <section className="result-card glass-card fade-in">
      <h2>{title}</h2>
      <div>{children}</div>
    </section>
  );
}
