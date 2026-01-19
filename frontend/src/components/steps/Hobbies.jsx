const Hobbies = ({ data, updateData }) => {
  const handleChange = (e) => {
    const values = e.target.value
      .split(",")
      .map(v => v.trim())
      .filter(Boolean);

    updateData({
      ...data,
      hobbies: values
    });
  };

  return (
    <div>
      <input
        type="text"
        placeholder="Reading, Cricket"
        onChange={handleChange}
      />
    </div>
  );
};

export default Hobbies;
