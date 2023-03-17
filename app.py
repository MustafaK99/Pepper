import os

import openai
from flask import Flask, redirect, render_template, request, url_for
from flaskext.markdown import Markdown

app = Flask(__name__)
Markdown(app)
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

        mkd_text = response.choices[0].text
        return redirect(url_for("index", result=mkd_text))

    result = request.args.get("result")
    return render_template("index.html", result=result)

