export default function ConfidenceBar({ score }) {
  const percent = Math.round(score * 100);

  return (
    <div className="mt-2">
      <div className="text-xs text-gray-600">
        Confidence: {percent}%
      </div>

      <div className="w-full bg-gray-200 rounded-full h-2 mt-1">
        <div
          className="bg-green-500 h-2 rounded-full"
          style={{ width: `${percent}%` }}
        />
      </div>
    </div>
  );
}
