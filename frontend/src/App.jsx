import { useEffect } from "react";
import { api } from "./services/api";

function App() {
  useEffect(() => {
    api.get("/")
      .then((res) => {
        console.log("Backend response:", res.data);
      })
      .catch((err) => {
        console.error("API error:", err);
      });
  }, []);

  return (
    <div style={{ padding: "20px" }}>
      <h1>PathFinder AI</h1>
      <p>Check the browser console to see backend response.</p>
    </div>
  );
}

export default App;
