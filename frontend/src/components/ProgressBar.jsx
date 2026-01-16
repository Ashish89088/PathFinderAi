export default function ProgressBar({ step, total }) {
  const percent = ((step + 1) / total) * 100;

  return (
    <div style={{ marginBottom: "20px" }}>
      <div
        style={{
          height: "8px",
          background: "#eee",
          borderRadius: "4px",
        }}
      >
        <div
          style={{
            width: `${percent}%`,
            height: "8px",
            background: "#4f46e5",
            borderRadius: "4px",
          }}
        />
      </div>
      <small>
        Step {step + 1} of {total}
      </small>
    </div>
  );
}
