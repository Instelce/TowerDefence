import pygame
from settings import *
from game_data import turrets_data


class UI:
    def __init__(self, surface):
        self.display_surface = surface

        self.turrets_data = turrets_data

        self.center = 3.3333333333333333333333333333333

        # Font
        self.font = pygame.font.Font("graphics/ui/Gamer.ttf", 30)

        # Topbar
        self.topbar_padding = 32
        self.topbar_size = (screen_width, 64)
        self.topbar_surf = pygame.Surface(self.topbar_size)
        self.topbar_surf.fill("#2A2A2A")

        # Turret panel
        self.turret_panel_size = (screen_width, 200)
        self.turret_panel_surf = pygame.Surface(self.turret_panel_size)
        self.turret_panel_rect = self.turret_panel_surf.get_rect(
            bottomleft=(0, screen_height))
        self.turret_panel_surf.fill("#2A2A2A")

    def show_coins(self, amount):
        coin_text_surf = self.font.render(str(amount), False, "white")
        coin_text_rect = coin_text_surf.get_rect(
            topleft=(self.topbar_padding, self.topbar_size[1] / self.center))
        self.display_surface.blit(coin_text_surf, coin_text_rect)

    def show_life(self, amount):
        life_text_surf = self.font.render(str(amount), False, "white")
        life_text_rect = life_text_surf.get_rect(
            topleft=(self.topbar_padding * 4, self.topbar_size[1] / self.center))
        self.display_surface.blit(life_text_surf, life_text_rect)

    def show_turret_amount(self, turret_amount):
        stat_turret_text_surf = self.font.render(
            f"{turret_amount} TURRET", False, "white")
        stat_turret_text_rect = stat_turret_text_surf.get_rect(
            topright=(screen_width - self.topbar_padding, self.topbar_size[1] / self.center))
        self.display_surface.blit(stat_turret_text_surf, stat_turret_text_rect)

    def turret_panel(self):
        pass

    def show(self):
        self.display_surface.blit(self.topbar_surf, (0, 0))
        # self.display_surface.blit(
            # self.turret_panel_surf, self.turret_panel_rect)


class Button:
    def __init__(self):
        pass
