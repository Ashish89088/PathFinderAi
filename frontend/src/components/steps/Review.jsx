import { api } from "../../services/api";

export default function Review({ data }) {

  const submitProfile = async () => {
    const payload = {
      name: data.name,
      age: Number(data.age),
      academics: {
        qualification: data.qualification,
        grades: data.grades,
      },
      interests: data.interests,
      hobbies: data.hobbies || "",
      platforms: {
        linkedin: data.linkedin,
        coding: data.coding,
      },
    };

    try {
      const res = await api.post("/api/profile", payload);
      alert("Profile submitted successfully!");
      console.log(res.data);
    } catch (err) {
      console.error(err);
      alert("Submission failed");
    }
  };

  return (
    <div>
      <pre>{JSON.stringify(data, null, 2)}</pre>
      <button onClick={submitProfile}>Submit Profile</button>
    </div>
  );
}
