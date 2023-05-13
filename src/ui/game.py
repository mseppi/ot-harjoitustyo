import pygame
from services.piece import Pieces
from variables.config import *
from variables.constants import *
from services.grid import Grid

        
def final(screen):
    clock = pygame.time.Clock()
    game = Grid()
    piece = Pieces()
    running = True
    counter = 0

    while running:
        counter += 1
        if counter >= 100000:
            counter = 0
        if counter%(FPS // game.level // 2) == 0 or piece.downmoving:
            piece.down()
        for event in pygame.event.get():
            piece.events(event)
        if piece.game_over():
            running = False
            break
        

        screen.fill((BLACK))
        game.draw_grid(screen)
        piece.draw(screen)
        pygame.display.update()
        clock.tick(FPS)
        
    
