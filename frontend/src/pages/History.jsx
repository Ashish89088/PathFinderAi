import { useParams } from "react-router-dom";
import { useEffect, useState } from "react";
import { api } from "../services/api";
// import { useNavigate } from "react-router-dom";

export default function History() {
    console.log('Came here');
const { userId } = useParams();
console.log("User ID from params:", userId);

  const [history, setHistory] = useState([]);
  console.log("History data:", JSON.stringify(history, null, 2));
//   const navigate = useNavigate();

//   useEffect(() => {
//     api.get(`/api/history?user_id=${userId}`)
//       .then(res => setHistory(res.data));
//   }, [userId]);

  useEffect(() => {
  api.get(`/api/history?user_id=${userId}`)
        .then(res => setHistory([res.data]));
    }, [userId]);

  return (
    // <div className="p-6">
    //   <h1 className="text-xl font-bold mb-4">Past Career Analyses , History page</h1>

    //   {history.map(item => (
    //     <div
    //       key={item._id}
    //       className="border p-4 mb-3 cursor-pointer"
    //       onClick={() => navigate(`/results?analysis=${item._id}`)}
    //     >
    //       <p className="font-medium">
    //         {/* {item.career_recommendations?.[0]?.career} */}
    //         {item}
    //       </p>
    //       <p className="text-sm text-gray-500">
    //         {new Date(item.created_at).toLocaleString()}
    //       </p>
    //     </div>
    //   ))}
    // </div>
    <div className="p-6">
      <h1 className="text-2xl font-bold mb-4">History Data (JSON)</h1>
      <pre className="bg-gray-100 p-4 rounded overflow-auto" style={{ maxHeight: '80vh' }}>
        {JSON.stringify(history, null, 2)}
      </pre>
    </div>
  );
}
