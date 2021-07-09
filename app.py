from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello World!"


@app.route("/math/<hype>")
def hype(hype):
    return f"<h1>You are the best {hype}</h1>"
