import pygame
import sys
from variables.config import UI_WINDOW_HEIGHT, UI_WINDOW_WIDTH
from ui.main_menu import main_menu
from ui.game import final
from ui.highscore import highscore


screen = pygame.display.set_mode((UI_WINDOW_WIDTH, UI_WINDOW_HEIGHT))
pygame.display.set_caption("Tetris")

def main():
    main_menu(screen)
    final(screen)
    highscore(screen)
    sys.exit()

if __name__ == '__main__':
    main()
