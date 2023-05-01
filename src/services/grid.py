import random
import pygame
from variables.config import WINDOW_HEIGHT, WINDOW_WIDTH, BSIZE
from variables.constants import *

class Grid:

    def __init__(self):
        self.grid = []
        self.rows = WINDOW_HEIGHT // BSIZE
        self.columns = WINDOW_WIDTH // BSIZE
        self.create_grid()

    def create_grid(self):
        for row in range(self.rows):
            self.grid.append([])
            for _column in range(self.columns):
                self.grid[row].append(0)

    def draw(self, screen):
        for row in range(self.rows):
            pygame.draw.line(screen, (GRAY), (0, row * BSIZE),
                             (WINDOW_WIDTH, row * BSIZE))
        for column in range(self.columns):
            pygame.draw.line(screen, (GRAY), (column * BSIZE, 0),
                             (column * BSIZE, WINDOW_HEIGHT))

    def draw_frozen_blocks(self, screen):
        for block in frozen_blocks:
            pygame.draw.rect(screen, (block[2]), (block[0], block[1], BSIZE, BSIZE))

    def check_rows(self):
        for row in range(self.rows):
            if 0 not in self.grid[row]:
                self.grid.pop(row)
                self.grid.insert(0, [0 for _ in range(self.columns)])

    def draw_grid(self, screen):
        self.draw(screen)
        self.draw_frozen_blocks(screen)
        self.check_rows()