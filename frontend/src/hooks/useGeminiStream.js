import { useEffect, useState } from "react";

export default function useGeminiStream(userId) {
  const [events, setEvents] = useState([]);

  useEffect(() => {
    const eventSource = new EventSource(
      `http://localhost:8000/api/analyze-profile/stream?user_id=${userId}`
    );

    eventSource.onmessage = (event) => {
      const parsed = JSON.parse(event.data);
      setEvents((prev) => [...prev, parsed]);
    };

    return () => eventSource.close();
  }, [userId]);

  return events;
}
