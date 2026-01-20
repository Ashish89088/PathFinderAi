# import time
# import json

# def gemini_stream(normalized_profile):
#     stages = [
#         {
#             "stage": "skill_inference",
#             "message": "Analyzing skills and behavioral traits...",
#             "data": {
#                 "strengths": ["Analytical thinking", "Self learning"],
#                 "working_style": "Disciplineddddddddddddd"
#             }
#         },
#         {
#             "stage": "career_matching",
#             "message": "Matching suitable career paths...",
#             "data": [
#                 {
#                     "career": "Software Engineer",
#                     "confidence": 0.82,
#                     "reasoning": "Strong tech inclination and coding presence"
#                 }
#             ]
#         },
#         {
#             "stage": "roadmap",
#             "message": "Generating personalized roadmap...",
#             "data": {
#                 "Software Engineer": [
#                     "Master DSA",
#                     "Build 3 projects",
#                     "Apply for internships"
#                 ]
#             }
#         }
#     ]

#     for stage in stages:
#         yield f"data: {json.dumps(stage)}\n\n"
#         time.sleep(1)  # simulate Gemini latency


from app.ai.orchestrator import run_career_ai_pipeline
def gemini_stream(normalized_profile):

    ai_result = run_career_ai_pipeline(normalized_profile)

    print("AI RESULT:", ai_result)

    for key, value in ai_result.items():
        yield f"data: {key}: {value}\n\n"

