

import pygame

pygame.init()


SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Working With Rectangles")

solider = pygame.image.load("walk.gif").convert_alpha()

#create rectangle from scratch
#arguments are x and y coords (top left), width, height
rect_1 = pygame.Rect(200,100, 150, 100)

rect_2 = solider.get_rect()

rect_2.topleft = (200,200)



#another option: derive rectangle from existing object





clock = pygame.time.Clock()

run = True

while run:
    #frame rate
    clock.tick(60)

    screen.fill((255,255,255))

    #args: game window, color, rectange itself
    #pygame.draw.rect(screen, (255,0,255), rect_1)

    # Just drawing a basic rectangle inline with only a single line of code
    # Notice, no blit required here. diplay.flip() or display.update() takes care of it
    pygame.draw.rect(screen,(0,25,25), pygame.Rect(30,30,60,60))

    pygame.draw.rect(screen, (2,10,10), (400, 600, 150, 100), width=5) # <-- this one will not render for some reason?

    pygame.draw.rect(screen, (202,143,9), (200, 100, 150, 150), width=5)

    # Drawing a rectangle that references an already created rect object
    # A pre-created rect object has its x and y coords, and w/h defined. Can also be set to an image.

    #pygame.draw.rect(screen, (0,255,255), rect_2)

    #character will stay with rectangle as it moves
    screen.blit(solider, rect_2)

    key = pygame.key.get_pressed()

    if key[pygame.K_a] == True:
       rect_2.move_ip(-5,0)

    if key[pygame.K_d] == True:
        rect_2.move_ip(5,0)

    if key[pygame.K_w] == True:
        rect_2.move_ip(0,-5)

    if key[pygame.K_s] == True:
        rect_2.move_ip(0,5)

    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run = False

    pygame.display.flip()

pygame.quit()

