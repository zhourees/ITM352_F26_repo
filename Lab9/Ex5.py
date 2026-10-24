# Take Assignment 1 quiz questions and turn them into a JSON file
# Name: Reesa Zhou
# Date: October 23, 2026

import json

questions = {
    "What is the capital of France? ": ["Paris", "Foulousa", "Rice", "Antigonous"],
    "What is the captial of Germany? ": ["Berlin", "Mumlich", "Hamburg", "Frankfurt"],
    "The last supper was painted by which artist? ": ["Da Vinci", "Michelangeo", "Raphael", "Carneggie"]
}

fileName = "quizQuestions.json"

with open(fileName, "w") as file:
    json.dump(questions, file, indent=2)

print(F"Quiz questions saved to {fileName}.")
