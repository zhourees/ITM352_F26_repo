# 
# Name: Reesa Zhou
# Date: October 7, 2026

from string import ascii_lowercase
import random

questions = {
    "What is the capital of France? ": ["Paris", "Foulousa", "Rice", "Antigonous"],
    "What is the captial of Germany? ": ["Berlin", "Mumlich", "Hamburg", "Frankfurt"],
    "The last supper was painted by which artist? ": ["Da Vinci", "Michelangeo", "Raphael", "Carneggie"]
}

NUM_QUESTIONS_PER_QUIZ = 5
numQuestions = min(NUM_QUESTIONS_PER_QUIZ, len(questions))
selectedQuestions = random.sample(list(questions.items()), k=numQuestions)
numCorrect = 0

for num, (question, answers) in enumerate(questions.items(), start=1):
    correctAnswer = answers[0]
    print(F"\nQuestion {num}: {question}")

    sortedAnswers = sorted(answers)
    labeledAnswers = dict(zip(ascii_lowercase, random.sample(sortedAnswers, k=len(sortedAnswers))))
    for label, answer in labeledAnswers.items():
        print(F"{label}. {answer}")

    while (answerLabel := input("\nChoice? ").lower()) not in labeledAnswers:
        print(F"\nInvalid choice. Please select one of {', '.join(labeledAnswers.keys())}")
        
    answer = labeledAnswers.get(answerLabel)

    if answer == correctAnswer:
        print("\nCorrect!")
        numCorrect += 1
    else:
        print(F"\nIncorrect! The answer is {correctAnswer}, not {answer}.")

print(F"\nYou got {numCorrect} out of {len(questions)} correct.")
