import pygame
from variables.config import *
from variables.constants import *
from ui.game import final
from ui.highscore import highscore



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
                    process = False
                if event.key == pygame.K_h:
                    highscore(screen)