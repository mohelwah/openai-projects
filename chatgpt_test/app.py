import os

import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")

MODEL = "gpt-3.5-turbo"

messages = [
    {"role": "user", "content": "write print statements in python"},
]



@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        message = request.form["message"]
        response = openai.ChatCompletion.create(
    model=MODEL,
    messages=generate_message(message),
    temperature=0,
)
        return redirect(url_for("index", result=response['choices'][0]['message']['content']))

    result = request.args.get("result")
    return render_template("index.html", result=result)

def generate_message(message):
    return [{"role": "user", "content": message},]
