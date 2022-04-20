from os import name
from flask import Flask, render_template, template_rendered
import flask

app = Flask(__name__)

@app.route("/")
def espres():
    return render_template("deez.html")

if __name__ == "__main__":
    app.run()


