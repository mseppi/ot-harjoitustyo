import unittest
from game_logic import *


class TestTetris(unittest.TestCase):
    def setUp(self):
        print("Set up succesful")

    def test_pieces_move_down(self):
        piece = Pieces()
        test_y = piece.y
        piece.down()
        assert piece.y > test_y
