from rag.intent_parser import parse_intent
from rag.retriever import GraphRetriever


class QueryRouter:

    def __init__(self):
        self.retriever = GraphRetriever()

    def handle_query(self, user_query: str):
        parsed = parse_intent(user_query)
        intent = parsed["intent"]
        entity = parsed["entity"]

        if intent == "BY_TREND" and entity:
            return self.retriever.get_ideas_by_trend(entity)

        if intent == "BY_VALUE" and entity:
            return self.retriever.get_ideas_by_value_type(entity)

        if intent == "BY_PROBLEM" and entity:
            return self.retriever.get_ideas_by_problem(entity)

        return self.retriever.get_all_ideas()
