# Create a skeleton for the quiz game
# Name: Reesa Zhou
# Date: November 12, 2026

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('quizHome.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        userid = request.form['username']
        password = request.form['password']
        # Replace this with your actual authentication logic
        if USERS.get(userid) == password:
            return redirect(url_for('quizStart', username=userid))
        else:
            return "Incorrect password. Try again."
    else:
        return render_template('quizLogin.html')

@app.route('/quizStart/<username>')
def quizStart(username):
    return render_template('quizStart.html', username=username)

USERS = {"zhourees": "strawberry",
        "reesazhou6": "blueberry"}


if __name__ == '__main__':
    app.run(debug=True, port=5001)
