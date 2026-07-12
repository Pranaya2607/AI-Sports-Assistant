import { Route, Routes } from 'react-router-dom';
import Navbar from './components/Navbar.jsx';
import Dashboard from './pages/Dashboard.jsx';
import EquipmentDetection from './pages/EquipmentDetection.jsx';
import EquipmentDetails from './pages/EquipmentDetails.jsx';
import AccessoriesRecommendation from './pages/AccessoriesRecommendation.jsx';
import SizeRecommendation from './pages/SizeRecommendation.jsx';
import MaintenanceGuide from './pages/MaintenanceGuide.jsx';
import ConditionChecker from './pages/ConditionChecker.jsx';
import FakeEquipmentDetector from './pages/FakeEquipmentDetector.jsx';
import AIAssistant from './pages/AIAssistant.jsx';
import About from './pages/About.jsx';
import Footer from './components/Footer.jsx';

export default function App() {
  return (
    <div className="app-shell">
      <Navbar />
      <main className="page-container">
        <Routes>
          <Route path="/" element={<Dashboard />} />
          <Route path="/detect" element={<EquipmentDetection />} />
          <Route path="/details" element={<EquipmentDetails />} />
          <Route path="/accessories" element={<AccessoriesRecommendation />} />
          <Route path="/size" element={<SizeRecommendation />} />
          <Route path="/maintenance" element={<MaintenanceGuide />} />
          <Route path="/condition" element={<ConditionChecker />} />
          <Route path="/fake-detector" element={<FakeEquipmentDetector />} />
          <Route path="/assistant" element={<AIAssistant />} />
          <Route path="/about" element={<About />} />
        </Routes>
      </main>
      <Footer />
    </div>
  );
}
