import pygame

WIDTH,HEIGHT=600,600
ROWS,COLS=8,8
SQUARE_SIZE = WIDTH//COLS

# rgb
RED=(183,0,0)
WHITE=(242,242,242)
BLACK=(0,0,0)
BLUE=(0,0,255)
GREEN=(1,50,32)

CROWN = pygame.transform.scale(pygame.image.load("Checkers-Game/checkers/assets/crown.png"),(45,25))