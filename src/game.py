import pygame 
from constants import *
import sys
import math

class Game:
    def __init__(self, board):
        self.board = board
        pygame.init()
        self.width = COLUMN_COUNT * SQUARESIZE
        self.height = (ROW_COUNT+1) * SQUARESIZE
        size = (self.width, self.height)
        self.screen = pygame.display.set_mode(size)
        self.game_over = False
        self.turn = 0

    def draw_board(self):
        for c in range(COLUMN_COUNT):
            for r in range(ROW_COUNT):
                pygame.draw.rect(self.screen, BLUE, (c*SQUARESIZE, r*SQUARESIZE+SQUARESIZE, SQUARESIZE, SQUARESIZE))
                pygame.draw.circle(self.screen, BLACK, (int(c*SQUARESIZE+SQUARESIZE/2), int(r*SQUARESIZE+SQUARESIZE+SQUARESIZE/2)), RADIUS)
            
        for c in range(COLUMN_COUNT):
            for r in range(ROW_COUNT):        
                if self.board.board[r][c] == 1:
                    pygame.draw.circle(self.screen, RED, (int(c*SQUARESIZE+SQUARESIZE/2), self.height-int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS)
                elif self.board.board[r][c] == 2: 
                    pygame.draw.circle(self.screen, YELLOW, (int(c*SQUARESIZE+SQUARESIZE/2), self.height-int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS)
        pygame.display.update()

    def is_valid_location(self, col):
        return self.board.board[ROW_COUNT-1][col] == 0

    def get_next_open_row(self, col):
        for r in range(ROW_COUNT):
            if self.board.board[r][col] == 0:
                return r

    def check_win(self, piece):
        # Check for win logic
        # Returns True if piece has won, False otherwise
        pass

    def run(self):
        self.draw_board()

        while not self.game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEMOTION:
                    pygame.draw.rect(self.screen, BLACK, (0,0, self.width, SQUARESIZE))
                    posx = event.pos[0]
                    if self.turn == 0:
                        pygame.draw.circle(self.screen, RED, (posx, int(SQUARESIZE/2)), RADIUS)
                    else: 
                        pygame.draw.circle(self.screen, YELLOW, (posx, int(SQUARESIZE/2)), RADIUS)
                    pygame.display.update()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    pygame.draw.rect(self.screen, BLACK, (0,0, self.width, SQUARESIZE))

                    # Player 1 Input
                    if self.turn == 0:
                        posx = event.pos[0]
                        col = int(math.floor(posx/SQUARESIZE))

                        if self.is_valid_location(col):
                            row = self.get_next_open_row(col)
                            self.board.drop_piece(row, col, 1)

                            if self.check_win(1):
                                print("Player 1 wins!!")
                                self.game_over = True

                    # Player 2 Input
                    else:                
                        posx = event.pos[0]
                        col = int(math.floor(posx/SQUARESIZE))

                        if self.is_valid_location(col):
                            row = self.get_next_open_row(col)
                            self.board.drop_piece(row, col, 2)

                            if self.check_win(2):
                                print("Player 2 wins!!")
                                self.game_over = True

                    self.turn += 1
                    self.turn = self.turn % 2

                    if not self.game_over:
                        self.draw_board()

        if self.game_over:
            pygame.time.wait(3000)

