import pygame
import os
from variables.config import *
from variables.constants import *
dir = "/home/mseppi/ot-harjoitustyo/src"
highscore_file = os.path.join(dir,"variables", "highscore.txt")

def is_score_highscore(score):
    """Checks if the score is a highscore

    Args:
        score (int): The score to be checked

    Returns:
        bool: True if the score is a highscore, False otherwise
    """
    highscore = []
    with open(highscore_file, 'r') as file:
        for line in file:
            name, score_file = line.strip().split(",")
            highscore.append((name, int(score_file)))
        for i in highscore:
            if score > i[1]:
                return True
    return False

def remove_lowest_score(highscore_file):
    """Removes the lowest score from the highscore file

    Args:
        highscore_file (str): The path to the highscore file
    """
    highscore = []
    with open(highscore_file, 'r') as file:
        for line in file:
            name, score = line.strip().split(",")
            highscore.append((name, int(score)))
    highscore = sorted(highscore, key=lambda x: x[1], reverse=True)
    highscore = highscore[:10]
    with open(highscore_file, 'w') as file:
        for name, score in highscore:
            file.write(name + "," + str(score) + "\n")