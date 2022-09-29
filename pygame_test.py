import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((600,500))

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    pygame.display.update()

pygame.quit()  # quits pygame
sys.exit()
