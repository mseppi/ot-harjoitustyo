import pygame
from config import *

class Pieces:
    def __init__(self, shape, x, y):
        self.shape = shape
        self.x = x
        self.y = y

    def draw(self, screen):
        for row in range(len(self.shape)):
            for column in range(len(self.shape[0])):
                if self.shape[row][column] == 1:
                    pygame.draw.rect(screen, (255, 255, 255), (self.x +
                                     column * BSIZE, self.y + row * BSIZE, BSIZE, BSIZE))

    def down(self):
        self.y += BSIZE

    def left(self):
        self.x -= BSIZE

    def right(self):
        self.x += BSIZE

# Draw game outlines


def draw_game(screen):
    for row in range(WINDOW_HEIGHT // BSIZE):
        pygame.draw.line(screen, (0, 0, 0), (0, row * BSIZE),
                         (WINDOW_WIDTH, row * BSIZE))
    for column in range(WINDOW_WIDTH // BSIZE):
        pygame.draw.line(screen, (0, 0, 0), (column * BSIZE, 0),
                         (column * BSIZE, WINDOW_HEIGHT))