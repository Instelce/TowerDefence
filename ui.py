import pygame
import sys

from settings import *
from game_data import turrets_data
from menu import *


class UI:
    def __init__(self, surface, quit_game, create_menu):
        self.display_surface = surface
        self.quit_game = quit_game
        self.create_menu = create_menu

        self.turrets_data = turrets_data

        self.clock = pygame.time.Clock()

        # Font
        self.font_size = 30
        self.font = pygame.font.Font("graphics/ui/Gamer.ttf", self.font_size)

        # Topbar
        self.topbar_padding = 32
        self.topbar_size = (screen_width, 64)
        self.topbar_surf = pygame.Surface(self.topbar_size)
        self.topbar_surf.fill("black")

        # Resume window
        self.pause = False
        self.resume_window = Menu(self.display_surface,
                                  "Pause",
                                  [
                                      Button(self.display_surface,
                                             self.resume_game, "Resume", 200, 50),
                                      Button(self.display_surface,
                                             self.create_menu, "Go to Menu", 200, 50),
                                      Button(self.display_surface,
                                             self.create_menu, "Settings", 200, 50),
                                      Button(self.display_surface,
                                             self.quit_game, "Quit", 200, 50),
                                  ]
                                  )

        # Turret panel
        self.turret_panel_size = (screen_width, 200)
        self.turret_panel_surf = pygame.Surface(self.turret_panel_size)
        self.turret_panel_rect = self.turret_panel_surf.get_rect(
            bottomleft=(0, screen_height))
        self.turret_panel_surf.fill("#2A2A2A")

        self.horizontal_center = self.topbar_size[1] / 2

        self.last_time = pygame.time.get_ticks()

    def topbar(self):
        pause_button = Button(self.display_surface,
                              self.draw_resume_window,
                              'Pause',
                              80, 40,
                              (screen_width - 100,
                               self.horizontal_center - 20))
        pause_button.draw(pause_button.pos)

    def show_coins(self, amount):
        coin_text_surf = self.font.render(str(amount), False, "white")
        coin_text_rect = coin_text_surf.get_rect(
            topleft=(self.topbar_padding, self.horizontal_center - self.font_size / 2))
        self.display_surface.blit(coin_text_surf, coin_text_rect)

    def show_life(self, amount):
        life_text_surf = self.font.render(str(amount), False, "white")
        life_text_rect = life_text_surf.get_rect(
            topleft=(self.topbar_padding * 4, self.horizontal_center - self.font_size / 2))
        self.display_surface.blit(life_text_surf, life_text_rect)

    def draw_resume_window(self):
        self.pause = True
        while self.pause:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.resume_window.run()

            pygame.display.update()
            self.clock.tick(5)

    def resume_game(self):
        self.pause = False

    def draw_turret_panel(self, change_turret_selected):
        for index, turret_type in enumerate(self.turrets_data):
            x_pos = ((screen_width / 2) -
                     (len(self.turrets_data) * 80) / 2) + index * 80
            y_pos = screen_height - 160
            selector_surf = pygame.Rect(x_pos, y_pos + 48, 80, 80)
            turret_button = Button(self.display_surface,
                                   self.no_callback,
                                   '',
                                   80,
                                   128,
                                   (x_pos, y_pos),
                                   self.turrets_data[turret_type]['card_normal'],
                                   self.turrets_data[turret_type]['card_hover'])
            turret_button.draw(turret_button.pos)
            if self.turrets_data[turret_type]['is_selected']:
                pygame.draw.rect(self.display_surface,
                                 "white", selector_surf, 2)

    def no_callback(self):
        return None

    def draw_wave_timer(self, wave_duration):
        timer_duration = pygame.time.set_timer(
            pygame.USEREVENT, wave_duration * 100)

        timer_surf = self.font.render(str(wave_duration), False, 'white')
        timer_rect = timer_surf.get_rect(
            center=(screen_height - 200, self.horizontal_center))

    def show(self):
        self.display_surface.blit(self.topbar_surf, (0, 0))
        # self.topbar()

        # self.display_surface.blit(
        # self.turret_panel_surf, self.turret_panel_rect)
