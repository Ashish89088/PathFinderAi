// export default function Interests({ updateData }) {
//   return (
//     <textarea
//       placeholder="Hobbies, interests, sports"
//       onChange={(e) =>
//         updateData({ interests: e.target.value })
//       }
//     />
//   );
// }

const Interests = ({ data, updateData }) => {
  const handleChange = (e) => {
    const values = e.target.value
      .split(",")
      .map(v => v.trim())
      .filter(Boolean);

    updateData({
      ...data,
      interests: values
    });
  };

  return (
    <div>
      <input
        type="text"
        placeholder="AI, Football, Startups"
        onChange={handleChange}
      />
    </div>
  );
};

export default Interests;
