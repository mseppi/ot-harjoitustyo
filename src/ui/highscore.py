import pygame
from variables.config import *
from variables.constants import *
import os

def highscore(screen):
    """Displays the highscore screen

    Args:
        screen (pygame.Surface): The screen to display the highscore on
    """
    dir = "/home/mseppi/ot-harjoitustyo/src"
    highscore_file = os.path.join(dir, "variables", "highscore.txt")
    process = True
    highscore = []
    with open(highscore_file, "r")as f:
        for line in f:
            name, score = line.strip().split(",")
            highscore.append((name, int(score)))

    
    while process:
        screen.fill((BLACK))
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render("Highscore", True, (255, 255, 255))
        textRect = text.get_rect()
        textRect.center = (UI_WINDOW_WIDTH // 2, UI_WINDOW_HEIGHT // 2 - 200)
        screen.blit(text, textRect)
        for i in range(len(highscore)):
            text = font.render(f"{i+1}. {highscore[i][0]}: {highscore[i][1]}", True, (255, 255, 255))
            textRect = text.get_rect()
            textRect.center = (UI_WINDOW_WIDTH // 2, UI_WINDOW_HEIGHT // 2 - 150 + 50*i)
            screen.blit(text, textRect)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                process = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    process = False
                    break
                if event.key == pygame.K_ESCAPE:
                    process = False
                    break