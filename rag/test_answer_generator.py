from rag.answer_generator import AnswerGenerator

ag = AnswerGenerator()

questions = [
    "Which ideas use AI?",
    "What ideas address vegetation interference?",
    "Which initiatives improve reliability?"
]

for q in questions:
    print("\nQ:", q)
    print("A:", ag.answer(q))
