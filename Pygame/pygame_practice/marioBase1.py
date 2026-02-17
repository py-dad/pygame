import pygame as pg
from pygame.locals import *
import sys
import time


pg.init()

clock = pg.time.Clock()
screen = pg.display.set_mode((800, 800))
jumping = False

Y_GRAVITY = 1
JUMP_HEIGHT = 20
Y_VELOCITY = JUMP_HEIGHT

X_POSITION, Y_POSITION = 424, 658

def stay():
    if rect1.y > 631:
        rect1.y = 631
    #if rect1.y < 0:
        #rect1.y = 0
    if rect1.x > 750:
        rect1.x = 750
    if rect1.x < 0:
        rect1.x = 0

# creat rect object, pass in xy (top-left) coords, wid, height
# this object can be drawn later with pygame.draw, or use .blit()
rect1 = pg.Rect(0,0,48,64)
print(f'rect1 pos before calling .get_rect: {rect1}')

# last tuple (48, 64) is width, height of image
mario_standing = pg.transform.scale(pg.image.load("assets/mario_standing.png"), (48,64))
mario_jumping =  pg.transform.scale(pg.image.load("assets/mario_jumping.png"), (48,64))
background = pg.image.load("assets/background.png")


# calling get_rect overrides original parameters of mRect, with current param of mario_standing
# optional: pass in new coordinates. this is where the rect will be once the game starts
rect1 = mario_standing.get_rect(topleft=(15,658))
print(rect1)



while True:

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

    # .draw.rect() seems to simply draw whatever rect object you defined previously, ie rect1
    #pg.draw.rect(background,(255,0,255), rect1) #rect1 here is just a pink rectangle 
    
    screen.blit(background, (0,0)) #blit the background image onto the screen (top-left x = 0, y = 0)
    screen.blit(mario_standing, rect1) #blit mario sprite onto rect1 object

    stay()
    
    key = pg.key.get_pressed()
    if key[pg.K_a] == True:
        #rect_2.x -= 5
        #move_ip does not create a new rect
        rect1.move_ip(-5, 0)
        print(rect1.x, rect1.y)

    if key[pg.K_d] == True:
        rect1.move_ip(5, 0)
        print(rect1.x, rect1.y)
        
    # Removed buttons that alter y coordinates
        
    if key[pg.K_SPACE]:
        jumping = True
    # Not sure why mario's y pos is at 0 once this jumping = True
    # Thought y should be at 658 (starting point prior to jumping)
    if jumping:
        # Before jump x = 15, y = 631
        # Y_VELOCITY starts getting subtracting from y coord, moving him up
        rect1.y -= Y_VELOCITY
        #print('after jump: ' + str(rect1.x) + ' ' + str(rect1.y))
        #time.sleep(0.85)
        # At the same time, Y_VELOCITY starts lowering by the value of Y_GRAVITY
        Y_VELOCITY -= Y_GRAVITY   # Allows mario to come back down. each time Y coord is reduced by one less (20, 19, 18..)


        if Y_VELOCITY < -JUMP_HEIGHT:
            print('Y_VELOCITY is now less than -JUMP_HEIGHT')
            jumping = False
            Y_VELOCITY = JUMP_HEIGHT
        
        rect1 = mario_jumping.get_rect(center=(X_POSITION, Y_POSITION))
        screen.blit(mario_jumping, rect1)
    else:
        #rect1 = mario_standing.get_rect(center=(X_POSITION, Y_POSITION))
        screen.blit(mario_standing, rect1)
        
        
        

    
    


   
    pg.display.update()

    # Research .tick further. now causing player to move faster or slower
    #clock.tick(30)

      