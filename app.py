from flask import Flask, request
import requests as rq
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


@app.route("/pokemon_butts/<pokemon_name>")
def poke_butts(pokemon_name):
    poke_data = rq.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}")
    parsed_pokedata = poke_data.json()
    img_url = parsed_pokedata["sprites"]["back_default"]
    return f"<img src='{img_url}' />"