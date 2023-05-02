import random
import pygame
from variables.config import WINDOW_HEIGHT, WINDOW_WIDTH, BSIZE
from variables.constants import *


class Pieces:
    def __init__(self):
        shape_id = random.randrange(len(shapes))
        self.shape = shapes[shape_id]
        self.color = shape_colors[shape_id]
        self.x_value = WINDOW_WIDTH // 2 - len(self.shape[0]) // 2
        self.y_value = 0 - BSIZE * 5

    def draw(self, screen):
        for row_index, row in enumerate(self.shape):
            for column_index, value in enumerate(row):
                if value != 0:
                    x_value = self.x_value + column_index * BSIZE
                    y_value = self.y_value + row_index * BSIZE
                    pygame.draw.rect(screen, self.color, (x_value, y_value, BSIZE, BSIZE))

    def rotate(self):
        self.shape = list(zip(*self.shape[::-1]))

    def reverse_rotate(self):
        self.shape = list(zip(*self.shape))[::-1]

    def down(self):
        self.y_value += BSIZE

    def left(self):
        self.x_value -= BSIZE

    def right(self):
        self.x_value += BSIZE

    def collision(self):
        for row in range(len(self.shape)):
            for column in range(len(self.shape[0])):
                if self.shape[row][column] != 0:
                    if self.y_value + row * BSIZE >= WINDOW_HEIGHT-BSIZE:
                        return True
                    for block in frozen_blocks:
                        if self.x_value + column * BSIZE == block[0] and self.y_value + row * BSIZE + BSIZE == block[1]:
                            return True
        return False
    
    def left_wall_collision(self):
        for row in range(len(self.shape)):
            for column in range(len(self.shape[0])):
                if self.shape[row][column] != 0:
                    if self.x_value + column * BSIZE < 0-BSIZE:
                        return True
        return False

    def right_wall_collision(self):
        for row in range(len(self.shape)):
            for column in range(len(self.shape[0])):
                if self.shape[row][column] != 0:
                    if self.x_value + column * BSIZE > WINDOW_WIDTH-BSIZE:
                        return True
        return False
    
    def wall_collision(self):
        return self.left_wall_collision() or self.right_wall_collision()
    
    def freeze(self):
        for row in range(len(self.shape)):
            for column in range(len(self.shape[0])):
                if self.shape[row][column] != 0:
                    frozen_blocks.append(
                        (self.x_value + column * BSIZE, self.y_value + row * BSIZE, self.color))

    def new_piece(self):
        self.freeze()
        self.__init__()
    