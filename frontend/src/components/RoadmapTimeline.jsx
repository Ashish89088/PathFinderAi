export default function RoadmapTimeline({ steps }) {
  return (
    <div className="mt-3">
      <h4 className="text-sm font-semibold mb-2">Roadmap</h4>
      <ul className="border-l-2 border-blue-500 pl-4 space-y-2">
        {steps.map((step, idx) => (
          <li key={idx} className="text-sm text-gray-700">
            <span className="text-blue-500 font-bold mr-2">•</span>
            {step}
          </li>
        ))}
      </ul>
    </div>
  );
}
