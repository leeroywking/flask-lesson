from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello World!"


@app.route("/hype/<hype>")
def hype(hype):
    return f"<h1>You are the best {hype}</h1>"


@app.route("/parse_arguments")
def argument_parsing():
    args = request.args
    return args
