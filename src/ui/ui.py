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
        game = Grid()
        print(game.grid)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    piece.left()
                    if piece.left_wall_collision() or piece.collision():
                        piece.right()
                elif event.key == pygame.K_RIGHT:
                    piece.right()
                    if piece.right_wall_collision() or piece.collision():
                        piece.left()
#                elif event.key == pygame.K_DOWN:
                    down_moving = True
                elif event.key == pygame.K_UP:
                    piece.rotate()
                    if piece.left_wall_collision():
                        piece.right()
                    if piece.right_wall_collision():
                        piece.left()
                    if piece.collision():
                        piece.reverse_rotate()
                elif event.key == pygame.K_SPACE:
                    piece.reverse_rotate()
                    if piece.left_wall_collision():
                        piece.right()
                    if piece.right_wall_collision():
                        piece.left()
                    if piece.collision():
                        piece.rotate()

        screen.fill((BLACK))
        game.draw_grid(screen)

        if piece.collision():
            piece.new_piece()
        piece.down()
        piece.draw(screen)
        pygame.display.update()
        clock.tick(FPS)

