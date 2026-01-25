import useGeminiStream from "../hooks/useGeminiStream";
import { useEffect, useRef } from "react";


export default function StreamingResults({ userId, onComplete }) {

  console.log("StreamingResults User ID:", userId);

  const events = useGeminiStream(userId);
  const completedRef = useRef(false);

  useEffect(() => {
    if (!events.length) return;

    const last = events[events.length - 1];

    if (last.stage === "final_result" && !completedRef.current) {
      completedRef.current = true; // prevent double call
      onComplete(last.data);
    }
  }, [events, onComplete]);

    return (
    <div className="space-y-3">
      <h2 className="font-semibold">Analyzing your profile...</h2>

      {events.map((e, i) => (
        <div key={i} className="border p-3 rounded">
          <strong>{e.stage}</strong>
          <pre>{JSON.stringify(e.data, null, 2)}</pre>
        </div>
      ))}
    </div>
  );
}
