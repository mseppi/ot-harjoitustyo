import pygame

pygame.init()

# Setup variables (may change later)
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 1000
FPS = 10
BSIZE = 20

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Tetris")

# Make blocks (rest of the blocks coming later)
T_BLOCK = [[1, 1, 1], [0, 1, 0]]

# Draw tetris pieces + movement
class Pieces:
    def __init__(self, shape, x, y):
        self.shape = shape
        self.x = x
        self.y = y

    def draw(self, screen):
        for row in range(len(self.shape)):
            for column in range(len(self.shape[0])):
                if self.shape[row][column]==1:
                    pygame.draw.rect(screen, (255, 255, 255), (self.x + column * BSIZE, self.y + row * BSIZE, BSIZE, BSIZE))
    
    def down(self):
        self.y += BSIZE

    def left(self):
        self.x -= BSIZE

    def right(self):
        self.x += BSIZE
    
# Draw game outlines
def draw_game(screen):
    for row in range(WINDOW_HEIGHT // BSIZE):
        pygame.draw.line(screen, (0, 0, 0), (0, row * BSIZE), (WINDOW_WIDTH, row * BSIZE))
    for column in range(WINDOW_WIDTH // BSIZE):
        pygame.draw.line(screen, (0, 0, 0), (column * BSIZE, 0), (column * BSIZE, WINDOW_HEIGHT))

#main function

def final():
    clock = pygame.time.Clock()
    
    piece=Pieces(T_BLOCK, WINDOW_WIDTH // 2 - BSIZE, 0)

    # Quitting game possible + moving
    left_moving = False
    right_moving = False
    down_moving = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    left_moving = True
                elif event.key == pygame.K_RIGHT:
                    right_moving = True
                elif event.key == pygame.K_DOWN:
                    down_moving = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    left_moving = False
                elif event.key == pygame.K_RIGHT:
                    right_moving = False
                elif event.key == pygame.K_DOWN:
                    down_moving = False
                    
                
                
        screen.fill((0, 0, 0))
        draw_game(screen)

        if left_moving:
            piece.left()
        if right_moving:
            piece.right()
        if down_moving:
            piece.down()
        
        piece.down()
        piece.draw(screen)
        pygame.display.update()
        clock.tick(FPS)
if __name__ == '__main__':
    final()