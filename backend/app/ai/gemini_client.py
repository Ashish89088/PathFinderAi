# Gemini Client Wrapper
import os
import time
from typing import Optional

# PSEUDO CLIENT – replace with official Gemini SDK when wiring key
class GeminiClient:
    def __init__(self):
        self.api_key = os.getenv("GEMINI_API_KEY")

    def generate(self, prompt: str, timeout: int = 15) -> str:
        """
        Simulated Gemini call (replace with real SDK call)
        """
        start = time.time()
        try:
            # TODO: Replace with Gemini 3 SDK call
            # response = gemini.generate_content(prompt)
            # return response.text

            # Mock response for now (hackathon-safe)
            time.sleep(1)  # simulate latency
            return f"MOCK_GEMINI_RESPONSE_FOR: {prompt[:200]}"

        except Exception as e:
            raise RuntimeError(f"Gemini API failed: {str(e)}")

        finally:
            latency = round(time.time() - start, 2)
            print(f"Gemini latency: {latency}s")
