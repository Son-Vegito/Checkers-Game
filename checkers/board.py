import pygame
from .constants import BLACK,ROWS,COLS,GREEN,SQUARE_SIZE,RED,WHITE
from .piece import Piece

class Board:
    def __init__(self):
        self.board = []
        self.selected_piece = None
        self.red_left=self.white_left=12    # number of pieces
        self.red_kings=self.white_king=0    # number of kings
        self.create_board()
        
    def draw_squares(self,win):
        win.fill(BLACK)
        for row in range(ROWS):
            for col in range(row%2, ROWS, 2):
                pygame.draw.rect(win,GREEN,(row*SQUARE_SIZE,col*SQUARE_SIZE,SQUARE_SIZE,SQUARE_SIZE))
                
    def create_board(self):
        for row in range(ROWS):
            self.board.append([]) 
            for col in range(COLS):
                if col % 2 ==((row + 1)%2):
                    if row<3:
                        self.board[row].append(Piece(row,col,WHITE))
                    elif row>4:
                        self.board[row].append(Piece(row,col,RED))
                    else:
                        self.board[row].append(0)
                else:
                    self.board[row].append(0)
                    
    def draw(self,win):
        self.draw_squares(win)
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[row][col]
                if piece != 0:
                    piece.draw(win)