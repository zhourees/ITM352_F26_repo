# 
# Name: Reesa Zhou
# Date: October 7, 2026

questions = {
    "What is the capital of France? ": ["Paris", "Foulousa", "Rice", "Antigonous"],
    "What is the captial of Germany? ": ["Berlin", "Mumlich", "Hamburg", "Frankfurt"],
    "The last supper was painted by which artist? ": ["Da Vinci", "Michelangeo", "Raphael", "Carneggie"]
}

for question, answers in questions.items():
    correctAnswer = answers[0]
    sortedAnswers = sorted(answers)
    for label, answer in enumerate(sortedAnswers, start=1):
        print(F"{label}. {answer}")

    answerLabel = int(input(F"{question}Please type in the answer number: "))
    answer = sortedAnswers[answerLabel - 1]

    if answer == correctAnswer:
        print("Correct!")
    else:
        print(F"Incorrect! The answer is {correctAnswer}.")
