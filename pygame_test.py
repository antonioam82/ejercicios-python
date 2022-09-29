import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((600,500))
color = (255,0,0)
x = 100
y = 100
done = False
clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    keyPressed = pygame.key.get_pressed()
    screen.fill((0,0,0))
    if keyPressed[pygame.K_UP]:
        y-=3;
    if keyPressed[pygame.K_DOWN]:
        y+=3;
    if keyPressed[pygame.K_LEFT]:
        x-=3;
    if keyPressed[pygame.K_RIGHT]:
        x+=3;
        
    pygame.draw.rect(screen,color,pygame.Rect(x,y,100,100))
    pygame.display.update()
    clock.tick(60)

pygame.quit()  # quits pygame
sys.exit()
