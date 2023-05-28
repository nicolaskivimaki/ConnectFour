from constants import *
import random

class AI_engine:

    def __init__(self, board):
        self.board = board
        self.piece = 2

    def is_game_over(self, board):
        # Check if the game has ended
        return self.board.check_win(1, board) or self.board.check_win(2, board) or len(self.get_valid_locations(board)) == 0

    def evaluate_window(self, window, piece):
        score = 0
        opponent_piece = 1

        if piece == 1:
            opponent_piece = 2
        if window.count(piece) == 4:
            score += 100
        elif window.count(piece) == 3 and window.count(0) == 1:
            score += 5
        elif window.count(piece) == 2 and window.count(0) == 2:
            score += 2
        if window.count(opponent_piece) == 3 and window.count(0) == 1:
            score -= 4

        return score

    def evaluate_position(self, board, piece):
        score = 0

        # Center
        center_array = [int(i) for i in list(board[:, COLUMN_COUNT//2])]
        center_count = center_array.count(piece)
        score += center_count * 3

        # Horizontal
        for r in range(ROW_COUNT):
            row_array = [int(i) for i in list(board[r,:])]
            for c in range(COLUMN_COUNT-3):
                window = row_array[c:c+4]
                score += self.evaluate_window(window, piece)

        # Vertical
        for c in range(COLUMN_COUNT):
            col_array = [int(i) for i in list(board[:,c])]
            for r in range(ROW_COUNT-3):
                window = col_array[r:r+4]
                score += self.evaluate_window(window, piece)

        # Positive diagonal
        for r in range(ROW_COUNT-3):
            for c in range(COLUMN_COUNT-3):
                window = [board[r+i][c+i] for i in range(4)]
                score += self.evaluate_window(window, piece)

        # Negative diagonal
        for r in range(ROW_COUNT-3):
            for c in range(COLUMN_COUNT-3):
                window = [board[r+3-i][c+i] for i in range(4)]
                score += self.evaluate_window(window, piece)

        return score

    def get_valid_locations(self, board):

        valid_locations = []
        for col in range(COLUMN_COUNT):
            if self.board.is_valid_location(col, board):
                valid_locations.append(col)
        return valid_locations

    def minimax(self, board, depth, max_player, alpha, beta):

        valid_locations = self.get_valid_locations(board)
        game_over = self.is_game_over(board)

        if depth == 0 or game_over:
            if game_over:
                if self.board.check_win(2, board):
                    return (None, INFINITY)
                elif self.board.check_win(1, board):
                    return (None, -INFINITY)
                else: # Game is over, no more valid moves
                    return (None, 0)
            else: # Depth is zero
                return (None, self.evaluate_position(board, 2))

        if max_player:
            max_score = -INFINITY
            column = random.choice(valid_locations)
            for col in valid_locations:
                row = self.board.get_next_open_row(col, board)
                board_copy = board.copy()
                self.board.drop_piece(row, col, 2, board_copy)
                new_score = self.minimax(board_copy, depth-1, False, alpha, beta)[1]
                if new_score > max_score:
                    max_score = new_score
                    column = col
                alpha = max(alpha, max_score)
                if alpha >= beta:
                    break
            return column, max_score

        else: # Minimizing player
            max_score = INFINITY
            column = random.choice(valid_locations)
            for col in valid_locations:
                row = self.board.get_next_open_row(col, board)
                board_copy = board.copy()
                self.board.drop_piece(row, col, 1, board_copy)
                new_score = self.minimax(board_copy, depth-1, True, alpha, beta)[1]
                if new_score < max_score:
                    max_score = new_score
                    column = col
                beta = min(beta, max_score)
                if alpha >= beta:
                    break
            return column, max_score

