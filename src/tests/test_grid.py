import unittest
from services.grid import Grid

class TestGrid(unittest.TestCase):
    def setUp(self):
        print("Set up succesful")
    
    def test_grid_create(self):
        grid = Grid()
        assert grid.grid != []