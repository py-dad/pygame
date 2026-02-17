import pygame
from pygame.locals import * 


pygame.init()

CLOCK =  pygame.time.Clock()


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

rect_1 = pygame.Rect(100, 100, 150, 100)

def moveBox():
    key = pygame.key.get_pressed()
    if key[pygame.K_RIGHT]:
        rect_1.move_ip(1, 0)
    if key[pygame.K_LEFT]:
        rect_1.move_ip(-1, 0)
    if key[pygame.K_UP]:
        rect_1.move_ip(0, -1)
    if key[pygame.K_DOWN]:
        rect_1.move_ip(0, 1)

run = True
while run:
    screen.fill((15, 0, 255))
    pygame.draw.rect(screen, (10, 255, 88), rect_1)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    moveBox()
    screen.blit(screen, rect_1)
    pygame.display.flip()
    CLOCK.tick(120)
   
   
    
    
   
    



pygame.quit()



