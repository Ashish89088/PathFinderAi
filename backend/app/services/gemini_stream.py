import json
from app.ai.orchestrator import run_career_ai_pipeline
import json
def gemini_stream(normalized_profile):

    ai_result = run_career_ai_pipeline(normalized_profile)

    print("AI RESULT:", ai_result)

    for key, value in ai_result.items():
        payload = {
            "stage": key,
            "data": value
        }
        yield f"data: {json.dumps(payload)}\n\n"

