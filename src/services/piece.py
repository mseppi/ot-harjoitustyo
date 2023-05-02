import random
import pygame
from variables.config import WINDOW_HEIGHT, WINDOW_WIDTH, BSIZE
from variables.constants import frozen_blocks, shapes, shape_colors


class Pieces:
    """Class for the pieces that fall down
    """
    def __init__(self):
        """Constructor for the Pieces class
        """
        shape_id = random.randrange(len(shapes))
        self.shape = shapes[shape_id]
        self.color = shape_colors[shape_id]
        self.x_value = WINDOW_WIDTH // 2 - len(self.shape[0]) // 2
        self.y_value = 0 - BSIZE * 5

    def draw(self, screen):
        """Draws the piece on the screen

        Args:
            screen (pygame.Surface): The screen to draw the piece on
        """
        for row_index, row in enumerate(self.shape):
            for column_index, value in enumerate(row):
                if value != 0:
                    x_value = self.x_value + column_index * BSIZE
                    y_value = self.y_value + row_index * BSIZE
                    pygame.draw.rect(screen, self.color, (x_value, y_value, BSIZE, BSIZE))

    def rotate(self):
        """Rotates the piece
        """
        self.shape = list(zip(*self.shape[::-1]))

    def reverse_rotate(self):
        """Reverses the rotation of the piece
        """
        self.shape = list(zip(*self.shape))[::-1]

    def down(self):
        """Moves the piece down
        """
        self.y_value += BSIZE

    def left(self):
        """Moves the piece left
        """
        self.x_value -= BSIZE

    def right(self):
        """Moves the piece right
        """
        self.x_value += BSIZE

    def collision(self):
        """Checks if the piece collides with the bottom of the screen or with another piece

        Returns:
            bool: True if the piece collides, False otherwise
        """
        for row_index, row in enumerate(self.shape):
            for column_index, column in enumerate(row):
                if column != 0:
                    if self.y_value + row_index * BSIZE >= WINDOW_HEIGHT-BSIZE:
                        return True
                    for block in frozen_blocks:
                        if self.x_value + column_index * BSIZE == block[0] \
                                and self.y_value + row_index * BSIZE + BSIZE == block[1]:
                            return True
        return False

    def left_wall_collision(self):
        """Checks if the piece collides with the left wall

        Returns:
            bool: True if the piece collides, False otherwise
        """
        for _, row in enumerate(self.shape):
            for column_index, column in enumerate(row):
                if column != 0:
                    if self.x_value + column_index * BSIZE < 0-BSIZE:
                        return True
        return False

    def right_wall_collision(self):
        """Checks if the piece collides with the right wall

        Returns:
            bool: True if the piece collides, False otherwise
        """
        for _, row in enumerate(self.shape):
            for column_index, column in enumerate(row):
                if column != 0:
                    if self.x_value + column_index * BSIZE > WINDOW_WIDTH-BSIZE:
                        return True
        return False


    def wall_collision(self):
        """Checks if the piece collides with the left or right wall

        Returns:
            bool: True if the piece collides, False otherwise
        """
        return self.left_wall_collision() or self.right_wall_collision()

    def freeze(self):
        """Freezes the piece in place
        """
        for row_index, row in enumerate(self.shape):
            for column_index, column in enumerate(row):
                if column != 0:
                    x_value = self.x_value + column_index * BSIZE
                    y_value = self.y_value + row_index * BSIZE
                    frozen_blocks.append((x_value, y_value, self.color))

    def new_piece(self):
        """Creates a new piece and freezes the current one
        """
        self.freeze()
        self.__init__()
    