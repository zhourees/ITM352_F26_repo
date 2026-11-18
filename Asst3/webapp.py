# Application to manage the web page
# Name: Reesa Zhou
# Date: November 13, 2026

from flask import Flask, render_template, request, redirect, url_for
import json
import random
import time
from pathlib import Path

score = 0
questionNumber = 0
with (Path(__file__).resolve().parent.parent / "quizQuestions.json").open() as questionsFile:
    questions = json.load(questionsFile)

highScore = 0
highScoreTimed = 0
highScoreList = [0]
highScoreListTimed = [0]

maxQuestions = len(questions)

app = Flask(__name__)

@app.route("/")
def index():
    global score, questionNumber, highScoreList, highScoreListTimed, highScore, highScoreTimed
    score = 0
    questionNumber = 0
    return render_template("index.html")

@app.route("/quiz", methods=["GET", "POST"])
def quiz():
    global score, questionNumber, maxQuestions, questions, highScoreList, highScoreListTimed, highScore, highScoreTimed

    if request.method == "POST":
        answer = request.form.get("answer")
        if answer == list(questions.values())[0+questionNumber][0]:
            score += 1
        questionNumber += 1

    if questionNumber < maxQuestions:
        listAnswers = list(questions.values())[0+questionNumber].copy()
        randomAnswers = random.sample(listAnswers, k=4)
        return render_template("quiz.html", question=list(questions.keys())[0+questionNumber], questionNumber=questionNumber, choices=randomAnswers)
    else:
        highScoreList.append(score)
        highScoreList.sort()
        highScore = highScoreList[-1]
        return render_template("result.html", score=score, maxQuestions=maxQuestions, highScore=highScore, highScoreTimed=highScoreTimed)

@app.route("/quizTimed", methods=["GET", "POST"])
def quizTimed():
    global score, questionNumber, maxQuestions, questions, highScoreList, highScoreListTimed, highScore, highScoreTimed

    if request.method == "POST":
        answer = request.form.get("answer")
        if answer == list(questions.values())[0+questionNumber][0]:
            score += 1
        questionNumber += 1

    if questionNumber < maxQuestions:
        listAnswers = list(questions.values())[0+questionNumber].copy()
        randomAnswers = random.sample(listAnswers, k=4)
        return render_template("quizTimed.html", question=list(questions.keys())[0+questionNumber], questionNumber=questionNumber, choices=randomAnswers)
    else:
        highScoreListTimed.append(score)
        highScoreListTimed.sort()
        highScoreTimed = highScoreListTimed[-1]
        return render_template("result.html", score=score, maxQuestions=maxQuestions, highScore=highScore, highScoreTimed=highScoreTimed)

@app.route("/result")
def result():
    global score, maxQuestions, highScoreList, highScoreListTimed, highScore, highScoreTimed

    highScoreList.append(score)
    highScoreList.sort()
    highScore = highScoreList[-1]

    highScoreListTimed.append(score)
    highScoreListTimed.sort()
    highScoreTimed = highScoreListTimed[-1]

    return render_template("result.html", score=score, maxQuestions=maxQuestions, highScore=highScore, highScoreTimed=highScoreTimed)

def main():
    app.run(debug=True)

if __name__ == "__main__":
    main()
