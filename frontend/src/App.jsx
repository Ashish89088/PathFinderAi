import { BrowserRouter, Routes, Route } from "react-router-dom";
import LandingPage from "./pages/LandingPage";
import ProfileWizard from "./pages/ProfileWizard";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<LandingPage />} />
        <Route path="/profile" element={<ProfileWizard />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
