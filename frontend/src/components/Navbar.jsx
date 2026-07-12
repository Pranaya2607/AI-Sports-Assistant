import { NavLink } from 'react-router-dom';
import { Dumbbell } from 'lucide-react';

const links = [
  ['/', 'Dashboard'],
  ['/detect', 'Detection'],
  ['/details', 'Details'],
  ['/accessories', 'Accessories'],
  ['/size', 'Size'],
  ['/maintenance', 'Maintenance'],
  ['/condition', 'Condition'],
  ['/fake-detector', 'Fake Check'],
  ['/assistant', 'AI Assistant'],
  ['/about', 'About'],
];

export default function Navbar() {
  return (
    <header className="navbar glass-card">
      <NavLink to="/" className="brand">
        <Dumbbell size={26} />
        <span>AI Sports Assistant</span>
      </NavLink>
      <nav className="nav-links">
        {links.map(([path, label]) => (
          <NavLink key={path} to={path} className={({ isActive }) => isActive ? 'active nav-link' : 'nav-link'}>
            {label}
          </NavLink>
        ))}
      </nav>
    </header>
  );
}
