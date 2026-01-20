# # Gemini Client Wrapper
# import os
# import time
# from typing import Optional

# # PSEUDO CLIENT – replace with official Gemini SDK when wiring key
# class GeminiClient:
#     def __init__(self):
#         self.api_key = os.getenv("GEMINI_API_KEY")

#     def generate(self, prompt: str, timeout: int = 15) -> str:
#         """
#         Simulated Gemini call (replace with real SDK call)
#         """
#         start = time.time()
#         try:
#             # TODO: Replace with Gemini 3 SDK call
#             # response = gemini.generate_content(prompt)
#             # return response.text

#             # Mock response for now (hackathon-safe)
#             time.sleep(1)  # simulate latency
#             return f"MOCK_GEMINI_RESPONSE_FOR: {prompt[:200]}"

#         except Exception as e:
#             raise RuntimeError(f"Gemini API failed: {str(e)}")

#         finally:
#             latency = round(time.time() - start, 2)
#             print(f"Gemini latency: {latency}s")


import os
import time
from google import genai


class GeminiClient:
    def __init__(self):
        # api_key = os.getenv("GEMINI_API_KEY")
        # if not api_key:
        #     raise RuntimeError("GEMINI_API_KEY not set")

        # genai.configure(api_key=api_key)
        # The client gets the API key from the environment variable `GEMINI_API_KEY`.
        self.client = genai.Client()

    def generate(self, prompt: str, timeout: int = 15) -> str:
        start = time.time()
        try:
            # response = self.model.generate_content(
            #     prompt,
            #     generation_config={
            #         "temperature": 0.6,
            #         "max_output_tokens": 1024,
            #     },
            # )
            response = self.client.models.generate_content(
                model="gemini-3-flash-preview",
                contents="How does AI work?"
            )

            print("gemini response is",response)
            return response.text

        except Exception as e:
            raise RuntimeError(f"Gemini API failed: {str(e)}")

        finally:
            latency = round(time.time() - start, 2)
            print(f"Gemini latency: {latency}s")

