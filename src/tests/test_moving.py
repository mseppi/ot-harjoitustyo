import unittest
from services.piece import *


class TestPieces(unittest.TestCase):
    def setUp(self):
        print("Set up succesful")

    def test_pieces_move_down(self):
        piece = Pieces()
        test_y = piece.y_value
        piece.down()
        assert piece.y_value > test_y

    def test_pieces_move_left(self):
        piece = Pieces()
        test_x = piece.x_value
        piece.left()
        assert piece.x_value < test_x

    def test_pieces_move_right(self):
        piece = Pieces()
        test_x = piece.x_value
        piece.right()
        assert piece.x_value > test_x

    def test_pieces_rotate(self):
        piece = Pieces()
        test_shape = piece.shape
        piece.rotate()
        assert piece.shape != test_shape

    def test_pieces_collision(self):
        piece = Pieces()
        piece.y = WINDOW_HEIGHT - BSIZE
        for i in range(20):
            piece.down()
        assert piece.collision() == True
