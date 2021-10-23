import pygame
import sys

from settings import *
from level import Level


class Game:
    def __init__(self):
        self.level = Level(screen)

    def run(self):
        self.level.run()


# Setup level
pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
game = Game()

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill('black')
    game.run()

    pygame.display.update()
    clock.tick(60)
