import { useEffect, useState, useRef } from "react";

export default function useGeminiStream(userId) {
  const [events, setEvents] = useState([]);
  const eventSourceRef = useRef(null);

  useEffect(() => {
    if (!userId) return;

    // prevent duplicate connections
    if (eventSourceRef.current) return;

    const eventSource = new EventSource(
      `http://localhost:8000/api/analyze-profile/stream?user_id=${userId}`
    );

    eventSourceRef.current = eventSource;

    eventSource.onmessage = (event) => {
      console.log("Received event:", event.data);
      const parsed = JSON.parse(event.data);
      setEvents((prev) => [...prev, parsed]);

      // stop streaming when final result arrives
      if (parsed.stage === "final_result") {
        eventSource.close();
        eventSourceRef.current = null;
      }
    };

    eventSource.onerror = () => {
      eventSource.close();
      eventSourceRef.current = null;
    };

    return () => {
      eventSource.close();
      eventSourceRef.current = null;
    };
  }, [userId]);

  return events;
}
