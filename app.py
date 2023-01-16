from flask import Flask, render_template, request, flash
app = Flask(__name__)
app.secret_key = "key"


@app.route("/hello")
def index():
    flash("what's test")
    return render_template("index.html")

@app.route("/greet", methods=["POST"])
def greet():
    flash('hi '+ str(request.form['input_name']) +", psartek ?")
    return render_template("index.html")
