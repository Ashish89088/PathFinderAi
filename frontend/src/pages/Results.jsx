import CareerCard from "../components/CareerCard";

const mockData = {
  career_recommendations: [
    {
      career: "Software Engineer",
      reasoning: "Strong tech inclination and coding presence",
      confidence: 0.82,
      roadmap: [
        "Master DSA",
        "Build 3 real-world projects",
        "Apply for internships"
      ],
      opportunities: {
        certifications: ["AWS", "Google Cloud"],
        events: ["Hackathons", "Meetups"]
      }
    }
  ]
};


export default function Results() {
  return (
    <div className="p-6 max-w-5xl mx-auto">
      <h1 className="text-2xl font-bold mb-4">Your Career Matches</h1>

      <div className="grid md:grid-cols-2 gap-4">
        {mockData.career_recommendations.map((item, index) => (
          <CareerCard key={index} data={item} />
        ))}
      </div>
    </div>
  );
}
