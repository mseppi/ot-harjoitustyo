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
        game = Grid()
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
        
def main_menu(screen):
    process = True
    while process:
        screen.fill((BLACK))
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render("Press Enter to start", True, (255, 255, 255))
        textRect = text.get_rect()
        textRect.center = (UI_WINDOW_WIDTH // 2, UI_WINDOW_HEIGHT // 2)
        screen.blit(text, textRect)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                process = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    final(screen)
    

pygame.quit()
