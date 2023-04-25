import unittest
from game_logic import *


class TestPieces(unittest.TestCase):
    def setUp(self):
        print("Set up succesful")

    def test_pieces_move_down(self):
        piece = Pieces()
        test_y = piece.y
        piece.down()
        assert piece.y > test_y

    def test_pieces_move_left(self):
        piece = Pieces()
        test_x = piece.x
        piece.left()
        assert piece.x < test_x

    def test_pieces_move_right(self):
        piece = Pieces()
        test_x = piece.x
        piece.right()
        assert piece.x > test_x

    def test_pieces_rotate(self):
        piece = Pieces()
        test_shape = piece.shape
        piece.rotate()
        assert piece.shape != test_shape
