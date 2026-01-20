import { BrowserRouter, Routes, Route } from "react-router-dom";
import LandingPage from "./pages/LandingPage";
import ProfileWizard from "./pages/ProfileWizard";
import Results from "./pages/Results";
import StreamingResults from "./pages/StreamingResults";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<LandingPage />} />
        <Route path="/profile" element={<ProfileWizard />} />
        {/* <Route path="/results" element={<Results />} /> */}
        <Route path="/results/:userId" element={<Results />} />
        {/* <Route path="/results/:userId" element={<StreamingResults />} /> */}
      </Routes>
    </BrowserRouter>
  );
}

export default App;
