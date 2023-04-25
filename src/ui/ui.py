import pygame
from game_logic import *
from config import FPS
pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
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
                if event.key == pygame.K_LEFT:
                    left_moving = True
                elif event.key == pygame.K_RIGHT:
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

        screen.fill((0, 0, 0))
        game.draw_grid(screen)

        if left_moving:
            piece.left()
        if right_moving:
            piece.right()
#       if down_moving:
            piece.down()
        if piece.collision():
            piece.new_piece()
        piece.down()
        piece.draw(screen)
        pygame.display.update()
        clock.tick(FPS)

