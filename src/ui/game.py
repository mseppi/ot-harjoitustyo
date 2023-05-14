import pygame
from services.piece import Pieces
from variables.config import *
from variables.constants import *
from services.grid import Grid
from services.scores import *
from ui.add_score import add_score
        
def final(screen):
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


    while timer <1000:
        font = pygame.font.Font('freesansbold.ttf', 100)
        text = font.render("Game Over", True, (RED))
        textRect = text.get_rect()
        textRect.center = (UI_WINDOW_WIDTH // 2, UI_WINDOW_HEIGHT // 2 - 100)
        screen.blit(text, textRect)
        pygame.display.update()
        timer += clock.tick(10)

    if is_score_highscore(game.score):
        add_score(game.score, screen)
        
    
