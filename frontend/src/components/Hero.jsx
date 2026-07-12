export default function Hero({ eyebrow, title, subtitle }) {
  return (
    <section className="hero glass-card fade-in">
      <p className="eyebrow">{eyebrow}</p>
      <h1>{title}</h1>
      <p className="hero-subtitle">{subtitle}</p>
    </section>
  );
}
