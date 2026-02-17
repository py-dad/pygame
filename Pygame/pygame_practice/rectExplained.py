import pygame
from pygame.locals import *



pygame.init()

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("")

jet = pygame.image.load('jet.png').convert()
jet.set_colorkey((255,255,255), RLEACCEL)
jet_rect = jet.get_rect()




def jetMovement():
    keys = pygame.key.get_pressed() # would like to set a global var and have the function reference it
    if keys[pygame.K_RIGHT]:
        jet_rect.move_ip(1, 0)

    if keys[pygame.K_LEFT]:
            jet_rect.move_ip(-1, 0)

# images/pygame surfaces don't have a position, so you have to store
# the blit position in the rect
# when you call get_rect of a pygame.Surface, pygame creates a new rect
# with the size of the image and the x,y coords
# to give the rect other coords during instantiation,
# you can pass an arugment to get_rect, mostly center or topleft is used
# to move the rect later you can change any of these attributes of the rect


# Another way to create a rect is to create an instance of the Rect class
# This rect object takes x, y, and wid/hgt
# This by itself will not draw the rect on screen
rect_1 = pygame.Rect(150, 150, 75, 35)



run = True

while run:
    
    screen.fill((255, 255, 255))
    # One way to draw rectangles is to simply draw it inline with pygame.draw.rect
    # Just pass surface, color, coords, size
    pygame.draw.rect(screen, (0, 0 , 0), (30, 30, 100, 100)) 

    # Another way is to call the draw function on the rect instance
    # We created at the top of the code
    # This works great for just drawing a rectangle object,
    # but for images, that's when you should use .blit
    pygame.draw.rect(screen, (11, 25, 79), rect_1)

    # a simple image blit, args surface, coords
    # Note: simply blitting this image(sufrace) onto the screen
    # does not allow it move. rather pass into .blit for movement 
    # this does not call the rect object created by jet_rect = jet.get_rect()
    #screen.blit(jet, (33, 99))
    

    # Screen blit may only be necessary for drawing images that are loaded
    # onto rect objects
    # images are represented by pygame.Surface objects
    # .draw is for drawing uniform colored rectangles
    # .blit is a method of Surface to draw bitmap images

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

   
    jetMovement()
    # .blit (surface to rect), this allows movement
    screen.blit(jet, jet_rect)
    pygame.display.flip()

pygame.quit()