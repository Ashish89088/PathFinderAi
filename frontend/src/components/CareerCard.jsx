import ReasoningAccordion from "./ReasoningAccordion";
import ConfidenceBar from "./ConfidenceBar";
import RoadmapTimeline from "./RoadmapTimeline";
import OpportunitiesList from "./OpportunitiesList";

export default function CareerCard({ data }) {
  return (
    <div className="border rounded-lg p-4 shadow-sm">
      <h2 className="text-xl font-semibold">{data.career}</h2>

      <ConfidenceBar score={data.confidence} />

      <ReasoningAccordion text={data.reasoning} />
            
      <RoadmapTimeline steps={data.roadmap} />

      <OpportunitiesList opportunities={data.opportunities} />

      <button className="mt-4 w-full bg-blue-600 text-white py-2 rounded">
        Start this path
      </button>
    </div>
  );
}
