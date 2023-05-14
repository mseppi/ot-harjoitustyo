import pygame
from variables.config import *
from variables.constants import *
from services.scores import highscore_file, remove_lowest_score

def add_score(score, screen):
    """Adds a score to the highscore file

    Args:
        score (int): The score to be added
        screen (pygame.Surface): The Pygame surface object to display the input prompt
    """
    process = True
    name = ""
    font = pygame.font.Font('freesansbold.ttf', 32)
    while process:
        screen.fill((BLACK))
        prompt_text = font.render("Enter your name", True, (255, 255, 255))
        prompt_text_rect = prompt_text.get_rect(center=(UI_WINDOW_WIDTH // 2, UI_WINDOW_HEIGHT // 2 - 50))
        name_text = font.render(name, True, (255, 255, 255))
        name_text_rect = name_text.get_rect(center=(UI_WINDOW_WIDTH // 2, UI_WINDOW_HEIGHT // 2))
        screen.blit(prompt_text, prompt_text_rect)
        screen.blit(name_text, name_text_rect)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                process = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    process = False
                elif event.key == pygame.K_BACKSPACE:
                    name = name[:-1]
                else:
                    if len(name) < 10:
                        name += event.unicode
    with open(highscore_file, 'a') as file:
        file.write(name + "," + str(score) + "\n")
    remove_lowest_score()