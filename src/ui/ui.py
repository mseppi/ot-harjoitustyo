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

    # Quitting game possible + moving
    left_moving = False
    right_moving = False
    #down_moving = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and piece.x_value > 0:
                    left_moving = True
                elif event.key == pygame.K_RIGHT and piece.x_value < WINDOW_WIDTH - len(piece.shape[0]) * BSIZE:
                    right_moving = True
#                elif event.key == pygame.K_DOWN:
                    down_moving = True
                elif event.key == pygame.K_UP:
                    piece.rotate()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    left_moving = False
                elif event.key == pygame.K_RIGHT:
                    right_moving = False
#                elif event.key == pygame.K_DOWN:
                    down_moving = False

        screen.fill((BLACK))
        game.draw_grid(screen)

        if left_moving and not piece.wall_collision():
            piece.left()
        if right_moving and not piece.wall_collision():
            piece.right()
#       if down_moving:
            piece.down()
        if piece.collision():
            piece.new_piece()
        game.check_rows()
        piece.down()
        piece.draw(screen)
        pygame.display.update()
        clock.tick(FPS)

