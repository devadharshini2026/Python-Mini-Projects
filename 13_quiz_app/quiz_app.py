def quiz():
    questions = [
        {
            "question": "What is the capital of France?",
            "options": ["A. Paris", "B. London", "C. Rome", "D. Berlin"],
            "answer": "A"
        },
        {
            "question": "Which language is used for AI?",
            "options": ["A. Python", "B. C++", "C. HTML", "D. CSS"],
            "answer": "A"
        },
        {
            "question": "What is 5 + 7?",
            "options": ["A. 10", "B. 12", "C. 11", "D. 13"],
            "answer": "B"
        }
    ]

    score = 0

    print("=== Simple Quiz App ===\n")
    for idx, q in enumerate(questions, 1):
        print(f"Q{idx}: {q['question']}")
        for option in q["options"]:
            print(option)
        answer = input("Your answer (A/B/C/D): ").upper()
        if answer == q["answer"]:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! Correct answer: {q['answer']}\n")

    print(f"Quiz Finished! Your Score: {score}/{len(questions)}")
    input("Press Enter to exit...")

if __name__ == "__main__":
    quiz()
