import pygame
from config import *

# Make blocks (rest of the blocks coming later)
T_BLOCK = [[1, 1, 1], [0, 1, 0]]

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