from rag.router import QueryRouter

router = QueryRouter()

queries = [
    "Which ideas use AI?",
    "Show ideas related to vegetation issues",
    "Ideas that improve reliability",
    "List all ideas"
]

for q in queries:
    print(f"\nQ: {q}")
    print(router.handle_query(q))
