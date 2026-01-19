from app.ai.prompts.skill_inference import build_skill_inference_prompt

print(build_skill_inference_prompt({
    "signals": {"tech_inclination": 0.8},
    "raw_summary": {"interests": ["AI"]}
}))
