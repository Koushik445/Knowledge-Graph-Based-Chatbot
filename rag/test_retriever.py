from rag.retriever import GraphRetriever

gr = GraphRetriever()

print("All ideas:")
print(gr.get_all_ideas()[:5])

print("\nIdeas using AI:")
print(gr.get_ideas_by_trend("AI"))

print("\nIdeas with Reliability value:")
print(gr.get_ideas_by_value_type("Reliability"))
