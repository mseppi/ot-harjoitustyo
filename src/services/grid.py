import pygame
from variables.config import WINDOW_HEIGHT, WINDOW_WIDTH, BSIZE
from variables.constants import frozen_blocks, GRAY, WHITE

class Grid:
    """Class for the grid
    """

    def __init__(self):
        """Constructor for the Grid class
        """
        self.rows = WINDOW_HEIGHT // BSIZE
        self.columns = WINDOW_WIDTH // BSIZE
        self.create_grid()
        self.score = 25
        self.level = 1
        self.digit = []
        global frozen_blocks

    def create_grid(self):
        """Creates the grid
        """
        global frozen_blocks
        self.grid = []
        for _ in range(self.rows):
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
            pygame.draw.rect(screen, block[2], (block[0], block[1], BSIZE, BSIZE))


    def remove_rows(self):
        """Removes the rows that are full
        """
        global frozen_blocks
        frozen_blocks_temp = []
        rows_removed = []
        for i in range(len(self.grid)-1, -1, -1):
            row = self.grid[i]
            if (0, 0, 0) not in row:
                for j in frozen_blocks:
                    if j[1] == i * BSIZE:
                        frozen_blocks_temp.append(j)
                rows_removed.append(i)
                
        inc = 1
        for i in frozen_blocks_temp:
            frozen_blocks.remove(i)
        for i in rows_removed:
            self.move_down(i, inc)
            inc += 1
        self.score += len(rows_removed)**2


    def move_down(self, row, inc):
        """Moves the rows above this row down

        Args:
            row (int): The row to move the blocks down from
        """
        global frozen_blocks
        for i in range(len(frozen_blocks)):
            if frozen_blocks[i][1] < (row + inc) * BSIZE:
                frozen_blocks[i] = (frozen_blocks[i][0], frozen_blocks[i][1] + BSIZE, frozen_blocks[i][2])


    def draw_score(self, screen):
        """Draws the score on the screen

        Args:
            screen (pygame.Surface): The screen to draw the score on
        """
        font = pygame.font.SysFont('comicsans', 30)
        label = font.render(f'Score: {self.score}', 1, (WHITE))
        screen.blit(label, (600, 700))

    def check_level(self):
        """Checks the level and increases it if necessary
        """
        if self.score // self.level >= 20:
            self.level += 1



    def draw_grid(self, screen):
        self.create_grid()
        self.draw(screen)
        self.draw_frozen_blocks(screen)
        self.remove_rows()
        self.draw_score(screen)
        self.check_level()

