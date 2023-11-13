import pygame
from .constants import RED,SQUARE_SIZE,GREEN

class Piece:
    PADDING=8
    # OUTLINE=4
    
    def __init__(self,row,col,colour):
        self.row=row
        self.col=col
        self.colour=colour
        self.king=False
        
        if self.colour==RED:
            self.direction=-1
        else:
            self.direction=1
            
        self.x=0
        self.y=0
        self.calc_pos()
        
    def calc_pos(self):
        self.x=SQUARE_SIZE*self.col + SQUARE_SIZE//2
        self.y=SQUARE_SIZE*self.row + SQUARE_SIZE//2
        
    def make_king(self):
        self.king=True
        
    def draw(self,win):
        radius=(SQUARE_SIZE//2-self.PADDING)
        # pygame.draw.circle(win,GREEN,(self.x,self.y),radius+self.OUTLINE)
        pygame.draw.circle(win,self.colour,(self.x,self.y),radius)
        
    def __repr__(self):
        return str(self.colour)