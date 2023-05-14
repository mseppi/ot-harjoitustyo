import pygame
import sys
from variables.config import *
from variables.constants import *
from ui.game import final
from ui.highscore import highscore
from text.text import Text



def main_menu(screen):
    """Displays the main menu and inits pygame

    Args:
        screen (pygame.Surface): The screen to display the menu on
    """
    pygame.init()
    process = True
    text = Text(screen)
    while process:
        screen.fill((BLACK))
        a, b = text.main_menu()
        screen.blit(a, b)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    process = False
                if event.key == pygame.K_h:
                    highscore(screen)