# Create a quiz with at least 5 questions, that tracks high scores
# Name: Reesa Zhou
# Date: October 11, 2026

import random
import json

# imported list of questions from questioons.json
questionsList = open("questions.json", "r")
questions = json.load(questionsList)

# create lables for the answers, create points to keep track of how many questions were answered correctly
# points helps track high scores
answerLabels = ["a", "b", "c", "d"]
points = 0
highScore = 0

# define function that allows user to restart the quiz by inputting yes or no
def retry():
    while True:
        answer = input("\nWould you like to try again? Yes/No: ").strip().casefold()
        if answer == "yes":
            return True
        if answer == "no":
            return False
        print("Invalid choice. Please enter yes or no.")

# start of the quiz, which is contained in a loop
# loop only triggers if the user inputs yes at the end
while True:
    points = 0
    # create number labels for the questions, sets correct answer to first answer of each question in questions.json file
    for num, (question, answer) in enumerate(questions.items(), start=1):
        correctAnswer = answer[0]
        print(F"\nQuestion {num}. {question}")

        # randomize order of answers per question
        randomAnswers = answer.copy()
        random.shuffle(randomAnswers)
        labeledAnswers = dict(zip(answerLabels, randomAnswers))

        # put labels (a, b, c, d) next to answers
        for label, answer in labeledAnswers.items():
            print(F"{label}. {answer}")

        # prompts user to try again if they input a letter that's not in the selection
        while True:
            userAnswer = input("\nPlease choose a letter: ").strip().lower()
            if userAnswer in labeledAnswers:
                break
            print("Invalid choice. Try again.")

        # locks in user's answer
        answer = labeledAnswers[userAnswer]

        # checks if user's answer was correct, and if not, provides the correct answer
        # adds a point to the number of questions answered correctly
        if answer == correctAnswer:
            print("\nCorrect!")
            points += 1
        else:
            print(F"\nIncorrect! The answer is '{correctAnswer}', not '{answer}'.")

    # prints the amount of questions answered correctly
    print(F"\nYou got {points} out of {len(questions)} questions correct.")

    # sets the high score to the current amount of questions answered correctly if it's higher than the previous score
    if points > highScore:
        highScore = points
        
    print(F"\nYour high score is {highScore}.")

    # prompts user to retry or quit the quiz, and doesn't allow other inputs besides yes and no
    if not retry():
        break