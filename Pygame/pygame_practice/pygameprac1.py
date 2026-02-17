import pygame

#local constants
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    #event type for keypresses is keydown
    KEYDOWN,
    QUIT
)

pygame.init()

s_width = 800
s_height = 600

# Define a Player object by extending pygame.sprite.Sprite class 
# The surface drawn on the screen is now an attribute of 'player'

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.Surface((75, 25))
        self.surf.fill((255,255,255))
        self.rect = self.surf.get_rect()



# class pygame.surface.Surface - pass list containing width, height variables
screen = pygame.display.set_mode([s_width,s_height])
screen.fill((255,200,200))

#draw circle with parameters of color, center coordinates (x, y), radius in pixels
#this passes a surface object as arugment, i.e., screen variable here
pygame.draw.circle(screen, (0,0,255),(250, 250), 75)


#size = input("Enter a number for circle size: ") - could pass this in on the draw.circle parameters

#print(type(screen))

#create continous loop until running evaluates to false 
running = True

#each cycle of game loop is called a frame
while running: 
    #event handler
    for event in pygame.event.get():

        if event.type == KEYDOWN:

            if event.key == K_ESCAPE:
                #exits loop
                running = False

        # pygame.QUIT occurs when user clicks window close button
        elif event.type == pygame.QUIT:
            #causes loop to end, and drop down to pygame.quit()
            running = False

            
    #create new surface object and color its background
    
    surf = pygame.Surface((150,150))
    surf.fill((0,0,0))

    #calc to get exact center location, and assign to variable surf_center
    surf_center = (
        (s_width-surf.get_width())/2,
        (s_height-surf.get_height())/2
    )


    rect = surf.get_rect()

   #transfer contents of surf to screen, using coordinates of surf_center variable
    screen.blit(surf, (surf_center))
  
    #push contents to display
    pygame.display.flip()

#close window after exiting loop
pygame.quit()