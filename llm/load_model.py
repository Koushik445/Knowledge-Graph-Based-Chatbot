from llama_cpp import Llama

MODEL_PATH = "models/mistral-7b-instruct.gguf"

llm = Llama(
    model_path=MODEL_PATH,
    n_ctx=2048,
    n_threads=6,
    verbose=False
)

def generate_answer(prompt: str) -> str:
    output = llm(
        prompt,
        max_tokens=300,
        temperature=0.2,
        stop=["User:"]
    )
    return output["choices"][0]["text"].strip()
