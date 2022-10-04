import pygame
import random

from pygame.constants import *


class Player:
    def __init__(self, x, y, moveSpeed):
        self.x = x
        self.y = y
        self.movespeed = moveSpeed

    def draw(self):
        pygame.draw.circle(screen, (0, 0, 150), (self.x, self.y), 20)


class Tree:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        pygame.draw.circle(screen, (0, 80, 0), (self.x, self.y), 60)


pygame.init()
FPS = 400

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

# Set up the drawing window
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
clock = pygame.time.Clock()

# PLAYER:
player = Player(250, 250, 1)

# TREE:

treeList = []

for i in range(20):
    randX = random.randint(0, SCREEN_WIDTH)
    randY = random.randint(0, SCREEN_HEIGHT)

    tree = Tree(randX, randY)
    treeList.append(tree)

# Run until the user asks to quit
running = True
while running:

    keys = pygame.key.get_pressed()
    if keys[K_w]:
        player.y -= player.movespeed

    if keys[K_s]:
        player.y += player.movespeed

    if keys[K_d]:
        player.x += player.movespeed

    if keys[K_a]:
        player.x -= player.movespeed

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with white

    screen.fill((0, 180, 0))

    # Draw a solid blue circle in the center

    player.draw()

    for tree in treeList:
        tree.draw()

    # Flip the display
    pygame.display.flip()

    clock.tick(FPS)

# Done! Time to quit.
pygame.quit()
