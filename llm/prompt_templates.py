def build_prompt(user_question: str, graph_results: list) -> str:
    """
    Builds a grounded prompt for the LLM using graph-retrieved results.
    The LLM is strictly instructed to answer only from the given context.
    """

    if not graph_results:
        context_text = "No data available."
    else:
        context_lines = []
        for idx, item in enumerate(graph_results, start=1):
            context_lines.append(f"{idx}. {item}")
        context_text = "\n".join(context_lines)

    prompt = f"""
You are a domain expert assistant for a power utilities innovation dataset.

IMPORTANT RULES (FOLLOW STRICTLY):
- Use ONLY the information provided in the context
- Do NOT use outside knowledge
- Do NOT assume or hallucinate missing details
- If the answer is not present in the context, say so clearly

Context:
{context_text}

User Question:
{user_question}

Answer (clear, concise, and based only on the context):
"""

    return prompt
