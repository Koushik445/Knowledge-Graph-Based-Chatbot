from rag.router import QueryRouter
from llm.load_model import generate_answer
from llm.prompt_templates import build_prompt


class AnswerGenerator:
    def __init__(self):
        self.router = QueryRouter()

    def answer(self, user_question: str) -> str:
        graph_results = self.router.handle_query(user_question)

        if not graph_results:
            return "No relevant information found in the dataset."

        prompt = build_prompt(user_question, graph_results)
        return generate_answer(prompt)
