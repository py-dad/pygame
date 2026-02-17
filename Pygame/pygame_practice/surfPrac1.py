import pygame
import sys

pygame.init()

display = pygame.display.set_mode((400,300))

mySurface1 = pygame.Surface((100, 50))

mySurface2 = pygame.Surface((50,50))

mySurface3 = pygame.Surface((50,100))

mySurface1.fill((255, 0, 0))
mySurface2.fill((0, 255, 0))
mySurface3.fill((0,0,255))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    display.blit(mySurface1, (20,20))
    display.blit(mySurface2, (100,100))
    display.blit(mySurface3, (200,80))

    pygame.display.update()