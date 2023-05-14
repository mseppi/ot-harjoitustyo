import pygame
from variables.config import *
from variables.constants import *
from services.text import Text
import os

def highscore(screen):
    """Displays the highscore screen

    Args:
        screen (pygame.Surface): The screen to display the highscore on
    """
    process = True
    
    while process:
        screen.fill((BLACK))
        highscore = Text(screen)
        highscore.highscore()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                process = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    process = False
                    break
                if event.key == pygame.K_ESCAPE:
                    process = False
                    break