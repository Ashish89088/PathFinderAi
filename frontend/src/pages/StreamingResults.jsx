import useGeminiStream from "../hooks/useGeminiStream";

export default function StreamingResults() {
  const events = useGeminiStream("USER_ID_HERE");

  return (
    <div className="p-6 max-w-3xl mx-auto">
      <h1 className="text-xl font-bold mb-4">AI Career Analysis</h1>

      {events.map((e, idx) => (
        <div key={idx} className="mb-3 p-3 border rounded">
          <p className="text-sm font-semibold">{e.message}</p>
          <pre className="text-xs mt-2 bg-gray-100 p-2 rounded">
            {JSON.stringify(e.data, null, 2)}
          </pre>
        </div>
      ))}
    </div>
  );
}
