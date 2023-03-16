import os

import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        code = request.form["code"]
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=f"{code}\n\nRead the code and generate a README.md for it in markdown format",
            temperature=1,
            max_tokens=64,
            top_p=1.0,
            frequency_penalty=2.0,
            presence_penalty=0.
        )
        return redirect(url_for("index", result=response.choices[0].text))

    result = request.args.get("result")
    return render_template("index.html", result=result)

