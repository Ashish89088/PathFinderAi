import { useState } from "react";
import BasicInfo from "../components/steps/BasicInfo";
import Academics from "../components/steps/Academics";
import Interests from "../components/steps/Interests";
import Platforms from "../components/steps/Platforms";
import Review from "../components/steps/Review";
import ProgressBar from "../components/ProgressBar";

const steps = [
  { title: "Basic Info", component: BasicInfo },
  { title: "Academics", component: Academics },
  { title: "Interests", component: Interests },
  { title: "Platforms", component: Platforms },
  { title: "Review", component: Review },
];

export default function ProfileWizard() {
  const [currentStep, setCurrentStep] = useState(0);
  const [profileData, setProfileData] = useState({});

  const StepComponent = steps[currentStep].component;

  return (
    <div style={{ maxWidth: "600px", margin: "40px auto" }}>
      <ProgressBar step={currentStep} total={steps.length} />

      <h2>{steps[currentStep].title}</h2>

      <StepComponent
        data={profileData}
        updateData={(data) =>
          setProfileData({ ...profileData, ...data })
        }
      />

      <div style={{ marginTop: "20px" }}>
        {currentStep > 0 && (
          <button onClick={() => setCurrentStep(currentStep - 1)}>
            Back
          </button>
        )}

        <button
          style={{ marginLeft: "10px" }}
          onClick={() => setCurrentStep(currentStep + 1)}
        >
          {currentStep === steps.length - 1 ? "Submit" : "Next"}
        </button>
      </div>
    </div>
  );
}
