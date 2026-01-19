import ReasoningAccordion from "./ReasoningAccordion";
import ConfidenceBar from "./ConfidenceBar";

export default function CareerCard({ data }) {
  return (
    <div className="border rounded-lg p-4 shadow-sm">
      <h2 className="text-xl font-semibold">{data.career}</h2>

      <ConfidenceBar score={data.confidence} />

      <ReasoningAccordion text={data.reasoning} />
    </div>
  );
}
