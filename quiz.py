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