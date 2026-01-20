import { useParams } from "react-router-dom";
import StreamingResults from "./StreamingResults";
import CareerCard from "../components/CareerCard";
import { useState } from "react";

export default function Results() {
  const { userId } = useParams();

  const [finalResult, setFinalResult] = useState(null);
  console.log("Final Result: Page");

  return (
    <div className="p-6 max-w-5xl mx-auto">
      <h1 className="text-2xl font-bold mb-4">
        Your Career Analysis
      </h1>

      {/* STEP 1: STREAMING */}
      {!finalResult && (
        <StreamingResults
          userId={userId}
          onComplete={setFinalResult}
        />
      )}

      {/* STEP 2: FINAL RESULTS */}
      {finalResult && (
        <div className="grid md:grid-cols-2 gap-4 mt-6">
          {finalResult.career_recommendations.map((item, index) => (
            <CareerCard key={index} data={item} />
          ))}
        </div>
      )}
    </div>
  );
}
