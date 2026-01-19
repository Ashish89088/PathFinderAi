import { useState } from "react";

export default function ReasoningAccordion({ text }) {
  const [open, setOpen] = useState(false);

  return (
    <div className="mt-3">
      <button
        className="text-blue-600 text-sm"
        onClick={() => setOpen(!open)}
      >
        {open ? "Hide reasoning ▲" : "Why this career? ▼"}
      </button>

      {open && (
        <p className="mt-2 text-gray-700 text-sm">
          {text}
        </p>
      )}
    </div>
  );
}
