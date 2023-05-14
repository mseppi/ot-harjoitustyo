import os
import pygame
from variables.config import UI_WINDOW_HEIGHT, UI_WINDOW_WIDTH
from variables.constants import RED, BLACK, dir


class Text:
    """Class for drawing text on the screen and handling highscores
    """
    def __init__(self, screen):
        """Constructor for the Text class

        Args:
            screen (pygame.Surface): The screen to draw the text on
        """
        self.screen = screen
        self.font = pygame.font.Font('freesansbold.ttf', 32)
        self.highscore_file = os.path.join(dir, "highscore.txt")
        self.highscore_list = []
        with open(self.highscore_file, "r", encoding="utf8")as file:
            for line in file:
                name, score = line.strip().split(",")
                self.highscore_list.append((name, int(score)))


    def game_over(self):
        """Displays the game over screen
        """
        font = pygame.font.Font('freesansbold.ttf', 100)
        text = font.render("Game Over", True, (RED))
        text_rect = text.get_rect()
        text_rect.center = (UI_WINDOW_WIDTH // 2, UI_WINDOW_HEIGHT // 2 - 100)
        self.screen.blit(text, text_rect)
        pygame.display.update()


    def highscore(self):
        """Displays the highscore screen
        """
        self.screen.fill((BLACK))
        text = self.font.render("Highscore", True, (BLACK))
        textRect = text.get_rect()
        textRect.center = (UI_WINDOW_WIDTH // 2, UI_WINDOW_HEIGHT // 2 - 200)
        self.screen.blit(text, textRect)
        for i, highscore in enumerate(self.highscore_list):
            text = self.font.render(f"{i+1}. {highscore[0]}: {highscore[1]}", True, (255, 255, 255))
            textRect = text.get_rect()
            textRect.center = (UI_WINDOW_WIDTH // 2, UI_WINDOW_HEIGHT // 2 - 150 + 50*i)
            self.screen.blit(text, textRect)
        pygame.display.update()


    def remove_lowest_score(self):
        """Removes the lowest score from the highscore file

        Args:
            highscore_file (str): The path to the highscore file
        """
        highscore = sorted(self.highscore_list, key=lambda x: x[1], reverse=True)
        highscore = highscore[:10]
        with open(self.highscore_file, 'w', encoding="utf8") as file:
            for name, score in highscore:
                file.write(name + "," + str(score) + "\n")


    def add_score_to_file(self, name, score):
        """Adds a score to the highscore file

        Args:
            name (str): The name of the player
            score (int): The score of the player
        """
        with open(self.highscore_file, 'a', encoding="utf8") as file:
            file.write(name + "," + str(score) + "\n")


    def is_score_highscore(self, score):
        """Checks if the score is a highscore

        Args:
            score (int): The score to be checked

        Returns:
            bool: True if the score is a highscore, False otherwise
        """
        with open(self.highscore_file, 'r', encoding="utf8") as file:
            for line in file:
                name, score_file = line.strip().split(",")
                self.highscore_list.append((name, int(score_file)))
            if len(self.highscore_list) < 10:
                return True
            for i in self.highscore_list:
                if score > i[1]:
                    return True
        return False


    def main_menu(self):
        """Draws the main menu text on the screen

        Returns:
            pygame.Surface, pygame.Rect: The text and the rect of the text
        """
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render("Press Enter to start", True, (255, 255, 255))
        text_rect = text.get_rect()
        text_rect.center = (UI_WINDOW_WIDTH // 2, UI_WINDOW_HEIGHT // 2)
        return text, text_rect


    def add_score(self, name):
        """Draws the text for adding a score to the highscore file

        Args:
            name (str): The name of the player

        Returns:
            pygame.Surface, pygame.Rect, pygame.Surface, pygame.Rect:
            The text and the rect of the text
        """
        prompt_text = self.font.render("Enter your name", True, (255, 255, 255))
        prompt_text_rect = prompt_text.get_rect(center=\
                        (UI_WINDOW_WIDTH // 2, UI_WINDOW_HEIGHT // 2 - 50))
        name_text = self.font.render(name, True, (255, 255, 255))
        name_text_rect = name_text.get_rect(center=(UI_WINDOW_WIDTH // 2, UI_WINDOW_HEIGHT // 2))
        return prompt_text, prompt_text_rect, name_text, name_text_rect
