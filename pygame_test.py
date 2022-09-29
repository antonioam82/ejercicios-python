import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((600,500))
color = (255,0,0)
done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    pygame.draw.rect(screen,color,pygame.Rect(100,100,100,100))
    pygame.display.update()

pygame.quit()  # quits pygame
sys.exit()
