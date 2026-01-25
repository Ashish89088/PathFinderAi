import { BrowserRouter, Routes, Route } from "react-router-dom";
import LandingPage from "./pages/LandingPage";
import ProfileWizard from "./pages/ProfileWizard";
import Results from "./pages/Results";  
import History from './pages/History';
// import StreamingResults from "./pages/StreamingResults";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<LandingPage />} />
        <Route path="/profile" element={<ProfileWizard />} />
        {/* <Route path="/results" element={<Results />} /> */}
        <Route path="/analyze-profile/:userId" element={<Results />} />
        {/* React sample endpoint for result page : http://localhost:5173/analyze-profile/c7c336f5-2bc5-49b6-bd3c-305b58881992 */}
        {/* <Route path="/results/:userId" element={<StreamingResults />} /> */}
        <Route path="/history/:userId" element={<History />} />
        {/* React endpoint for history page = http://localhost:5173/history/c7c336f5-2bc5-49b6-bd3c-305b58881992 */}
      </Routes>
    </BrowserRouter>
  );
}

export default App;
