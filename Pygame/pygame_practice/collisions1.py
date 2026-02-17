import pygame
import random

pygame.init()

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) 
pygame.display.set_caption('Collision')

#create main rect and obstacle rect
rect_1 = pygame.Rect(0, 0, 25, 25)

obstacles = []
# create multiple of the same obstacle rect
# remember to draw them!
for _ in range(16):
    obstacle_rect = pygame.Rect(random.randint(0, 500), random.randint(0, 300), 25, 25)
    obstacles.append(obstacle_rect)


#define colors

BG = (50, 50, 50)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

#hide mouse cursor
pygame.mouse.set_visible(False)


run = True
while run:
    #update background
    screen.fill(BG)

    #get mouse coords and use them to position rect

   

    #check collision and change color
   

    # check for collision for all obstacle items in list
    #for obstacle in obstacles:
        #if rect_1.colliderect(obstacle):
            #col = RED

    # a better way to detect collision in list
    col = GREEN
    # if no collision, value returns -1, doesn't return Boolean
    if rect_1.collidelist(obstacles) >= 0:
        print(rect_1.collidelist(obstacles))
        col = RED

    pos = pygame.mouse.get_pos()
    rect_1.center = pos

    #we started with this condition, but it only checks 
    # for the last obstacle created        
    #if rect_1.colliderect(obstacle_rect):
        #col = RED

    # draw all rectangles
    pygame.draw.rect(screen, col, rect_1)
    for obstacle in obstacles:
        pygame.draw.rect(screen, BLUE, obstacle)
    

    




    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    # udpate display
    pygame.display.flip()


pygame.quit()