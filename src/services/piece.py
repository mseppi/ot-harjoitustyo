import random
import pygame
import sys
from variables.config import WINDOW_HEIGHT, WINDOW_WIDTH, BSIZE
from variables.constants import FROZEN_BLOCKS, shapes, shape_colors



class Pieces:
    """Class for the pieces that fall down
    """
    def __init__(self, piece=random.randint(0, len(shapes)-1)):
        """Constructor for the Pieces class
        """
        self.shape = shapes[piece]
        self.color = shape_colors[piece]
        self.x_value = (WINDOW_WIDTH // 2 - len(self.shape[0]) // 2)+2
        self.y_value = 0-BSIZE*2
        self.downmoving = False
        self.next_shape = random.randint(0, len(shapes)-1)

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

    def draw_next_piece(self, screen):
        """Draws the next piece on the screen

        Args:
            screen (pygame.Surface): The screen to draw the piece on
        """
        for row_index, row in enumerate(shapes[self.next_shape]):
            for column_index, value in enumerate(row):
                if value != 0:
                    x_value = 500 + column_index * BSIZE
                    y_value = 150 + row_index * BSIZE
                    pygame.draw.rect(screen, shape_colors[self.next_shape], \
                                     (x_value, y_value, BSIZE, BSIZE))
        screen.blit(pygame.font.SysFont('comicsans', 30).render('Next piece:', \
                                            True, (255, 255, 255)), (500, 100))

    def rotate(self):
        """Rotates the piece
        """
        self.shape = list(zip(*self.shape[::-1]))
        if self.collision():
            self.reverse_rotate()

    def reverse_rotate(self):
        """Reverses the rotation of the piece
        """
        self.shape = list(zip(*self.shape))[::-1]
        if self.collision():
            self.rotate()

    def down(self):
        """Moves the piece down
        """
        self.y_value += BSIZE
        if self.collision():
            self.y_value -= BSIZE
            self.new_piece()

    def left(self):
        """Moves the piece left
        """
        self.x_value -= BSIZE
        if self.collision():
            self.x_value += BSIZE

    def right(self):
        """Moves the piece right
        """
        self.x_value += BSIZE
        if self.collision():
            self.x_value -= BSIZE

    def space(self):
        """Moves the piece down until it collides
        """
        while not self.collision():
            self.y_value += BSIZE
        self.y_value -= BSIZE
        self.new_piece()

    def collision(self):
        """Checks if the piece collides with the bottom of the screen or with another piece

        Returns:
            bool: True if the piece collides, False otherwise
        """
        for row_index, row in enumerate(self.shape):
            for column_index, column in enumerate(row):
                if column != 0:
                    if self.y_value + row_index * BSIZE >= WINDOW_HEIGHT:
                        return True
                    for block in FROZEN_BLOCKS:
                        if block[0] == self.x_value + column_index * BSIZE and \
                            block[1] == self.y_value + row_index * BSIZE:
                            return True
                    if self.x_value + column_index * BSIZE < 0:
                        return True
                    if self.x_value + column_index * BSIZE >= WINDOW_WIDTH:
                        return True
        return False

    def freeze(self):
        """Freezes the piece in place
        """
        for row_index, row in enumerate(self.shape):
            for column_index, column in enumerate(row):
                if column != 0:
                    x_value = self.x_value + column_index * BSIZE
                    y_value = self.y_value + row_index * BSIZE
                    FROZEN_BLOCKS.append([x_value, y_value, self.color])

    def new_piece(self):
        """Creates a new piece and freezes the current one
        """
        self.freeze()
        self.__init__(self.next_shape)

    def game_over(self):
        """Checks if the game is over

        Returns:
            bool: True if the game is over, False otherwise
        """
        for block in FROZEN_BLOCKS:
            if block[1] <= 0:
                return True
        return False

    def events(self, event):
        """Handles the events for the piece

        Args:
            event (pygame.event): The event to handle
        """
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.left()
            if event.key == pygame.K_RIGHT:
                self.right()
            if event.key == pygame.K_UP:
                self.rotate()
            if event.key == pygame.K_SPACE:
                self.space()
            if event.key == pygame.K_DOWN:
                self.downmoving = True
            if event.key == pygame.K_LCTRL:
                self.reverse_rotate()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                self.downmoving = False
    