from llama_cpp import Llama
import os

MODEL_PATH = os.path.join("backend/models", "gemma-3-4b-it.Q4_K_M.gguf")

class LLMHandler:
    def __init__(self, model_path=MODEL_PATH):
        self.llm = Llama(
            model_path=model_path,
            n_threads=8,
            n_ctx=4096,
            verbose=False
        )

    def summarize(self, text: str) -> str:
        prompt = f"Summarize the following text in one concise sentence:\n\n{text}"
        output = self.llm(prompt, max_tokens=100)
        return output["choices"][0]["text"].strip()
