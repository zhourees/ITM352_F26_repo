# Application to manage the web page
# Name: Reesa Zhou
# Date: November 13, 2026

from flask import Flask, render_template, request, redirect, url_for
import json
import random

score = 0
questionNumber = 0
questionsFile = open("quizQuestions.json", "r")
questions = json.load(questionsFile)

highScoreList = [0]

maxQuestions = len(questions)

app = Flask(__name__)

@app.route("/")
def index():
    global score, questionNumber, highScoreList
    score = 0
    questionNumber = 0
    return render_template("index.html")

@app.route("/quiz", methods=["GET", "POST"])
def quiz():
    global score, questionNumber, maxQuestions, questions, highScoreList

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
        return render_template("result.html", score=score, maxQuestions=maxQuestions, highScore=highScore)

@app.route("/result")
def result():
    global score, maxQuestions, highScoreList

    highScoreList.append(score)
    highScoreList.sort()
    highScore = highScoreList[-1]

    return render_template("result.html", score=score, maxQuestions=maxQuestions, highScore=highScore)

def main():
    app.run(debug=True)

if __name__ == "__main__":
    main()
