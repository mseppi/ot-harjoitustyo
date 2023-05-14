import pygame
from variables.config import *
from variables.constants import *
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
                if event.key == pygame.K_RETURN and len(name) > 0:
                    process = False
                elif event.key == pygame.K_BACKSPACE:
                    name = name[:-1]
                elif event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
                    continue
                else:
                    name += event.unicode
    text.add_score_to_file(name, score)
    text = Text(screen)
    text.remove_lowest_score()
