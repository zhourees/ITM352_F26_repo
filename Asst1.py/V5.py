# 
# Name: Reesa Zhou
# Date: October 7, 2026

from string import ascii_lowercase

questions = {
    "What is the capital of France? ": ["Paris", "Foulousa", "Rice", "Antigonous"],
    "What is the captial of Germany? ": ["Berlin", "Mumlich", "Hamburg", "Frankfurt"],
    "The last supper was painted by which artist? ": ["Da Vinci", "Michelangeo", "Raphael", "Carneggie"]
}

numCorrect = 0

for num, (question, answers) in enumerate(questions.items(), start=1):
    correctAnswer = answers[0]
    print(F"\nQuestion {num}: {question}")

    sortedAnswers = sorted(answers)
    labeledAnswers = dict(zip(ascii_lowercase, sortedAnswers))
    for label, answer in labeledAnswers.items():
        print(F"{label}. {answer}")

    answerLabel = input("Choice? ").lower()
    answer = labeledAnswers.get(answerLabel)

    if answer == correctAnswer:
        print("\nCorrect!")
        numCorrect += 1
    else:
        print(F"\nIncorrect! The answer is {correctAnswer}, not {answer}.")

print(F"\nYou got {numCorrect} out of {len(questions)} correct.")
