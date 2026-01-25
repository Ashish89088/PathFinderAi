import time
from google import genai


class GeminiClient:
    def __init__(self):
        self.client = genai.Client()

    def generate(self, prompt: str, timeout: int = 15) -> str:
        start = time.time()
        try:
            response = self.client.models.generate_content(
                model="gemini-3-flash-preview",
                contents=""
            )

            print("gemini response is",response)
            return response.text

        except Exception as e:
            raise RuntimeError(f"Gemini API failed: {str(e)}")

        finally:
            latency = round(time.time() - start, 2)
            print(f"Gemini latency: {latency}s")

