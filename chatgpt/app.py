import os
import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")

MODEL = "gpt-3.5-turbo"


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        message = request.form["message"]
        response = openai.ChatCompletion.create(
            model=MODEL,
            messages=generate_message(message),
            temperature=0,
        )
        result = response["choices"][0]["message"]["content"]
        return redirect(url_for("index", result=result))

    result = request.args.get("result")
    return render_template("index.html", result=result)


def generate_message(message):
    return [
        {"role": "user", "content": message},
    ]
