from ui.main_menu import main_menu
import pygame
from variables.config import *
from ui.game import final
from ui.highscore import highscore

pygame.init()
screen = pygame.display.set_mode((UI_WINDOW_WIDTH, UI_WINDOW_HEIGHT))
pygame.display.set_caption("Tetris")

def main():
    main_menu(screen)
    final(screen)
    highscore(screen)

if __name__ == '__main__':
    main()
