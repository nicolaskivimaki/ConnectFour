import unittest
from AI_engine import AI_engine
from board import Board
from constants import *

class TestAIEngine(unittest.TestCase):

    def setUp(self):
        self.board = Board()
        self.ai = AI_engine(self.board)

    def test_is_game_over(self):
        # test initial board
        self.assertEqual(self.ai.is_game_over(self.board.board), False)
        # test board with winning state for player 1
        self.board.board[0][:4] = 1
        self.assertEqual(self.ai.is_game_over(self.board.board), True)
        # test board with winning state for player 2
        self.board.board[0][:4] = 2
        self.assertEqual(self.ai.is_game_over(self.board.board), True)

    def test_evaluate_window(self):
        # test window with 4 pieces of player 1
        self.assertEqual(self.ai.evaluate_window([1, 1, 1, 1], 1), 100)
        # test window with 4 pieces of player 2
        self.assertEqual(self.ai.evaluate_window([2, 2, 2, 2], 2), 100)

    def test_evaluate_position(self):
        # test initial board
        self.assertEqual(self.ai.evaluate_position(self.board.board, 1), 0)
        # test board with winning state for player 1
        for i in range(2, 6):
            self.board.board[i][0] = 1 
            print(self.board.board)
        self.assertEqual(self.ai.evaluate_position(self.board.board, 1), 107)
        # test board with winning state for player 2
        for i in range(2, 6):
            self.board.board[i][0] = 2 
            print(self.board.board)
        self.assertEqual(self.ai.evaluate_position(self.board.board, 2), 107)

    def test_get_valid_locations(self):
        # test initial board
        self.assertEqual(self.ai.get_valid_locations(self.board.board), list(range(COLUMN_COUNT)))
        # test full column
        self.board.board[:, 0] = 1
        self.assertEqual(self.ai.get_valid_locations(self.board.board), list(range(1, COLUMN_COUNT)))

    def test_minimax(self):
        # test initial board
        column, score = self.ai.minimax(self.board.board, 3, True, -INFINITY, INFINITY)
        self.assertIn(column, list(range(COLUMN_COUNT)))
        self.assertIsInstance(score, int)


if __name__ == '__main__':
    unittest.main()
