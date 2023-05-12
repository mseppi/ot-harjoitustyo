from ui.ui import final, main_menu
import pygame
from variables.config import *
pygame.init()
screen = pygame.display.set_mode((UI_WINDOW_WIDTH, UI_WINDOW_HEIGHT))
pygame.display.set_caption("Tetris")

def main():
    main_menu(screen)

if __name__ == '__main__':
    main()
