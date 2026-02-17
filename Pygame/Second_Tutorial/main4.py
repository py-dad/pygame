# AirStrike v1.0.4

# import game module
import pygame
from pygame import mixer

# Import random for random numbers
import random

# import pygame.locals for easier access to key coordinates

from pygame.locals import (
    RLEACCEL,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,

)

# define constants for screen w/h
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


# Define player object by extending pygame.sprite.Sprite
# The surface drawn on the screen is now an atrribute of 'player'
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.image.load("jet.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect()

    # Move the sprite based on keypresses
    # speed up jet by increasing 1st number (defaults are 5 or -5)
    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -10)
            move_up_sound.play()
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 10)
            move_down_sound.play()
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-10, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(10, 0)

        # Get the current mouse position
        pos = pygame.mouse.get_pos()
        # Set the player x position to the mouse x position
        self.rect.x = pos[0]
        self.rect.y = pos[1]

        # Keep player on the screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT


# Define the enemy object (pass Sprite class to become super class)
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        # .convert() helps with optimization
        self.surf = pygame.image.load("missile.png").convert()
        # set colorkey to black to make image appear without background
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(0, SCREEN_HEIGHT),
            )

        )
        # determine speeds of enemies by passing two numbers into random integer fuction (lower is slower)
        # play around with speeds by changing the integers that are pass into randint function
        self.speed = random.randint(5, 20)

        # Move the sprite based on speed determined by randint
        # Remove the sprite when it passes left edge of screen

    def update(self):
        # second parameter changes direction which enemies move 0 = straight across, - moves up, + > 0 moves down
        self.rect.move_ip(-self.speed, 2)
        if self.rect.right < 0:
            self.kill()


# Try creating a new boss class
class Boss(pygame.sprite.Sprite):
    def __init__(self):
        super(Boss, self).__init__()
        self.surf = pygame.image.load("C-05.png").convert()
        # set colorkey to black to make image appear without background
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(0, SCREEN_HEIGHT),
            )

        )
        # determine speeds of enemies by passing two numbers into random integer fuction (lower is slower)
        # play around with speeds by changing the integers that are pass into randint function
        self.speed = random.randint(5, 50)

        # Move the sprite based on speed determined by randint
        # Remove the sprite when it passes left edge of screen

    def update(self):

        # place these if conds above the other if to cause boss to get stuck on the screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
        # 2nd parameter changes direction which enemies move 0 = straight across, -moves up, positive > 0 moves down
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()


# Define the cloud object by extending pygame.sprite.Sprite
class Cloud(pygame.sprite.Sprite):
    def __init__(self):
        super(Cloud, self).__init__()
        self.surf = pygame.image.load("cloud.png").convert()
        # used to set transparency of surface cloud is drawn on. setting to white makes background transparent
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)
        # starting position randomly generated
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(0, SCREEN_HEIGHT)
            )
        )
        # move cloud based on constant speed
        # remove cloud when it passes left edge of screen

    def update(self):
        self.rect.move_ip(-5, 0)
        if self.rect.right < 0:
            self.kill()


# Setup for sounds. Defaults are good.
# Note if you want to change defaults, you need to call mixer before pygame.init()
pygame.mixer.init()

# Initialize pygame
pygame.init()

# create the screen object
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Setupo the clock for a decent framerate
clock = pygame.time.Clock()

# Create a custom event for adding a new enemy and a cloud
ADDENEMY = pygame.USEREVENT + 1
# haha, set the timer to 1 if you want an insane level (time is in milliseconds)
pygame.time.set_timer(ADDENEMY, 250)
ADDCLOUD = pygame.USEREVENT + 2
# lower this time if you want a bulk of clouds together
pygame.time.set_timer(ADDCLOUD, 1000)
ADDBOSS = pygame.USEREVENT + 3
pygame.time.set_timer(ADDBOSS, 10000)

# Instantiate player. Right now, this is just a rectangle.
player = Player()

# create groups to hold enemy sprites, cloud sprites,(positional movements) and all sprites (rendering)

enemies = pygame.sprite.Group()
clouds = pygame.sprite.Group()
bosses = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

# Load and play background music
# changed music from v1
pygame.mixer.music.load("level2.wav")
pygame.mixer.music.play(loops=-1)

# Load all sound files assign to variable triggered by event
move_up_sound = pygame.mixer.Sound("Rising_putter.ogg")
move_down_sound = pygame.mixer.Sound("Falling_putter.ogg")
collision_sound = pygame.mixer.Sound("Collision.ogg")

# come back to later
# score = 0

# variable to keep the main loop running
running = True

# Main loop
while running:
    # Look at every event in the queue
    for event in pygame.event.get():
        # Did the user hit a key?
        if event.type == KEYDOWN:
            # was it the Esc key? is so, stop loop
            if event.key == K_ESCAPE:
                running = False

        elif event.type == QUIT:
            running = False

        # timer will fire off this event every 250 milliseconds
        elif event.type == ADDENEMY:
            # create the new enemy and add to sprite groups
            # new_enemy is an instance of the Enemy class and gets all its attributes
            new_enemy = Enemy()
            # add new_enemy to sprite group enemies
            enemies.add(new_enemy)
            # add new_enemy to all_sprites group
            all_sprites.add(new_enemy)

        # timer will fire off this event every 1000 milliseconds
        elif event.type == ADDCLOUD:
            # create the new cloud and add to sprite group
            new_cloud = Cloud()
            clouds.add(new_cloud)
            all_sprites.add(new_cloud)

        # taking out bosses for now
        # listen for event ADDBOSS, and then contstruct a new boss object
        # elif event.type == ADDBOSS:
        # new_boss = Boss()
        # bosses.add(new_boss)
        # all_sprites.add(new_boss)

    # Get the set of keys pressed and check for user input
    pressed_keys = pygame.key.get_pressed()

    # Update the player sprite based on user keypresses
    player.update(pressed_keys)

    # Update the position of enemies and clouds 
    enemies.update()
    clouds.update()
    bosses.update()

    # Fill the screen with sky blue
    screen.fill((135, 206, 250))

    # Draw the player on the screen
    screen.blit(player.surf, player.rect)

    # Create a surface and pass tuple containing width, length
    # surf is assigned to a surface, but can't tell exactly which surface in the game it applies to
    surf = pygame.Surface((50, 50))

    # Give the surface a color to sep from b/g
    surf.fill((0, 0, 0))
    rect = surf.get_rect()

    # This line says "draw surf onto the screen at the center"
    surf_center = (
        (SCREEN_WIDTH - surf.get_width()) / 2,
        (SCREEN_HEIGHT - surf.get_height()) / 2
    )
    # screen.blit(surf, surf_center)
    # draw all sprites
    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)

    # check if any enemies have collided with the player. im guessing only two entries can be passed at a time
    # because it only checks for two objects to collide, not 3 or more.
    if pygame.sprite.spritecollideany(player, enemies):
        # if so, then remove the player and stop the loop
        player.kill()

        # Stop any moving sounds and play the collision sound
        move_up_sound.stop()
        move_down_sound.stop()
        collision_sound.play()
        pygame.mixer.music.stop()
        pygame.mixer.quit()

        # Stop the loop
        running = True

    # elif pygame.sprite.spritecollideany(player, bosses):
    # player.kill()
    # running = False

    # still under For loop
    pygame.display.flip()

    # Ensure program maintains a rate of 30 fps
    clock.tick(30)
