#Coding With Russ

#note in this example, he shows a more complicated way to draw a grid
#with images and tiles. he wanted to demonstrate what is going on in the
#background during the game

import pygame
from pygame.locals import *

pygame.init()

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 900


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Platformer")

#define game variables

tile_size = 180

#load images
sun_img = pygame.image.load('sun.png')
bg_img = pygame.image.load('sky.png')

class World():
    def __init__(self, data):
        self.tile_list = []

        #load images
        dirt_img = pygame.image.load('dirt.png')
        grass_img = pygame.image.load('grass.png')
        row_count = 0
        for row in data:
            col_count = 0
            for tile in row:
                if tile == 1:
                    img = pygame.transform.scale(dirt_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                    print(self.tile_list)

                if tile == 2:
                    img = pygame.transform.scale(grass_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                    
                    
                col_count += 1
            row_count += 1

    def draw(self):
        for tile in self.tile_list:
            screen.blit(tile[0], tile[1])

#copy the enter list grid from video description if you want the entire world data list
world_data = [

[1,1,1,1,1],
[1,0,0,0,1],
[1,0,0,0,1],
[1,0,0,0,1],
[1,2,2,2,1],
]

world = World(world_data)

run = True
while run:

    #pass image, and x, y coords
    screen.blit(bg_img, (0,0))
    screen.blit(sun_img, (100,0))

    world.draw()
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                run = False

    pygame.display.update()

pygame.quit()