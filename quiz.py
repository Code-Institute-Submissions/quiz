from collections import deque

"""
This module will be imported into run.py
"""

def write_to_file(filename, data):
    """
    Write to file
    """
    with open(filename, "a") as file:
        file.writelines(data)
        
def update_guess(username, guess):
    """
    Update guesses.txt with player's incorrect guesses
    """
    write_to_file("data/guesses.txt", "{0} - {1}\n".format(username, guess))
    
def update_score(username, score):
    """
    Update scores.txt with player's score
    """
    write_to_file("data/scores.txt", "{0} - {1}\n".format(username, score)) 
    
def load_file(filename):
    """
    Load files and return the data to variable
    """
    with open(filename, "r") as data:
        return [row for row in data if len(row.strip()) > 0]
        
def delete_player(username):
    """
    Removes player from players.txt and deletes
    their incorrect guesses from guesses.txt
    """
    with open("data/players.txt", "r+") as player_data:
        players = player_data.readlines()
        player_data.seek(0)
        for line in players:
            if line != username + "\n":
                player_data.write(line)
        player_data.truncate()
        player_data.close()
    
    with open("data/guesses.txt", "r+") as data:
        f = data.readlines()
        data.seek(0)
        for line in f:
            if username not in line:
                data.write(line)
        data.truncate()
        data.close()
        
def get_guesses():
    """
    Open guesses.txt and gets ten most recent incorrect answers 
    to display on page. Function uses deque to return last ten guesses.
    """
    guesses = load_file("data/guesses.txt")
    d_guesses = deque(guesses, 10)
    return d_guesses
    
def check_answer(question, player_guess):
    """
    Check player's guess - if correct, add 5 to their score
    and move onto the next exotic fruit image.
    """
    if player_guess in question["answer"]:
        return True
    else:
        return False
        
def get_scores(data):
    """
    Open scores.txt and retrieve the top ten highest scores
    """
    scores = []
    with open(data) as f:
        for line in f:
            # If statement fixes ValueError bug
            if ' - ' in line:
                name, score = line.split(' - ')
                score = int(score)
                scores.append((name, score))
    
    scores.sort(key=lambda s: s[1], reverse=True) 
    top_scores = scores[:10]
    return top_scores