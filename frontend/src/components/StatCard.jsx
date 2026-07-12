export default function StatCard({ number, label }) {
  return (
    <div className="stat-card glass-card pop-in">
      <strong>{number}</strong>
      <span>{label}</span>
    </div>
  );
}
