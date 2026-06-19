# Simple Quiz Program

questions = [
    {
        "q": "What is 2 + 2?",
        "opts": ["3", "4", "5", "6"],
        "ans": 1
    },
    {
        "q": "Which language is used for Python programming?",
        "opts": ["Python", "HTML", "CSS", "SQL"],
        "ans": 0
    },
    {
        "q": "How many days are there in a week?",
        "opts": ["5", "6", "7", "8"],
        "ans": 2
    },
    {
        "q": "What is the capital of India?",
        "opts": ["Mumbai", "Chennai", "Delhi", "Kolkata"],
        "ans": 2
    },
    {
        "q": "Which planet is known as the Red Planet?",
        "opts": ["Earth", "Mars", "Jupiter", "Venus"],
        "ans": 1
    }
]

score = 0
total = len(questions)

for i, question in enumerate(questions, start=1):
    print(f"\nQuestion {i}: {question['q']}")

    for j, option in enumerate(question["opts"], start=1):
        print(f"{j}. {option}")

    answer = int(input("Enter your answer (1-4): "))

    # Convert to 0-based index
    if answer - 1 == question["ans"]:
        print("Correct!")
        score += 1
    else:
        print("Wrong!")

# Calculate percentage
percentage = (score / total) * 100

print("\n----- Quiz Result -----")
print(f"Score: {score}/{total}")
print(f"Percentage: {percentage:.2f}%")

# Performance message
if percentage >= 80:
    print("Excellent!")
elif percentage >= 60:
    print("Good Job!")
elif percentage >= 40:
    print("Keep Practicing!")
else:
    print("Needs Improvement!")
