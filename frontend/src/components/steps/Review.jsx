export default function Review({ data }) {
  return (
    <pre style={{ background: "#f5f5f5", padding: "10px" }}>
      {JSON.stringify(data, null, 2)}
    </pre>
  );
}
