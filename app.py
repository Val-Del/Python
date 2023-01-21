from flask import Flask, render_template, request, flash, jsonify
from FetchPostgres import get_pokemon
import json
app = Flask(__name__)
app.secret_key = "key"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/hello")
def hello():
    flash("Nom : ")
    return render_template("form.html")

@app.route("/greet", methods=["POST"])
def greet():
    flash('Salut '+ str(request.form['input_name']) +", ça va ?")
    return render_template("form.html")

@app.route("/pokemons", methods=["POST"])
def pokemons():
    pokemons_data = json.loads(get_pokemon())
    return render_template("index.html", pokemons=pokemons_data)