import random

# Questions database
questions = [
    {
        "question": "What is the capital of Japan?",
        "options": ["1. Tokyo", "2. Osaka", "3. Kyoto", "4. Nagoya"],
        "answer": "1"
    },
    {
        "question": "Which language is used in Python?",
        "options": ["1. Japanese", "2. English", "3. Spanish", "4. French"],
        "answer": "2"
    },
    {
        "question": "What does CPU stand for?",
        "options": [
            "1. Central Process Unit",
            "2. Central Processing Unit",
            "3. Computer Personal Unit",
            "4. Control Processing Unit"
        ],
        "answer": "2"
    }
]

score = 0

print("🎮 Welcome to the Quiz Game!")
print("-----------------------------")

# Shuffle questions
random.shuffle(questions)

for q in questions:
    print("\n" + q["question"])
    for option in q["options"]:
        print(option)
    
    user_answer = input("Your answer (1-4): ")

    if user_answer == q["answer"]:
        print("✅ Correct!")
        score += 1
    else:
        print("❌ Wrong!")

print("\nGame Over!")
print(f"Your final score: {score}/{len(questions)}")