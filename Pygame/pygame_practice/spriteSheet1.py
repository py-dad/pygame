import pygame
import spritesheet


pygame.init()

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Spritesheets")

sprite_sheet_image = pygame.image.load('doux.png').convert_alpha()
sprite_sheet = spritesheet.SpriteSheet(sprite_sheet_image)
BG = (50, 50, 50)
BLACK = (0, 0, 0)

#create animation list
animation_list = []
animation_steps = 10
last_update = pygame.time.get_ticks()
animation_cooldown = 250
frame = 0

for x in range(animation_steps):
    animation_list.append(sprite_sheet.get_image(x, 24, 24, 3, BLACK))
   

    

run = True

while run:

    screen.fill(BG)

    #update animation
    current_time = pygame.time.get_ticks()
    if current_time - last_update >=animation_cooldown:
        frame +=1
        last_update = current_time
        if frame >= len(animation_list):
            frame = 0

    # draw on screen AFTER background fill/image to the bg drawing over object
    # looks like you pass x/y into blit instead of rect object or vice versa
    #screen.blit(sprite_sheet_image, (0,0))

    #show frame image
    
    screen.blit(animation_list[frame], (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()

pygame.quit()