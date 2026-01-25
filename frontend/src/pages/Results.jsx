import { useParams } from "react-router-dom";
import { useNavigate } from "react-router-dom";
import StreamingResults from "./StreamingResults";
import CareerCard from "../components/CareerCard";
import { useState } from "react";
import { api } from "../services/api"; // axios instance


export default function Results() {
  const { userId } = useParams();
  console.log("Results Page User ID:", userId);
  const navigate = useNavigate();

  const [finalResult, setFinalResult] = useState(null);
  console.log("Final Result: Page",finalResult);

  const saveResult = async () =>{
     try {
      const res = await api.post(`/api/analyze-profile?user_id=${userId}`);

      console.info(`Analysis saved successfully for user ${userId}`);
      return res.data; // return data for further use if needed
    } catch (err) {
      console.error("Error saving analysis:", err); 
    }
  }

  // useEffect(() => {
  //   console.log("Final Result changed:", finalResult);
  //   if (!finalResult) return;

  //   api.post("/analyze-profile", { user_id: userId })
  //     .then(res => {
  //       console.log("Saved analysis response:", res.data);
  //     })
  //     .catch(err => console.error("Error saving analysis:", err))
  // }, [finalResult, userId]);

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

      <button
        onClick={() => saveResult()}
        style={{
          padding: "12px 20px",
          fontSize: "16px",
          marginTop: "20px",
          cursor: "pointer",
        }}
      >
        Save Result
      </button>


      <button
        onClick={() => navigate("/history/" + userId)}
        style={{
          padding: "12px 20px",
          fontSize: "16px",
          marginTop: "20px",
          cursor: "pointer",
        }}
      >
        History
      </button>
    </div>
  );
}
