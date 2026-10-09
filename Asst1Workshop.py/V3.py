# 
# Name: Reesa Zhou
# Date: October 7, 2026

questions = {
    "What is the capital of France? ": ["Paris", "Foulousa", "Rice", "Antigonous"],
    "What is the captial of Germany? ": ["Berlin", "Mumlich", "Hamburg", "Frankfurt"],
    "The last supper was painted by which artist?": ["Da Vinci", "Michelangeo", "Raphael", "Carneggie"]
}

for question, answers in questions.items():
    correctAnswer = answers[0]
    for answer in answers:
        print(F"{answer}")

    answer = input(F"{question}")
    if answer == correctAnswer:
        print("Correct!")
    else:
        print(F"Incorrect! The answer is {correctAnswer}")
