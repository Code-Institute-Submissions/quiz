import os
import json
from flask import Flask, render_template, request, redirect, url_for
from collections import deque
import quiz

app = Flask(__name__)

# INDEX PAGE

@app.route("/", methods=["GET", "POST"])
def index():
 
    # Username POST request
    if request.method == "POST":
        quiz.write_to_file("data/players.txt", request.form["username"] + "\n")
        return redirect(request.form["username"])
    players = quiz.load_file("data/players.txt")
    return render_template("index.html", players=players)