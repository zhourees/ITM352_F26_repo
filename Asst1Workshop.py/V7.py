# 
# Name: Reesa Zhou
# Date: October 9, 2026

from string import ascii_lowercase
import random
import json

question_file = open("questionsTest.json", "r")
questions = json.load(question_file)

NUM_QUESTIONS_PER_QUIZ = 5

def prepareQuestions(questions, numQuestions):
    numQuestions = min(NUM_QUESTIONS_PER_QUIZ, len(questions))
    return random.sample(list(questions.items()), k=numQuestions)

def getAnswer(question, alternatives):
    labeledAnswers = dict(zip(ascii_lowercase, alternatives))
    for label, answer in labeledAnswers.items():
            print(F"{label}. {answer}")

    while (answerLabel := input("\nChoice? ").lower()) not in labeledAnswers:
            print(F"\nInvalid choice. Please select one of {', '.join(labeledAnswers.keys())}")

    answer = labeledAnswers.get(answerLabel)
    return labeledAnswers[answerLabel]

def askQuestions(question, alternatives):
     correctAnswer = alternatives[0]
     orderedAlternatives = random.sample(alternatives, k=len(alternatives))
     answer = getAnswer(question, orderedAlternatives)
     if answer == correctAnswer:
           print("Correct!")
           return 1
     else:
           print(F"The answer is {correctAnswer}, not {answer}.")
           return 0
     
questions = prepareQuestions(questions, NUM_QUESTIONS_PER_QUIZ)

numCorrect = 0

for num, (question, answers) in enumerate(questions, start=1):
      print(F"\nQuestion {num}: {question}")
      numCorrect += askQuestions(question, answers)

print(F"\nYou got {numCorrect} out of {len(questions)} correct.")
