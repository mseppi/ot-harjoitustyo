import pygame
from game_logic import *
from config import FPS
pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Tetris")

def draw_game(screen):
    for row in range(WINDOW_HEIGHT // BSIZE):
        pygame.draw.line(screen, (WHITE), (0, row * BSIZE),
                         (WINDOW_WIDTH, row * BSIZE))
    for column in range(WINDOW_WIDTH // BSIZE):
        pygame.draw.line(screen, (WHITE), (column * BSIZE, 0),
                         (column * BSIZE, WINDOW_HEIGHT))
        
def final():
    clock = pygame.time.Clock()
    draw_game(screen)
    piece = Pieces()

    # Quitting game possible + moving
    left_moving = False
    right_moving = False
    down_moving = False

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
                elif event.key == pygame.K_DOWN:
                    down_moving = True
                elif event.key == pygame.K_UP:
                    piece.rotate()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    left_moving = False
                elif event.key == pygame.K_RIGHT:
                    right_moving = False
                elif event.key == pygame.K_DOWN:
                    down_moving = False

        screen.fill((0, 0, 0))
        draw_game(screen)

        if left_moving:
            piece.left()
        if right_moving:
            piece.right()
        if down_moving:
            piece.down()
        else:
            if not piece.collision():
                piece.down()
            else:
                piece.freeze()
                piece.new_piece()
        piece.down()
        piece.draw(screen)
        pygame.display.update()
        clock.tick(FPS)

