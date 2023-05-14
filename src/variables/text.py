import pygame
from variables.config import *
from variables.constants import *


class Text:
    """Class for drawing text on the screen
    """
    def __init__(self, screen):
        """Constructor for the Text class
        
        Args:
            screen (pygame.Surface): The screen to draw the text on
        """
        self.screen = screen

    def game_over(self):
        font = pygame.font.Font('freesansbold.ttf', 100)
        text = font.render("Game Over", True, (RED))
        textRect = text.get_rect()
        textRect.center = (UI_WINDOW_WIDTH // 2, UI_WINDOW_HEIGHT // 2 - 100)
        self.screen.blit(text, textRect)
        pygame.display.update()