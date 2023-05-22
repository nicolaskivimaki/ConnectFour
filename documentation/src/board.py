import numpy as np
from constants import *

class Board:
    def __init__(self, rows=ROW_COUNT, columns=COLUMN_COUNT):
        self.rows = rows
        self.columns = columns
        self.board = np.zeros((self.rows, self.columns))

    def drop_piece(self, row, col, piece):
        """
        Drop a piece into the board at the given location.
        """
        self.board[row][col] = piece

    def is_valid_location(self, col):
        """
        Check if a drop is valid (i.e., within the bounds of the board and the chosen column is not full).
        """
        return self.board[self.rows-1][col] == 0

    def get_next_open_row(self, col):
        """
        Given a column, find the next open row within that column.
        """
        for r in range(self.rows):
            if self.board[r][col] == 0:
                return r

    def print_board(self):
        """
        Print the board to the console (mainly for testing purposes).
        """
        print(np.flip(self.board, 0))
        
    def check_win(self, piece):
        """
        Check if the latest piece resulted in a win.
        """
        # Horizontal, vertical, and diagonal win conditions to be implemented.
        # return True if the game has been won, else False
