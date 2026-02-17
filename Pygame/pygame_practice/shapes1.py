
# Utilize shapes to create graphics without loading additonal assets

import pygame



pygame.init()

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
x = 0    # Variable for drawing arc 

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Working With Shapes")

run = True

while run:

    screen.fill((255, 255, 255))
    # Neat trick with arcs. Alter x variable with mouse input
    # X variable is start and stop radiants?
    if pygame.mouse.get_pressed()[0] == True:
        x += 0.001
    elif pygame.mouse.get_pressed()[2] == True:
        x -= 0.001
    # get x, y coordinates of mouse position
    pos = pygame.mouse.get_pos()

    # Polygons

    #pygame.draw.polygon(screen, (100,100,100), ((100, 200), (200, 300), (500, 100), (250, 250)))

    # Lines
    # Just need start and end coord, int coord
    # Line will follow mouse pos
    #pygame.draw.line(screen, (255, 0, 255), (300, 200), pos)
    
    # Rectangles 
    # Args surface, color, x, y, width, height (manipulate shape with other args)
    # pygame.draw.rect(screen, (255,0,0), (200, 100, 150, 100),width=5, border_radius = 50)

    # Circles
    #surface, color, center coords, radius)
    #pygame.draw.circle(screen, (0, 0, 0), (300, 200), 75)
    #pygame.draw.circle(screen, (255, 255, 0), (300,200), 75, draw_top_right = True, draw_bottom_left = True)

    # Arcs
    pygame.draw.arc(screen, (0, 255, 255), (200, 100, 150, 150), 0, x, width=5)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()

pygame.quit()