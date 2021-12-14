import pygame
import sys

from settings import *
from level import Level
from menu import Menu, Button
from ui import UI
from debug import debug


class Game:
    def __init__(self):
        self.coins_amount = 100
        self.life = 20

        self.status = 'mendu'
        # self.start_menu = Menu(screen,
        #                        "Tower Defence",
        #                        [
        #                            Button(screen,
        #                                   self.create_level, "Start", 200, 50),
        #                            Button(screen,
        #                                   self.create_level, "Settings", 200, 50),
        #                            Button(screen,
        #                                   self.quit_game, "Quit", 200, 50)
        #                        ],
        #                        "graphics/ui/start_menu_banner.png",)

        self.level = Level(screen, self.coins_amount,
                           self.change_coins, self.change_life)

        # User interface
        self.ui = UI(screen, self.quit_game,
                     self.create_menu)

    def quit_game(self):
        pygame.quit()
        sys.exit()

    def change_coins(self, amount):
        self.coins_amount += amount

    def change_life(self, amount):
        self.life += amount

    def create_menu(self):
        self.start_menu = Menu(screen,
                               "Tower Defence",
                               [
                                   Button(screen,
                                          self.create_level, "Start", 200, 50),
                                   Button(screen,
                                          self.create_level, "Settings", 200, 50),
                                   Button(screen,
                                          self.quit_game, "Quit", 200, 50)
                               ],
                               "graphics/ui/start_menu_banner.png",)
        self.status = 'menu'

    def create_level(self):
        self.level = Level(screen, self.coins_amount,
                           self.change_coins, self.change_life)
        self.status = 'level'

    def run(self):
        if self.status == 'menu':
            self.start_menu.run()
        else:
            self.level.run()
            self.ui.show()
            self.ui.show_coins(self.coins_amount)
            self.ui.show_life(self.life)


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
