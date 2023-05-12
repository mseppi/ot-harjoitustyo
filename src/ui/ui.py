import pygame
from services.piece import Pieces
from variables.config import *
from variables.constants import *
from services.grid import Grid
pygame.init()
screen = pygame.display.set_mode((UI_WINDOW_WIDTH, UI_WINDOW_HEIGHT))
pygame.display.set_caption("Tetris")

        
def final():
    clock = pygame.time.Clock()
    game = Grid()
    piece = Pieces()
    running = True
    counter = 0

    while running:
        counter += 1
        if counter >= 100:
            counter = 0
            piece.down()
        game = Grid()
        for event in pygame.event.get():
            piece.events(event)
            if event.type == pygame.QUIT:
                running = False
                break

        screen.fill((BLACK))
        game.draw_grid(screen)
        piece.draw(screen)
        pygame.display.update()
        clock.tick(FPS)
    pygame.quit()
