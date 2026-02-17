import pygame
import sys
import time
import random
from pygame import mixer
from pygame.locals import *

pygame.init()

sWidth = 1200
sHeight = 400
white = (255,255,255)
lightGreen = (148, 223, 206)
skyBlue = (79, 84, 203)
brown = (128, 101, 46)
yellow = (231, 249, 75)
grayBlue = (139, 134, 181)
greenBlue = (93, 156, 183)



#guy = pygame.image.load('walk.gif')

# Pass x, y, wid, height
#guy_rect = guy.get_rect()
#guy_rect.bottomleft = (126, 370)

# Returns a surface representing the visible part of the window
# It is this surface that you pass into drawing functions 
screen = pygame.display.set_mode((sWidth,sHeight))


#arguments are x and y coords (top left), width, height
#notice draw function is not called here. just setting up the object
#basic_rect = pygame.Rect(255, 35, 20, 10)

cloud = pygame.image.load('cloud.png')
cloud.set_colorkey((0,0,0), RLEACCEL)

cloud_rect = cloud.get_rect()

rock = pygame.image.load('rock2.png').convert_alpha()
rock.set_colorkey((0, 0, 0), RLEACCEL)
rock_rect = rock.get_rect()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.image.load('walk.gif').convert_alpha()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect()
        self.rect.x = 300
        self.rect.y = 270



       

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        #.convert() helps with optimization
        #self.surf = pygame.image.load("snowball.png").convert()
        #self.surf = pygame.image.load("rock2.png").convert()
        # Bigger fireballs
        self.surf = pygame.transform.scale(pygame.image.load("snowball.png"), (12,12))
        #set colorkey to black to make image appear without background
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)

        self.rect = self.surf.get_rect(center=(random.randint(sWidth + 20, sWidth + 100),
                                       random.randint(0, sHeight),))
                                       
        
    
        self.speed = random.randint(5,20)

        # Move the sprite based on speed determined by randint
        # Remove the sprite when it passes left edge of screen
    def update(self):
        #second parameter changes direction in which enemies move 0 = straight across, negative moves up, positive > 0 moves down
            self.rect.move_ip(-self.speed, 2)
            if self.rect.right < 0:
                self.kill()

        
pygame.mixer.init()
clock = pygame.time.Clock()

# Create a custom event for adding a new enemy and a cloud
ADDENEMY = pygame.USEREVENT + 1
#haha set the timer to 1 if you want an insane level (time is in milliseconds)

pygame.time.set_timer(ADDENEMY, 750)
player = Player()
#print(f'ADDENEMY EVENT {ADDENEMY}')
print(player.rect)

enemies = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)
clouds = pygame.sprite.Group()


pygame.mixer.music.load("nes1.wav")
pygame.mixer.music.play(loops=-1)




# Functions

""" def stay():
    if guy_rect.x <= 0:
        guy_rect.x = 0

    if guy_rect.x >= 1129:
        guy_rect.x = 1129

    if guy_rect.y <= 0:
        guy_rect.y = 0

    if guy_rect.y >= 270:
        guy_rect.y = 270
         """











running = True

while running:

    screen.fill(greenBlue)

   

    

    #stay()
    
    # args = surface, (color), (x, y, width, height), width=thicknes of line
    #pygame.draw.rect(screen, (202,143,9), (200, 100, 150, 150), width=5)
    #Note: must pass color, along with surface, and object itself
    #You don't need color if image? 
    screen.blit(cloud, cloud_rect)
   
    # pass in tuple of coordindates for rock's position
    screen.blit(rock,(1100, 342),(rock_rect))
    print(f'rock rect = {rock_rect}')
    
    # Ground shape 
    gr =  pygame.draw.rect(screen, (white), (0, 370, 1200, 100))
    # break up the white ground
    #gr1 = pygame.draw.rect(screen, (grayBlue), (50, 370, 100,10))
    #sun = pygame.draw.circle(screen, (yellow),(450, 82), 50 )
   
    # Get mouse position
    pos = pygame.mouse.get_pos()
    
    
    
    # Event handler 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
    
               
        if event.type == ADDENEMY:
            #create the new enemy and add to sprite groups
            #new_enemy is an instance of the Enemy class and gets all its attributes
            new_enemy = Enemy()
            #add new_enemy to sprite group enemies
            enemies.add(new_enemy)
            #add new_enemy to all_sprites group
            all_sprites.add(new_enemy)
            #print('new_enemy: ' + str(new_enemy))
    
    keys_pressed = pygame.key.get_pressed()
        
    if keys_pressed[pygame.K_RIGHT]:
        player.rect.move_ip(5, 0)

    if keys_pressed[pygame.K_LEFT]:
        player.rect.move(-5, 0)
        print('left')

    if keys_pressed[pygame.K_UP]:
        player.rect.move_ip(0, -5)

    if keys_pressed[pygame.K_DOWN]:
        player.rect.move_ip(0, 5)
    
    enemies.update()
  
    

    
        
     # Create a surface and pass tuple containing width, length
    #surf is assigned to a surface, but can't tell exactly which surface in the game it applies to
    surf = pygame.Surface((50,50))

    # Give the surface a color to sep from b/g
    surf.fill((0,0,0))
    rect = surf.get_rect()
    print(rect)

    # This line says "draw surf onto the screen at the center"
    surf_center = (
        (sWidth - surf.get_width())/2,
        (sHeight- surf.get_height())/2
    )
       
    for entity in all_sprites:
        screen.blit(entity.surf,entity.rect)
    
    if pygame.sprite.spritecollideany(player, enemies):
        # if so, then remove the player and stop the loop
        player.kill()

    

    
    


    pygame.display.flip()

    clock.tick(30)
    

pygame.quit()
sys.exit()