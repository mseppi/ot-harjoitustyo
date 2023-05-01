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