import pygame
import sys

from settings import *
from level import Level
from ui import UI
from debug import debug


class Game:
    def __init__(self):
        self.coins_amount = 100
        self.life = 20

        self.level = Level(screen, self.coins_amount,
                           self.change_coins, self.change_life)

        # User interface
        self.ui = UI(screen)

    def change_coins(self, amount):
        self.coins_amount += amount

    def change_life(self, amount):
        self.life += amount

    def run(self):
        self.level.run()
        self.ui.show()
        self.ui.show_coins(self.coins_amount)
        self.ui.show_life(self.life)
        self.ui.show_turret_amount(len(self.level.turret_sprites.sprites()))


# Setup level
pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Tower Defence")
# pygame.mouse.set_visible(False)
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

    debug(pygame.mouse.get_pos(), 70)

    pygame.display.update()
    clock.tick(60)
