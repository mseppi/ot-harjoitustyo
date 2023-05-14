import unittest
from services.grid import Grid
from variables.constants import FROZEN_BLOCKS

class TestGrid(unittest.TestCase):
    def setUp(self):
        print("Set up succesful")
        self.grid = Grid()
        FROZEN_BLOCKS.append((40, 40, 1))
        self.grid.score = 100
        screen = None
    
    def test_grid_create(self):
        assert self.grid.grid != []

    def test_create_grid(self):
        self.grid.create_grid()
        assert self.grid.grid[1][1] == 1
    
    def test_remove_rows(self):
        for i in range(0, 10):
            self.grid.grid[19][i] == (100, 100 , 100)
        self.grid.remove_rows()
        
                
        
    def test_check_level(self):
        self.grid.check_level()
        assert self.grid.level == 2

    def test_not_enough_points(self):
        self.grid.score = 0
        self.grid.check_level()
        assert self.grid.level == 1
