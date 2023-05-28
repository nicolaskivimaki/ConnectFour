import pygame 
from constants import *
import sys
import math
from AI_engine import AI_engine
import time

class Game:
    def __init__(self, board):
        pygame.init()
        self.board = board
        self.ai = AI_engine(board)
        self.ai_token = None
        self.player_token = None
        self.ai_level = None
        self.winner = ""
        self.width = COLUMN_COUNT * SQUARESIZE
        self.height = (ROW_COUNT+1) * SQUARESIZE
        size = (self.width, self.height)
        self.screen = pygame.display.set_mode(size)
        pygame.display.set_caption('Connect Four')
        self.game_state = "START"
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
                    pygame.draw.circle(self.screen, self.player_token, (int(c*SQUARESIZE+SQUARESIZE/2), self.height-int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS)
                elif self.board.board[r][c] == 2: 
                    pygame.draw.circle(self.screen, self.ai_token, (int(c*SQUARESIZE+SQUARESIZE/2), self.height-int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS)
        pygame.display.update()

    def is_valid_location(self, col):
        return self.board.board[ROW_COUNT-1][col] == 0

    def get_next_open_row(self, col):
        for r in range(ROW_COUNT):
            if self.board.board[r][col] == 0:
                return r
    
    def text_objects(self, text, font, color):
        textSurface = font.render(text, True, color)
        return textSurface, textSurface.get_rect()

    def ai_level_button(self, screen, x, y, level):
        (self.screen, self.width / 2, self.height / 2, 200, 100, "1", "1")
        width = 80
        height = 40
        mouse_pos = pygame.mouse.get_pos()
        clicked = pygame.mouse.get_pressed()[0]

        button_rect = pygame.Rect(x, y, width, height)

        # Check if the mouse is over the button
        if button_rect.collidepoint(mouse_pos):
            button_rect = pygame.Rect(x-10, y-5, width+20, height+10)
            pygame.draw.rect(screen, BLUE, button_rect)
            if clicked:
                self.ai_level = level
        elif self.ai_level == level:
            button_rect = pygame.Rect(x-10, y-5, width+20, height+10)
            pygame.draw.rect(screen, BLUE, button_rect)
        else:
            pygame.draw.rect(screen, WHITE, button_rect)

        # Draw the button text
        font = pygame.font.Font("freesansbold.ttf", 20)
        text_surface = font.render(str(level), True, BLACK)
        text_rect = text_surface.get_rect(center=button_rect.center)
        screen.blit(text_surface, text_rect)

    def colour_button(self, screen, msg, x, y, rad, colour):
        mouse_pos = pygame.mouse.get_pos()
        clicked = pygame.mouse.get_pressed()[0]

        button_rect = pygame.Rect(x-rad, y-rad, rad*2, rad*2)

        # Check if the mouse is over the button
        if button_rect.collidepoint(mouse_pos):
            pygame.draw.circle(self.screen, colour, (x, y), rad+10)
            if clicked:
                print("CHOSEN: ", colour)
                self.set_player_tokens(colour)
        elif self.player_token == colour:
            pygame.draw.circle(self.screen, colour, (x, y), rad+10)
        else:
            pygame.draw.circle(self.screen, colour, (x, y), rad)

        smallText = pygame.font.Font("freesansbold.ttf", 20)
        textSurf, textRect = self.text_objects(msg, smallText, BLACK)
        textRect.center = ((x, y))
        screen.blit(textSurf, textRect)

    def play_button(self, screen, x, y, text):
        (self.screen, self.width / 2, self.height / 2, 200, 100, "1", "1")
        width = 120
        height = 60
        mouse_pos = pygame.mouse.get_pos()
        clicked = pygame.mouse.get_pressed()[0]

        button_rect = pygame.Rect(x, y, width, height)

        # Check if the mouse is over the button
        if button_rect.collidepoint(mouse_pos):
            button_rect = pygame.Rect(x-10, y-5, width+20, height+10)
            pygame.draw.rect(screen, BLUE, button_rect)
            if clicked:
                if (self.ai_level and self.player_token) is not None:
                    self.run()
                    self.ai_level = None
                    self.ai_token = None
                    self.player_token = None
        else:
            pygame.draw.rect(screen, WHITE, button_rect)

        # Draw the button text
        font = pygame.font.Font("freesansbold.ttf", 20)
        text_surface = font.render(text, True, BLACK)
        text_rect = text_surface.get_rect(center=button_rect.center)
        screen.blit(text_surface, text_rect)


    def start_screen(self):

        intro = True

        while intro:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.screen.fill(BLACK)

            Title = pygame.font.Font('freesansbold.ttf', 64)
            TitleSurf, TitleRect = self.text_objects("Connect Four", Title, WHITE)
            TitleRect.center = (self.width / 2, 120)

            Text1 = pygame.font.SysFont('helveticalight.ttf', 28)
            Text1Surf, Text1Rect = self.text_objects("Choose your colour. Red goes first.", Text1, WHITE)
            Text1Rect.center = (self.width / 2, 190)

            Text2 = pygame.font.SysFont('helveticalight.ttf', 28)
            Text2Surf, Text2Rect = self.text_objects("Choose AI depth. 2 = easy, 6 = hard.", Text2, WHITE)
            Text2Rect.center = (self.width / 2, 390)

            self.screen.blit(TitleSurf, TitleRect)
            self.screen.blit(Text1Surf, Text1Rect)
            self.screen.blit(Text2Surf, Text2Rect)

            colour_button_y = 290

            self.colour_button(self.screen, "RED", (self.width / 2) - 90, colour_button_y, RADIUS + 8, RED)
            self.colour_button(self.screen, "YELLOW", (self.width / 2) + 90, colour_button_y, RADIUS + 8, YELLOW)

            level_button_y = 440

            self.ai_level_button(self.screen, -165 + self.width / 2, level_button_y, 2)
            self.ai_level_button(self.screen, -40 + self.width / 2, level_button_y, 4)
            self.ai_level_button(self.screen, 85 + self.width / 2, level_button_y, 6)
            self.play_button(self.screen, -60 + self.width / 2, 535, "PLAY")

            pygame.display.update()

    def set_player_tokens(self, player_colour):
        self.player_token = player_colour
        if player_colour == RED:
            self.ai_token = YELLOW
            self.turn = 1
        else:
            self.ai_token = RED
            self.turn = 2

    def run(self):

        self.game_over = False
        self.board.reset_board()
        self.draw_board()

        while not self.game_over:

            pygame.draw.rect(self.screen, BLACK, (0,0, self.width, SQUARESIZE))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEMOTION:
                    posx = event.pos[0]
                    if self.turn == 1:
                        pygame.draw.circle(self.screen, self.player_token, (posx, int(SQUARESIZE/2)), RADIUS)
                    pygame.display.update()

                if event.type == pygame.MOUSEBUTTONDOWN and self.turn == 1:

                    # Player Input
                    posx = event.pos[0]
                    col = int(math.floor(posx/SQUARESIZE))

                    if self.is_valid_location(col):
                        row = self.get_next_open_row(col)
                        self.board.drop_piece(row, col, 1)

                        if self.board.check_win(1):
                            self.winner = "You win!"
                            self.game_over = True
                        
                        self.turn = 2

                self.draw_board()

                if self.turn == 2 and not self.game_over:
                    
                    col = self.ai.minimax(self.board.board, self.ai_level, True, -INFINITY, INFINITY)[0]

                    if self.board.is_valid_location(col):
                        row = self.get_next_open_row(col)
                        self.board.drop_piece(row, col, 2)

                        if self.board.check_win(2):
                            self.winner = "AI wins!"
                            self.game_over = True

                    self.turn = 1

                self.draw_board()
 
        if self.game_over:
            GameOverTitle = pygame.font.Font('freesansbold.ttf', 44)
            GameOverTitleSurf, GameOverTitleRect = self.text_objects(self.winner, GameOverTitle, WHITE)
            GameOverTitleRect.center = (self.width / 2, 55)
            self.screen.blit(GameOverTitleSurf, GameOverTitleRect)
            pygame.display.update()

            time.sleep(4)

            

