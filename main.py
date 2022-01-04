import pygame
import sys

from settings import *
from level import Level
from menu import Menu, Button
from ui import UI
from debug import debug
from game_data import turrets_data


class Game:
    def __init__(self):
        self.coins_amount = 100
        self.life = 5
        self.turret_selected = 1

        self.status = '-menu'
        self.start_menu = Menu(screen,
                               "Tower Defence",
                               [
                                   Button(screen,
                                          self.create_level, "Start", 200, 50),
                                   Button(screen,
                                          self.create_level, "Settings", 200, 50),
                                   Button(screen,
                                          self.quit_game, "Quit", 200, 50)
                               ])

        self.level = Level(screen, self.turret_selected, self.change_turret_selected, self.coins_amount,
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

    def change_turret_selected(self, choice):
        self.turret_selected = choice
        for turret_type in turrets_data:
            turrets_data[turret_type]['is_selected'] = False
        turrets_data[f"0{self.turret_selected}"]['is_selected'] = True

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
        self.level = Level(screen, self.turret_selected, self.change_turret_selected, self.coins_amount,
                           self.change_coins, self.change_life)
        self.status = 'level'

    def create_game_over_menu(self):
        self.game_over_menu = Menu(screen,
                                   "Game Over",
                                   [
                                       Button(screen,
                                              self.create_level, "Restart", 200, 50),
                                       Button(screen,
                                              self.create_menu, "Go to home", 200, 50),
                                       Button(screen,
                                              self.quit_game, "Quit", 200, 50)
                                   ])
        self.status = 'game_over_menu'

    def run(self):
        if self.status == 'menu':
            self.start_menu.run()
        elif self.status == 'game_over_menu':
            self.game_over_menu.run()
        else:
            self.level.run()
            self.ui.show()
            self.ui.show_coins(self.coins_amount)
            self.ui.show_life(self.life)
            self.ui.draw_turret_panel(self.change_turret_selected)

            if self.life <= 0:
                self.create_game_over_menu()


# Setup level
pygame.init()
screen = pygame.display.set_mode(
    (screen_width, screen_height), pygame.SCALED + pygame.RESIZABLE)
pygame.display.set_caption("Tower Defence")
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
