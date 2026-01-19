export default function OpportunitiesList({ opportunities }) {
  return (
    <div className="mt-3">
      <h4 className="text-sm font-semibold mb-2">Opportunities</h4>

      {Object.entries(opportunities).map(([key, items]) => (
        <div key={key} className="mb-2">
          <p className="text-xs font-medium capitalize">{key}</p>
          <ul className="list-disc list-inside text-sm text-gray-700">
            {items.map((item, idx) => (
              <li key={idx}>{item}</li>
            ))}
          </ul>
        </div>
      ))}
    </div>
  );
}
