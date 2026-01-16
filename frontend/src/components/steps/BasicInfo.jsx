export default function BasicInfo({ updateData }) {
  return (
    <>
      <input
        placeholder="Name"
        onChange={(e) => updateData({ name: e.target.value })}
      />
      <br />
      <input
        type="number"
        placeholder="Age"
        onChange={(e) => updateData({ age: e.target.value })}
      />
    </>
  );
}
