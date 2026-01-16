export default function Interests({ updateData }) {
  return (
    <textarea
      placeholder="Hobbies, interests, sports"
      onChange={(e) =>
        updateData({ interests: e.target.value })
      }
    />
  );
}
