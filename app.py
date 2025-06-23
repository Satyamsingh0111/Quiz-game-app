def run_quiz(questions):
    score = 0
    for i, question in enumerate(questions, 1):
        print(f"\nQuestion {i}: {question['question']}")
        for option in question['options']:
            print(option)
        answer = input("Your answer (A, B, C, D): ").strip().upper()

        if answer == question['answer']:
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Wrong! The correct answer was {question['answer']}")
    print(f"\n🎉 Quiz finished! You got {score} out of {len(questions)} correct.")


# Sample questions
quiz_questions = [
    {
        "question": "What is the capital of France?",
        "options": ["A. Paris", "B. Rome", "C. Berlin", "D. Madrid"],
        "answer": "A"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A. Earth", "B. Venus", "C. Mars", "D. Jupiter"],
        "answer": "C"
    },
    {
        "question": "What is the largest mammal?",
        "options": ["A. Elephant", "B. Blue Whale", "C. Giraffe", "D. Hippopotamus"],
        "answer": "B"
    }
]

# Run the quiz
run_quiz(quiz_questions)
