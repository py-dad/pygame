import pygame
import sys
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
SCREEN = pygame.display.set_mode((800,800))
pygame.display.set_caption("Jumping in Pygame")

X_POSITION, Y_POSITION = 424, 658

jumping = False

Y_GRAVITY = 1
# how high to jump
JUMP_HEIGHT = 20

# speed at which mario jumps
Y_VELOCITY = JUMP_HEIGHT


STANDING_SURFACE = pygame.transform.scale(pygame.image.load("assets/mario_standing.png"), (48,64))
JUMPING_SURFACE =  pygame.transform.scale(pygame.image.load("assets/mario_jumping.png"), (48,64))
BACKGROUND = pygame.image.load("assets/background.png")

# rect for mario which controls his position
mario_rect = STANDING_SURFACE.get_rect(center=(X_POSITION, Y_POSITION))

#print mario_rect pos
print(mario_rect.x, mario_rect.y)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Maybe try getting KEYDOWN to work instead of get_pressed
    # Returns dict on all keys you can press
    keys_pressed = pygame.key.get_pressed()

    if keys_pressed[pygame.K_SPACE]:
        jumping = True

    if keys_pressed[pygame.K_RIGHT]:
        mario_rect.move_ip(5,0)
        print("mario_rect x coord = " + str(mario_rect.x))
    
    if keys_pressed[pygame.K_LEFT]:
        mario_rect.move_ip(-5,0)
        print("mario_rect x coord = " + str(mario_rect.x))
    



    SCREEN.blit(BACKGROUND, (0,0))
    
    # remove so mario is not always standing
    SCREEN.blit(STANDING_SURFACE, mario_rect)

    if jumping:
        # subtracing from Y position actually moves items up the screen
    
        Y_POSITION -= Y_VELOCITY
        # pull back down with gravity
        Y_VELOCITY -= Y_GRAVITY
       
        print('Y_POSITION = ' + str(Y_POSITION))
        print('Y_VELOCITY = ' + str(Y_VELOCITY))
        
        
        # check if we finished our jump
        if Y_VELOCITY <  -JUMP_HEIGHT:
            jumping = False
            Y_VELOCITY = JUMP_HEIGHT
            # Returns mario to his original x and y coords
            # could get_rect arguments be changed to make him land wherever he's standing?
        mario_rect = STANDING_SURFACE.get_rect(center=(X_POSITION, Y_POSITION))
        SCREEN.blit(JUMPING_SURFACE, mario_rect)
        print(STANDING_SURFACE.get_rect(center=(X_POSITION, Y_POSITION)))

    else:
       # mario_rect = STANDING_SURFACE.get_rect(center=(X_POSITION, Y_POSITION))
        SCREEN.blit(STANDING_SURFACE, mario_rect)

    pygame.display.update()
    CLOCK.tick(60)

