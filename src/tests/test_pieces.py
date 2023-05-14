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
        for i in range(23):
            piece.down()
        assert piece.collision() == True

    def test_pieces_reverse_rotate(self):
        piece = Pieces()
        test_shape = piece.shape
        piece.reverse_rotate()
        assert piece.shape != test_shape

    def test_pieces_left_wall_collision(self):
        piece = Pieces()
        for i in range(10):
            piece.left()
        assert piece.left_wall_collision() == True

    def test_pieces_right_wall_collision(self):
        piece = Pieces()
        for i in range(10):
            piece.right()
        assert piece.right_wall_collision() == True
    
    def test_freeze(self):
        piece = Pieces()
        piece.freeze()
        assert frozen_blocks != []
        