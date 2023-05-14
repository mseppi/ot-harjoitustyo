import pygame
from variables.config import *
from variables.constants import *
import os


class Text:
    """Class for drawing text on the screen and handling highscores
    """
    def __init__(self, screen):
        """Constructor for the Text class
        
        Args:
            screen (pygame.Surface): The screen to draw the text on
        """
        self.screen = screen
        self.font = pygame.font.Font('freesansbold.ttf', 32)
        dir = "/home/mseppi/ot-harjoitustyo/src"
        self.highscore_file = os.path.join(dir,"variables", "highscore.txt")
        self.highscore_list = []
        with open(self.highscore_file, "r")as f:
            for line in f:
                name, score = line.strip().split(",")
                self.highscore_list.append((name, int(score)))


    def game_over(self):
        font = pygame.font.Font('freesansbold.ttf', 100)
        text = font.render("Game Over", True, (RED))
        textRect = text.get_rect()
        textRect.center = (UI_WINDOW_WIDTH // 2, UI_WINDOW_HEIGHT // 2 - 100)
        self.screen.blit(text, textRect)
        pygame.display.update()

    

    def highscore(self):
        self.screen.fill((BLACK))
        text = self.font.render("Highscore", True, (255, 255, 255))
        textRect = text.get_rect()
        textRect.center = (UI_WINDOW_WIDTH // 2, UI_WINDOW_HEIGHT // 2 - 200)
        self.screen.blit(text, textRect)
        for i in range(len(self.highscore_list)):
            text = self.font.render(f"{i+1}. {self.highscore_list[i][0]}: {self.highscore_list[i][1]}", True, (255, 255, 255))
            textRect = text.get_rect()
            textRect.center = (UI_WINDOW_WIDTH // 2, UI_WINDOW_HEIGHT // 2 - 150 + 50*i)
            self.screen.blit(text, textRect)
        pygame.display.update()
    
    def remove_lowest_score(self):
        """Removes the lowest score from the highscore file

        Args:
            highscore_file (str): The path to the highscore file
        """
        highscore = sorted(self.highscore_list, key=lambda x: x[1], reverse=True)
        highscore = highscore[:10]
        with open(self.highscore_file, 'w') as file:
            for name, score in highscore:
                file.write(name + "," + str(score) + "\n")


    def add_score_to_file(self, name, score):
        """Adds a score to the highscore file

        Args:
            name (str): The name of the player
            score (int): The score of the player
        """
        with open(self.highscore_file, 'a') as file:
            file.write(name + "," + str(score) + "\n")
        print ("Score added to file")

    def is_score_highscore(self, score):
        """Checks if the score is a highscore

        Args:
            score (int): The score to be checked

        Returns:
            bool: True if the score is a highscore, False otherwise
        """
        with open(self.highscore_file, 'r') as file:
            for line in file:
                name, score_file = line.strip().split(",")
                self.highscore_list.append((name, int(score_file)))
            for i in self.highscore_list:
                if score > i[1]:
                    return True
        return False
    
    def main_menu(self):
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render("Press Enter to start", True, (255, 255, 255))
        textRect = text.get_rect()
        textRect.center = (UI_WINDOW_WIDTH // 2, UI_WINDOW_HEIGHT // 2)
        return text, textRect
    
    def add_score(self, name):
        prompt_text = self.font.render("Enter your name", True, (255, 255, 255))
        prompt_text_rect = prompt_text.get_rect(center=(UI_WINDOW_WIDTH // 2, UI_WINDOW_HEIGHT // 2 - 50))
        name_text = self.font.render(name, True, (255, 255, 255))
        name_text_rect = name_text.get_rect(center=(UI_WINDOW_WIDTH // 2, UI_WINDOW_HEIGHT // 2))
        return prompt_text, prompt_text_rect, name_text, name_text_rect