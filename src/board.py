import numpy as np
from constants import *

class Board:
    def __init__(self, rows=ROW_COUNT, columns=COLUMN_COUNT):
        self.rows = rows
        self.columns = columns
        self.board = np.zeros((self.rows, self.columns))

    def drop_piece(self, row, col, piece, board=None):
        """
        Drop a piece into the board at the given location.
        """
        if board is not None:
            board[row][col] = piece
        else:
            self.board[row][col] = piece

    def is_valid_location(self, col, board=None):
        """
        Check if a drop is valid (i.e., within the bounds of the board and the chosen column is not full).
        """
        if board is not None:
            return board[self.rows-1][col] == 0
        return self.board[self.rows-1][col] == 0

    def get_next_open_row(self, col, board=None):
        """
        Given a column, find the next open row within that column.
        """
        if board is None:
            board = self.board

        for r in range(self.rows):
            if board[r][col] == 0:
                return r

    def check_win(self, piece, board=None):

        if board is None:
            board = self.board

        # Check horizontal windows
        for c in range(COLUMN_COUNT - 3):
            for r in range(ROW_COUNT):
                if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                    return True

        # Check vertical windows
        for c in range(COLUMN_COUNT):
            for r in range(ROW_COUNT - 3):
                if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                    return True

        # Check positive diagonal windows
        for c in range(COLUMN_COUNT - 3):
            for r in range(ROW_COUNT - 3):
                if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
                    return True

        # Check negative diagonal windows
        for c in range(COLUMN_COUNT - 3):
            for r in range(3, ROW_COUNT):
                if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
                    return True

        return False

    def reset_board(self):
        self.board = np.zeros((self.rows, self.columns))
