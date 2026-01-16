import { useNavigate } from "react-router-dom";

export default function LandingPage() {
  const navigate = useNavigate();

  return (
    <div style={{ padding: "40px", textAlign: "center" }}>
      <h1>PathFinder AI </h1>
      <p>
        Discover your ideal career using your real skills, interests,
        and digital footprint.
      </p>

      <button
        onClick={() => navigate("/profile")}
        style={{
          padding: "12px 20px",
          fontSize: "16px",
          marginTop: "20px",
          cursor: "pointer",
        }}
      >
        Get Started
      </button>
    </div>
  );
}
