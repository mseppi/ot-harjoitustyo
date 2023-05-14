import pygame
from services.piece import Pieces
from variables.config import *
from variables.constants import *
from text.text import Text
from services.grid import Grid
from ui.add_score import add_score
        
def final(screen):
    """The main game loop

    Args:
        screen (pygame.Surface): The screen to display the game on
    """
    
    clock = pygame.time.Clock()
    game = Grid()
    piece = Pieces()
    running = True
    counter = 0
    timer = 0

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
        piece.draw_next_piece(screen)
        game.draw_grid(screen)
        piece.draw(screen)
        pygame.display.update()
        clock.tick(FPS)

    text = Text(screen)
    while timer <1000:
        text.game_over()
        timer +=1


    if text.is_score_highscore(game.score) and game.score > 0:
        add_score(game.score, screen)
        
    
