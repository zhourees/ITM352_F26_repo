# Read a file of quiz questions and save as a dictionary
# Name: Reesa Zhou
# Date: October 23, 2026

import json

fileName = "quizQuestions.json"

with open(fileName, "r") as file:
    questions = json.load(file)

print(questions)
