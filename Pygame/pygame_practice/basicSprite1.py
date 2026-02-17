#An example basic game template
#Modify as needed


import pygame
import random
import time




pygame.init()

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
col = (231, 249, 75)
colors = ["crimson", "chartreuse", "coral", "darkorange", "forestgreen",
          "lime", "navy"]

clock = pygame.time.Clock()
FPS = 60

class Square(pygame.sprite.Sprite):
    def __init__(self, col, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill(col)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def update(self):
        self.rect.move_ip(0,5)
        if self.rect.top > SCREEN_HEIGHT:
            # delete sprite from group once off screen
            self.kill()


square = Square("crimson", 500, 300)

squares = pygame.sprite.Group()


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("")

run = True

while run:

    clock.tick(FPS)

    print(squares)
    screen.fill(("cyan"))

    squares.update()
    squares.draw(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            square = Square(random.choice(colors), pos[0], pos[1])
            squares.add(square)

    pygame.display.flip()

pygame.quit()