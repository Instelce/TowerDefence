import pygame
import math
from random import randint

from settings import *
from support import import_folder
from menu import Button


class Bullet(pygame.sprite.Sprite):
    def __init__(self, turret, sbire_target, image_path):
        super().__init__()
        self.turret = turret
        self.sbire_target = sbire_target
        self.pos = turret.pos

        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect(center=self.pos)

        self.speed = 15

    def update(self):
        self.rect.center = self.pos


class Turret(pygame.sprite.Sprite):
    def __init__(self, size, pos, surface, price, damage, range_size, range_ratio, idle_path, fire_path, bullet_path):
        """
        Constructor.

        Args:
            size (int): Size of the turret
            pos (tupel): Position of the turret (x, y)
            range_size (int): size of the range

        """
        super().__init__()
        self.animations_path = {
            'idle': idle_path,
            'fire': fire_path,
        }

        self.import_turret_assets()

        # Setup
        self.pos = pos
        self.size = size
        self.display_surface = surface
        self.price = price
        self.damage = damage
        self.bullet_path = bullet_path

        # Animations
        self.frame_index = 0
        self.animation_speed = 0.2
        self.status = 'idle'

        # Image and pos
        self.image = self.animations[self.status][self.frame_index]
        self.rect = self.image.get_rect(center=self.pos)
        self.build_zone = pygame.Rect(
            self.pos[0] - int(size / 2), self.pos[1] - int(size / 2), size, size)
        self.wall = pygame.image.load(
            'graphics/turret/turret_wall.png')

        # Shoot
        self.shooting_range = pygame.Rect(
            self.rect.x - int(size * range_ratio), self.rect.y - int(size * range_ratio), range_size, range_size)
        self.is_shooting = False
        self.sbire_target = None
        self.shoot_speed = 400

        # UI
        self.is_ui_show = False

    def import_turret_assets(self):
        self.animations = {'idle': [], 'fire': []}

        for animation in self.animations.keys():
            full_path = self.animations_path[animation]
            print(full_path)
            self.animations[animation] = import_folder(full_path)

    def animate(self):
        animation = self.animations[self.status]

        # Loop over frame index
        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0

        self.image = animation[int(self.frame_index)]

    def get_status(self):
        if self.is_shooting:
            self.status = 'fire'
        else:
            self.status = 'idle'

    def rotate(self):
        correction_angle = 90

        if self.is_shooting:
            sx, sy = self.sbire_target.pos
            dx, dy = sx - self.rect.centerx, sy - self.rect.centery
            angle = math.degrees(math.atan2(-dy, dx)) - correction_angle

            self.image = pygame.transform.rotate(self.image, angle)
            self.rect = self.image.get_rect(center=self.pos)

        self.image = pygame.transform.rotate(self.image, 0)
        self.rect = self.image.get_rect(center=self.pos)

    def show_turret_ui(self):
        width = 3 * tile_size
        height = 2 * tile_size
        keys = pygame.key.get_pressed()
        mouse_pos = pygame.mouse.get_pos()

        # Container
        container_surf = pygame.image.load(
            'graphics/turret/ui/frame.png').convert_alpha()
        container_rect = container_surf.get_rect(
            center=(self.rect.x + 32, self.rect.y - 74))

        # Upgrade button
        upgrade_button = Button(
            container_surf, self.upgrade, '', 160, 32, (16, height - (32 + 16)), 'graphics/turret/ui/upgrade_button/upgrade_button_normal.png', 'graphics/turret/ui/upgrade_button/upgrade_button_hover.png')
        upgrade_button.draw(upgrade_button.pos)

        # If mouse collide turret
        if self.rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0]:
                self.is_ui_show = True
        if keys[pygame.K_ESCAPE]:
            self.is_ui_show = False

        if self.is_ui_show:
            self.display_surface.blit(container_surf, container_rect)

    def upgrade(self):
        pass

    def update(self):
        self.animate()
        self.get_status()
        self.rotate()
        self.show_turret_ui()

        self.display_surface.blit(
            self.wall, self.wall.get_rect(center=self.pos))

        if self.is_shooting == True:
            # Line
            self.start = pygame.math.Vector2(self.pos)
            self.end = pygame.math.Vector2(self.sbire_target.pos)
            pygame.draw.line(self.display_surface, "blue",
                             self.start, self.end, width=1)

        # Shooting range
        pygame.draw.rect(self.display_surface, "red", self.shooting_range, 2)
