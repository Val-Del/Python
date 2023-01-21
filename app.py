from flask import Flask, render_template, request, flash
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
    flash('hi '+ str(request.form['input_name']) +", psartek ?")
    return render_template("form.html")

