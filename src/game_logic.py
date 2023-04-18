import pygame
from config import *
import random

# Make blocks
shapes = [
    [[1, 1, 1],
     [0, 1, 0]],

    [[2, 2],
     [2, 2]],

    [[0, 3, 3],
     [3, 3, 0]],

    [[4, 4, 0],
     [0, 4, 4]],

    [[5, 5, 5, 5]],

    [[0, 0, 6],
     [6, 6, 6]],

    [[7, 7, 7],
     [0, 0, 7]]
]

#define colors
PURPLE = (148, 0, 211)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
CYAN = (0, 255, 255)
ORANGE = (255, 165, 0)
BLUE = (0, 0, 255)
colors = [PURPLE, YELLOW, GREEN, RED, CYAN, ORANGE, BLUE]

class Pieces:
    def __init__(self):
        shape = random.choice(shapes)
        color = colors[shapes.index(shape)]
        self.shape = shape
        self.color = color
        self.x = WINDOW_WIDTH // 2 - len(shape[0]) // 2
        self.y = 0


    def draw(self, screen):
        for row in range(len(self.shape)):
            for column in range(len(self.shape[0])):
                if self.shape[row][column] == 1:
                    pygame.draw.rect(screen, (255, 255, 255), (self.x +
                                     column * BSIZE, self.y + row * BSIZE, BSIZE, BSIZE))

    def rotate(self):
        self.shape = list(zip(*self.shape[::-1]))
    
    def down(self):
        self.y += BSIZE

    def left(self):
        self.x -= BSIZE

    def right(self):
        self.x += BSIZE