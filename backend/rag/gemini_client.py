from typing import Dict, List

from utils.config import settings

SYSTEM_STYLE = """
You are an expert sports equipment advisor. Give clear, practical, student-project friendly answers.
Use the retrieved context when available. Do not claim certainty about authenticity or safety when only text observations are provided.

Format your output cleanly in Markdown, using headers (##), bold text for emphasis, and bullet points for lists.
Please include the following sections when discussing specific equipment:
- **Usage Guide**: How to properly use it for the sport
- **Sizing & Selection**: How to pick the right one based on player size or skill level
- **Maintenance**: How to clean and maintain it for longevity
- **Common Counterfeits**: Things to look out for (if applicable)

Keep the response engaging, well-structured, and highly professional.
"""

class GeminiClient:
    def __init__(self):
        self.api_key = settings.gemini_api_key
        self.model_name = settings.gemini_model
        self._model = None

    def _load_model(self):
        if self._model is not None:
            return self._model
        if not self.api_key:
            return None
        import google.generativeai as genai
        genai.configure(api_key=self.api_key)
        self._model = genai.GenerativeModel(self.model_name)
        return self._model

    def generate(self, prompt: str, contexts: List[Dict] | None = None) -> str:
        contexts = contexts or []
        context_block = "\n\n".join([f"Source: {c.get('source')}\n{c.get('text')}" for c in contexts])
        final_prompt = f"{SYSTEM_STYLE}\n\nRetrieved context:\n{context_block}\n\nUser request:\n{prompt}"
        model = self._load_model()
        if model is None:
            return self.offline_response(prompt, contexts)
        try:
            response = model.generate_content(final_prompt)
            return response.text.strip()
        except Exception as exc:
            return self.offline_response(prompt, contexts, error=str(exc))

    def offline_response(self, prompt: str, contexts: List[Dict], error: str | None = None) -> str:
        context_text = "\n".join([c.get("text", "") for c in contexts[:3]])
        prefix = "Gemini API key is not configured, so this is a local RAG-based response."
        if error:
            prefix = f"Gemini response failed, so this is a local RAG-based response. Error: {error}"
        return (
            f"{prefix}\n\n"
            "Based on the available knowledge base:\n\n"
            f"{context_text[:1800]}\n\n"
            "Recommendation: inspect the equipment condition, choose the correct size for the player, "
            "buy from an authorized seller, and follow sport-specific maintenance practices."
        )

gemini_client = GeminiClient()
