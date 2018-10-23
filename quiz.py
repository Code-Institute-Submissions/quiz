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