import random
import pygame
from variables.config import WINDOW_HEIGHT, WINDOW_WIDTH, BSIZE
from variables.constants import *

class Grid:
    """Class for the grid
    """

    def __init__(self):
        """Constructor for the Grid class
        """
        self.grid = []
        self.rows = WINDOW_HEIGHT // BSIZE
        self.columns = WINDOW_WIDTH // BSIZE
        self.create_grid()
        self.score = 0

    def create_grid(self):
        """Creates the grid
        """
        for row in range(self.rows):
            self.grid.append([(0, 0, 0) for _column in range(self.columns)])
        for block in frozen_blocks:
            self.grid[block[1] // BSIZE][block[0] // BSIZE] = block[2]

    def draw(self, screen):
        """Draws the grid on the screen

        Args:
            screen (pygame.Surface): The screen to draw the grid on
        """
        for row in range(self.rows+1):
            pygame.draw.line(screen, (GRAY), (0, row * BSIZE),
                             (WINDOW_WIDTH, row * BSIZE))
        for column in range(self.columns+1):
            pygame.draw.line(screen, (GRAY), (column * BSIZE, 0),
                             (column * BSIZE, WINDOW_HEIGHT))

    def draw_frozen_blocks(self, screen):
        """Draws the frozen blocks on the screen

        Args:
            screen (pygame.Surface): The screen to draw the frozen blocks on
        """
        for block in frozen_blocks:
            pygame.draw.rect(screen, (block[2]), (block[0], block[1], BSIZE, BSIZE))

    def check_rows(self):
        """Checks if a row is full
        """
        inc = 0
        for row in self.grid:
            if (0, 0, 0) not in row:
                self.grid.pop(inc)
                self.grid.insert(0, [(0, 0, 0) for _column in range(self.columns)])
                self.score += 10
    
    def draw_score(self, screen):
        """Draws the score on the screen
        
        Args:
            screen (pygame.Surface): The screen to draw the score on
        """
        font = pygame.font.SysFont('comicsans', 30)
        label = font.render(f'Score: {self.score}', 1, (WHITE))
        screen.blit(label, (600, 700))

    def draw_grid(self, screen):
        """Draws the grid on the screen

        Args:
            screen (pygame.Surface): The screen to draw the grid on
        """
        self.draw(screen)
        self.draw_frozen_blocks(screen)
        self.check_rows()
        self.draw_score(screen)