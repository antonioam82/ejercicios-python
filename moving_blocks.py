import pygame, sys, time
from pygame.locals import *

pygame.init()

WINDOWWIDTH = 400
WINDOWHEIGHT = 400
windowSurface = pygame.display.set_mode(WINDOWWITH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption("Moving Blocks")

DOWNLEFT = 1
DOWNRIGHT = 3
UPLEFT = 7
UPRIGHT = 9

MOVESPEED = 4

BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
