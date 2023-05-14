import unittest
from services.piece import *


class TestPieces(unittest.TestCase):
    def setUp(self):
        print("Set up succesful")
        self.piece = Pieces()

    def test_pieces_move_down_and_collision(self):
        for i in range(20):
            self.piece.down()
        assert self.piece.y_value == -80
        

    def test_pieces_move_left(self):
        test_value = self.piece.x_value
        self.piece.left()
        assert self.piece.x_value < test_value

    def test_pieces_move_right(self):
        test_value = self.piece.x_value
        self.piece.right()
        assert self.piece.x_value > test_value

    def test_pieces_rotate(self):
        test_shape = self.piece.shape
        self.piece.rotate()
        assert self.piece.shape != test_shape

    def test_pieces_collision(self):
        self.piece.y_value = 1000
        assert self.piece.collision() == True

    def test_pieces_wall_collision(self):
        self.piece.x_value = -1000
        assert self.piece.collision() == True
    
    def test_pieces_other_wall_collision(self):
        self.piece.x_value = 1000
        assert self.piece.collision() == True

    def test_pieces_through_wall(self):
        for i in range(20):
            self.piece.right()
        assert self.piece.x_value == 240

    def test_pieces_through_other_wall(self):
        for i in range(20):
            self.piece.left()
        assert self.piece.x_value == 0

    def test_pieces_reverse_rotate(self):
        test_shape = self.piece.shape
        self.piece.reverse_rotate()
        assert self.piece.shape != test_shape

    def test_space(self):
        self.piece.space()
        assert self.piece.y_value == -80

    def test_game_over(self):
        FROZEN_BLOCKS.append((40, -30, 1))
        self.piece.game_over()
        assert self.piece.game_over() == True

    def test_game_not_over(self):
        self.piece.game_over()
        assert self.piece.game_over() == False
        
    
        