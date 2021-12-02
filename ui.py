import pygame
from settings import *


class UI:
    def __init__(self, surface):
        self.display_surface = surface

        self.center = 3.3333333333333333333333333333333

        # Font
        self.font = pygame.font.Font("graphics/ui/Gamer.ttf", 30)

        # Topbar
        self.topbar_padding = 32
        self.topbar_size = (screen_width, 64)
        self.topbar_surf = pygame.Surface(self.topbar_size)
        self.topbar_surf.fill("#2A2A2A")

    def topbar(self):
        pass

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

    def show_stat_turret(self, turret_amount):
        stat_turret_text_surf = self.font.render(
            f"{turret_amount} TURRET", False, "white")
        stat_turret_text_rect = stat_turret_text_surf.get_rect(
            topright=(screen_width - self.topbar_padding, self.topbar_size[1] / self.center))
        self.display_surface.blit(stat_turret_text_surf, stat_turret_text_rect)

    def show(self):
        self.display_surface.blit(self.topbar_surf, (0, 0))
