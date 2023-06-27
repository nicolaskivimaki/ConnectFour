import unittest
from AI_engine import AI_engine
from board import Board
from constants import *
import numpy as np

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

    def test_find_win_in_2(self):

        board = np.array([
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 1, 0, 0, 0],
            [0, 0, 2, 2, 0, 0, 0]
        ])

        # Winning move is found with depth 4 and score = infinity

        depth = 4
        best_move, score = self.ai.minimax(np.flip(board, 0), depth, True, -INFINITY, INFINITY)
        self.assertEqual(best_move, 1)
        self.assertEqual(score, INFINITY)

        # Winning move is not found with depth 1, score < infinity

        depth = 1
        best_move, score = self.ai.minimax(np.flip(board, 0), depth, True, -INFINITY, INFINITY)
        self.assertLess(score, INFINITY)

    def test_find_win_in_6(self):

        board = np.array([
            [1, 0, 0, 1, 1, 0, 0],
            [2, 0, 0, 2, 2, 0, 0],
            [1, 0, 0, 2, 1, 1, 0],
            [2, 0, 0, 2, 1, 2, 0],
            [1, 0, 0, 1, 2, 1, 0],
            [2, 0, 0, 2, 1, 2, 1]
        ])

        # Winning move is found with depth 7 and score = infinity

        depth = 7
        best_move, score = self.ai.minimax(np.flip(board, 0), depth, True, -INFINITY, INFINITY)
        self.assertEqual(best_move, 2)
        self.assertEqual(score, INFINITY)

        # Winning move is not found with depth 4, score < infinity

        depth = 4
        best_move, score = self.ai.minimax(np.flip(board, 0), depth, True, -INFINITY, INFINITY)
        self.assertLess(score, INFINITY)

    def test_defense_loss_in_1_move(self):

        """
        Test AI defense in situations where the opponent can win in one move 
        if we don't defend correctly. Because we have a certain loss 1 move ahead, 
        the AI should be able to defend at depth = 1.
        """

        # Test defense against imminent horizontal loss

        board = np.zeros((6, 7))
        board[0][2:5] = 1
        board[0][5:] = 2
        print(board)
        depth = 1
        best_move, score = self.ai.minimax(board, depth, True, -INFINITY, INFINITY)
        self.assertEqual(best_move, 1)

        # Test defense against imminent vertical loss

        self.board.board = np.array([
            [1, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0]
        ])

        col, score = self.ai.minimax(self.board.board, depth, True, -INFINITY, INFINITY)
        row = self.board.get_next_open_row(col)
        self.assertEqual(col, 0)

        # Test defense against imminent right diagonal loss

        self.board.board = np.array([
            [0, 0, 1, 1, 2, 1, 0],
            [0, 0, 2, 2, 1, 0, 0],
            [0, 0, 2, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0]
        ])

        col, score = self.ai.minimax(self.board.board, depth, True, -INFINITY, INFINITY)
        row = self.board.get_next_open_row(col)
        self.assertEqual(col, 2)

        # Test defense against imminent left diagonal loss

        self.board.board = np.array([
            [1, 2, 1, 1, 2, 1, 0],
            [0, 1, 2, 2, 1, 0, 0],
            [0, 0, 1, 2, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0]
        ])

        col, score = self.ai.minimax(self.board.board, depth, True, -INFINITY, INFINITY)
        row = self.board.get_next_open_row(col)
        self.assertEqual(col, 3)


    def test_minimax(self):
        # test initial board
        column, score = self.ai.minimax(self.board.board, 3, True, -INFINITY, INFINITY)
        self.assertIn(column, list(range(COLUMN_COUNT)))
        self.assertIsInstance(score, int)


if __name__ == '__main__':
    unittest.main()
