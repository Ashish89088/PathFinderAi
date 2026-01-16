export default function Academics({ updateData }) {
  return (
    <>
      <input
        placeholder="Highest Qualification"
        onChange={(e) =>
          updateData({ qualification: e.target.value })
        }
      />
      <br />
      <input
        placeholder="Grades / CGPA"
        onChange={(e) => updateData({ grades: e.target.value })}
      />
    </>
  );
}
