import random
import pygame
from config import WINDOW_HEIGHT, WINDOW_WIDTH, BSIZE

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
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)

shape_colors = {
    0: PURPLE,
    1: YELLOW,
    2: GREEN,
    3: RED,
    4: CYAN,
    5: ORANGE,
    6: BLUE
}
frozen_blocks = []

class Pieces:
    def __init__(self):
        shape_id = random.randrange(len(shapes))
        self.shape = shapes[shape_id]
        self.color = shape_colors[shape_id]
        self.x_value = WINDOW_WIDTH // 2 - len(self.shape[0]) // 2
        self.y_value = 0

    def draw(self, screen):
        for row in range(len(self.shape)):
            for column in range(len(self.shape[0])):
                if self.shape[row][column] != 0:
                    pygame.draw.rect(screen, (self.color), (
                        self.x_value + column * BSIZE, self.y_value + row * BSIZE, BSIZE, BSIZE))

    def rotate(self):
        self.shape = list(zip(*self.shape[::-1]))

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
                    if self.y_value + row * BSIZE >= WINDOW_HEIGHT-BSIZE*5:
                        return True
                    if self.x_value + column * BSIZE < 0:
                        return True
                    if self.x_value + column * BSIZE >= WINDOW_WIDTH:
                        return True
        return False

    def freeze(self):
        for row in range(len(self.shape)):
            for column in range(len(self.shape[0])):
                if self.shape[row][column] != 0:
                    frozen_blocks.append(
                        (self.x_value + column * BSIZE, self.y_value + row * BSIZE, self.color))

    def new_piece(self):
        self.freeze()
        self.__init__()

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
