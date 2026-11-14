# Application to manage the web page
# Name:Reesa Zhou
# Date: November 13, 2026

from flask import Flask, render_template, request, redirect, url_for

score = 0
questionNumber = 0
questions = [
    {
        "question": "Guess which lyric belongs to 'ART' by Tyla:",
        "options": [
            "Can you snatch my soul from me?",
            "Dancing alone don't look right on me, yeah",
            "Everybody needs somebody, but I can't be a fool",
            "Fifty shades and hues, tailormade for you"
        ],
    },
    {
        "question": "Guess which lyric belongs to 'Radio' by Bershy:",
        "options": [
            "Do I really love you? Is it a reflex?",
            "Liked it best in Technicolor",
            "And oh, your arms made it hard for me to breath in",
            "God, you're a laser beam, you're all my teen dreams"
        ],
    },
]

maxQuestions = len(questions)

app = Flask(__name__)

@app.route("/")
def index():
    global score, questionNumber
    score = 0
    questionNumber = 0
    return render_template("index.html")

@app.route("/quiz", methods=["GET", "POST"])
def quiz():
    global score, questionNumber, maxQuestions, questions

    if request.method == "POST":
        answer = request.form.get("answer")

        if answer == questions[questionNumber]["options"][-1]:
            score += 1
        questionNumber += 1

    if questionNumber < maxQuestions:
        return render_template("quiz.html", question=questions[questionNumber]["question"], questionNumber=questionNumber, options=questions[questionNumber]["options"])
    else:
        return render_template("result.html", score=score, maxQuestions=maxQuestions)

@app.route("/result")
def result():
    global score, maxQuestions
    return  render_template("result.html", score=score, maxQuestions=maxQuestions)

def main():
    app.run(debug=True)

if __name__ == "__main__":
    main()
