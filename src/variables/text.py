import pygame
from variables.config import *
from variables.constants import *
import os


class Text:
    """Class for drawing text on the screen
    """
    def __init__(self, screen):
        """Constructor for the Text class
        
        Args:
            screen (pygame.Surface): The screen to draw the text on
        """
        self.screen = screen
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
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render("Highscore", True, (255, 255, 255))
        textRect = text.get_rect()
        textRect.center = (UI_WINDOW_WIDTH // 2, UI_WINDOW_HEIGHT // 2 - 200)
        self.screen.blit(text, textRect)
        for i in range(len(self.highscore_list)):
            text = font.render(f"{i+1}. {self.highscore_list[i][0]}: {self.highscore_list[i][1]}", True, (255, 255, 255))
            textRect = text.get_rect()
            textRect.center = (UI_WINDOW_WIDTH // 2, UI_WINDOW_HEIGHT // 2 - 150 + 50*i)
            self.screen.blit(text, textRect)
        pygame.display.update()