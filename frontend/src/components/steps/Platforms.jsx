export default function Platforms({ updateData }) {
  return (
    <>
      <input
        placeholder="LinkedIn URL"
        onChange={(e) =>
          updateData({ linkedin: e.target.value })
        }
      />
      <br />
      <input
        placeholder="GitHub / LeetCode URL"
        onChange={(e) =>
          updateData({ coding: e.target.value })
        }
      />
    </>
  );
}
