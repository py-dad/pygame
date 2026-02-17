import pygame, sys, time
from pygame.locals import (
    RLEACCEL,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    K_SPACE,
    KEYDOWN,
    QUIT,

)


pygame.init()

CLOCK = pygame.time.Clock()
WIDTH = 600
HEIGHT = 400

WHITE = (255,255,255)
pygame.display.set_caption("Surf and Rect Practice")
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
print(WIDTH)
print(HEIGHT)

#create rect object: pass x, y coords (of top-left), wid and height
rect_2 = pygame.Rect(0, 0, 150, 100)


cloud = pygame.image.load("cloud.png").convert()
cloud.set_colorkey((0,0,0), RLEACCEL)

# get the x,y coords of top-left, and width and height of image
rect_2 = cloud.get_rect()
# this will override coordinates set when object was first created
#rect_2.topleft = (200, 200)

def Moving():
    if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                rect_2.move_ip(5, 0)
                print(rect_2)
            if event.key == K_LEFT:
                rect_2.move_ip(-10, 0)
                print(rect_2)
            if event.key == K_UP:
                rect_2.move_ip(0,-10)
                print(rect_2)
            if event.key == K_DOWN:
                rect_2.move_ip(0, 10)
                print(rect_2)

            # Keep object on the screen
            if rect_2.x < 0:
                rect_2.x = 0
            if rect_2.y < 0:
                rect_2.y = 0
            if rect_2.y > HEIGHT:
                rect_2.y = HEIGHT
            if rect_2.x > WIDTH:
                rect_2.x = WIDTH

# GAME LOOP
                
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # defined function to move rect
        # commenting out to use get_pressed()
        #Moving()
     


    SCREEN.fill((135, 206, 235))
    #draw rect_1 on screen
   # pygame.draw.rect(SCREEN, (255,255,255), rect_2)
    # russ demonstrated to draw the rect_2 on screen
    # but it seems as if blit is enough, and blit will also
    # maintain transparency, whereas "draw" didnt' for some reason
    # russ says draw command can be removed to use Blit
    # pygame.draw.rect(SCREEN,(0,0,255), rect_2)

    # this blit gets the image to follow the rect
    # sprites or images are just on top of rects
    # positions and collisions are handled by rectangles
    # this blits the cloud image on top of rect_2
    SCREEN.blit(cloud, rect_2 )

    #another way to handle keyboard input
    # it seems as if get_pressed allows users to hold down button
    # and continue to move. KEYDOWN does not seem to do this?
    key = pygame.key.get_pressed()
    if key[pygame.K_a] == True:
        #rect_2.x -= 5
        #move_ip does not create a new rect
        rect_2.move_ip(-5, 0)

    if key[pygame.K_d] == True:
        rect_2.move_ip(5, 0)

    if key[pygame.K_w] == True:
        rect_2.move_ip(0, -5)

    if key[pygame.K_s] == True:
        rect_2.move_ip(0, 5)
    
    
    
    pygame.display.flip()
    CLOCK.tick(30)

        

