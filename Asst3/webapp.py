# Application to manage the web page
# Name: Reesa Zhou
# Date: November 13, 2026

from flask import Flask, render_template, request, redirect, url_for
import json
import random

# define variables, like score, high score, max questions
# open json file with questions on it

score = 0
questionNumber = 0

questionsFile = open("quizQuestions.json", "r")
questions = json.load(questionsFile)

highScore = 0
highScoreTimed = 0
highScoreList = [0]
highScoreListTimed = [0]

maxQuestions = len(questions)

# start of app

app = Flask(__name__)

# opens home/index page, user starts with a score and high score of 0

@app.route("/")
def index():
    global score, questionNumber, highScoreList, highScoreListTimed, highScore, highScoreTimed
    score = 0
    questionNumber = 0
    return render_template("index.html")

# starts quiz on normal mode, gets user input through form on quiz.html
# correct answers add to score and question number
# changes feedback status to alternate between green flashes and red flashes
# flashes change the color of the quiz box depending on if the user was right or wrong

@app.route("/quiz", methods=["GET", "POST"])
def quiz():
    global score, questionNumber, maxQuestions, questions, highScoreList, highScoreListTimed, highScore, highScoreTimed

    feedback = None
    if request.method == "POST":
        answer = request.form.get("answer")
        isCorrect = answer == list(questions.values())[0+questionNumber][0]
        if isCorrect:
            score += 1
        feedback = "correct" if isCorrect else "wrong"
        questionNumber += 1

# randomizes answer order for each question and each repeat

    if questionNumber < maxQuestions:
        listAnswers = list(questions.values())[0+questionNumber].copy()
        randomAnswers = random.sample(listAnswers, k=4)
        return render_template("quiz.html", question=list(questions.keys())[0+questionNumber], questionNumber=questionNumber, choices=randomAnswers, feedback=feedback)
    else:
        highScoreList.append(score)
        highScoreList.sort()
        highScore = highScoreList[-1]
        return render_template("result.html", score=score, maxQuestions=maxQuestions, highScore=highScore, highScoreTimed=highScoreTimed)

# starts the quiz on timed mode
# generally the same as normal mode quiz

@app.route("/quizTimed", methods=["GET", "POST"])
def quizTimed():
    global score, questionNumber, maxQuestions, questions, highScoreList, highScoreListTimed, highScore, highScoreTimed

    feedback = None
    if request.method == "POST":
        answer = request.form.get("answer")
        isCorrect = answer == list(questions.values())[0+questionNumber][0]
        if isCorrect:
            score += 1
        feedback = "correct" if isCorrect else "wrong"
        questionNumber += 1

    if questionNumber < maxQuestions:
        listAnswers = list(questions.values())[0+questionNumber].copy()
        randomAnswers = random.sample(listAnswers, k=4)
        return render_template("quizTimed.html", question=list(questions.keys())[0+questionNumber], questionNumber=questionNumber, choices=randomAnswers, feedback=feedback)
    else:
        highScoreListTimed.append(score)
        highScoreListTimed.sort()
        highScoreTimed = highScoreListTimed[-1]
        return render_template("result.html", score=score, maxQuestions=maxQuestions, highScore=highScore, highScoreTimed=highScoreTimed)

# displays results page that contains score, high score on normal mode, and high score on timed mode
# gives user the option to take the quiz again

@app.route("/result")
def result():
    global score, maxQuestions, highScoreList, highScoreListTimed, highScore, highScoreTimed

# adds score to a list and sorts the list from lowest to highest integer
# the highest integer is displayed as the high score

    highScoreList.append(score)
    highScoreList.sort()
    highScore = highScoreList[-1]

    highScoreListTimed.append(score)
    highScoreListTimed.sort()
    highScoreTimed = highScoreListTimed[-1]

    return render_template("result.html", score=score, maxQuestions=maxQuestions, highScore=highScore, highScoreTimed=highScoreTimed)

# run the quiz

def main():
    app.run(debug=True)

if __name__ == "__main__":
    main()
