# Second version of the quiz game, interactive quiz system with list of questions and correct answers
# Name: Reesa Zhou
# Date: October 2, 2026

questions = [
    ("What is the capital of France? ", "Paris"),
    ("What is the captial of Germany? ", "Berlin"),
    ("The last supper was painted by which artist?" , "Da Vinci")
]

for question, correctAnswer in questions:
    answer = input(F"{question}")
    if answer == correctAnswer:
        print("Correct!")
    else:
        print(F"The answer is {correctAnswer}, not {answer}.")
    