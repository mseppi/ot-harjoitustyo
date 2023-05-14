import pygame
from variables.config import *
from variables.constants import *
from services.scores import highscore_file, remove_lowest_score
from variables.text import Text

def add_score(score, screen):
    """Adds a score to the highscore file

    Args:
        score (int): The score to be added
        screen (pygame.Surface): The Pygame surface object to display the input prompt
    """
    process = True
    text = Text(screen)
    name = ""
    while process:
        screen.fill((BLACK))
        prompt_text, prompt_text_rect, name_text, name_text_rect = text.add_score(name)
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
                    name += event.unicode
    with open(highscore_file, 'a') as file:
        file.write(name + "," + str(score) + "\n")
    remove_lowest_score()