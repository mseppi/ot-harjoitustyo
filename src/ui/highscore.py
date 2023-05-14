import pygame
import sys
import os
from variables.config import *
from variables.constants import *
from text.text import Text


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
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    process = False
                    break
                if event.key == pygame.K_ESCAPE:
                    process = False
                    break