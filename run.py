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
    
# MAIN PAGE

@app.route("/<username>", methods=["GET", "POST"])
def player(username):
    data = []
    with open("data/fruits.json", "r") as json_data:
        data = json.load(json_data)
    question_id = 0
    score = 0
    
    # Restart button:
    """
    Deletes players from all active players and their incorrect guesses
    and redirects player to the home page
    """
    if request.method == "POST":
        if request.form["button"] == "restart":
                quiz.delete_player(username)
                return redirect("/")   
            
    # Submit button:
    """
    Adds and deletes scores and
    also updates incorrect guesses
    """
    if request.method == "POST":
        if request.form["button"] == "submit":
            question_id = int(request.form["question_id"])
            score = int(request.form["score"])
            player_guess = request.form["answer"].lower() 
            if quiz.check_answer(data[question_id], player_guess):
                question_id += 1
                score += 5
            else:
                quiz.update_guess(username, player_guess + "\n")
                score -= 5
                  
    # Skip button:
    """
    Take away 2 points from player's score
    and move onto the next image. 
    When last image is skipped,
    delete player's data and redirect
    to end.html
    """
    if request.method == "POST":
        if request.form["button"] == "skip":
            question_id = int(request.form["question_id"])
            score = int(request.form["score"])
            question_id += 1
            score -= 2
            
            if question_id > 14:
                quiz.update_score(username, score)
                quiz.delete_player(username)
                return redirect ("/highscores")
            
    """
    If last question is answered correctly,
    return highscores.html
    """
    if request.method == "POST":    
        if request.form["button"] == "submit":
            if question_id == 14 and player_guess == "tamarillo":
                quiz.update_score(username, score)
                quiz.delete_player(username)
                return redirect ("/highscores")
    
    d_guesses = quiz.get_guesses()
    return render_template("game.html", 
                            quiz_data=data, 
                            question_id=question_id, 
                            guesses=d_guesses, 
                            score=score, 
                            username=username)
                            
# END OF GAME / HIGHSCORES

@app.route("/highscores")
def highscores():
    top_scores = quiz.get_scores("data/scores.txt")
    return render_template("highscores.html", scores=top_scores)