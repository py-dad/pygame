import pygame
import sys
import time
from pygame import mixer
import random

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

pygame.mixer.init()
pygame.init()

class Mario(pygame.sprite.Sprite):
    def __init__(self):
        super(Mario, self).__init__()
        X_POSITION = 424
        Y_POSITION = 658
        STANDING_SURFACE = pygame.transform.scale(pygame.image.load("assets/mario_standing.png"), (48,64))
        JUMPING_SURFACE =  pygame.transform.scale(pygame.image.load("assets/mario_jumping.png"), (48,64))
        self.rect = STANDING_SURFACE.get_rect(center=(X_POSITION, Y_POSITION))

    def update(self, pressed_keys):
        if pressed_keys[pygame.K_UP]:
            self.rect.move_ip(0, -10)
            #move_up_sound.play()
        if pressed_keys[pygame.K_DOWN]:
            self.rect.move_ip(0, 10)
            #move_down_sound.play()
        if pressed_keys[pygame.K_LEFT]:
            self.rect.move_ip(-10, 0)
        if pressed_keys[pygame.K_RIGHT]:
            self.rect.move_ip(10, 0)
        """ if pressed_keys[pygame.K_SPACE]:
            jumping = True """
    




""" X_POSITION, Y_POSITION = 424, 658
Y_GRAVITY = 1
# how high to jump
JUMP_HEIGHT = 20 

# speed at which mario jumps
Y_VELOCITY = JUMP_HEIGHT """

MARIO = Mario()
CLOCK = pygame.time.Clock()
SCREEN = pygame.display.set_mode((800,800))
pygame.display.set_caption("Jumping in Pygame")


all_sprites = pygame.sprite.Group()
all_sprites.add(MARIO)


X_POSITION, Y_POSITION = 424, 658

jumping = False

Y_GRAVITY = 1
JUMP_HEIGHT = 20
Y_VELOCITY = JUMP_HEIGHT


STANDING_SURFACE = pygame.transform.scale(pygame.image.load("assets/mario_standing.png"), (48,64))
JUMPING_SURFACE =  pygame.transform.scale(pygame.image.load("assets/mario_jumping.png"), (48,64))
BACKGROUND = pygame.image.load("assets/background.png")

# rect for mario which controls his position
#mario_rect = STANDING_SURFACE.get_rect(center=(X_POSITION, Y_POSITION))

#print mario_rect pos
print(MARIO.rect.x, MARIO.rect.y)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    

        elif event.type == KEYDOWN:
            if event.key == K_SPACE:
                jumping = True

        elif event.type == KEYDOWN:
            if event.key == K_RIGHT:
                Mario.rect.move.ip(5,0)
                SCREEN.blit(STANDING_SURFACE, MARIO.rect) 
                 

                
        
        

    # Returns dict on all keys you can press
    pressed_keys = pygame.key.get_pressed()

    MARIO.update(pressed_keys)

    SCREEN.blit(BACKGROUND, (0,0))
    
    # remove so mario is not always standing
    SCREEN.blit(STANDING_SURFACE, MARIO.rect)

    if jumping == True:
        
        Y_POSITION -= Y_VELOCITY
        # pull back down with gravity
        Y_VELOCITY -= Y_GRAVITY
        
        # check if we finished our jump
        if Y_VELOCITY <  -JUMP_HEIGHT:
            jumping = False
            Y_VELOCITY = JUMP_HEIGHT
        MARIO.rect = STANDING_SURFACE.get_rect(center=(X_POSITION, Y_POSITION))
        SCREEN.blit(JUMPING_SURFACE, MARIO.rect) 

    else:
        MARIO.rect = STANDING_SURFACE.get_rect(center=(X_POSITION, Y_POSITION))
        SCREEN.blit(STANDING_SURFACE, MARIO.rect)

    

    pygame.display.update()
    CLOCK.tick(60)

