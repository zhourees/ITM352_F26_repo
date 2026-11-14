# Create a simple application to retrieve memes
# Name: Reesa Zhou
# Date: November 12, 2026

from flask import Flask, request, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    response = requests.request("GET", "https://meme-api.com/gimme/wholesomememes")
    meme = response.json()
    return render_template("getMeme.html", image_url=meme["url"], subreddit=meme["subreddit"])

if __name__ == '__main__':
    app.run(debug=True)
