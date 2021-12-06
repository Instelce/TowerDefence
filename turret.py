import pygame
import math
from random import randint

from support import import_folder


class Bullet(pygame.sprite.Sprite):
    def __init__(self, turret, sbire_target):
        super().__init__()
        self.turret = turret
        self.sbire_target = sbire_target
        self.pos = turret.pos

        self.image = pygame.Surface((5, 5))
        self.image.fill("blue")
        self.rect = self.image.get_rect(center=self.pos)

        self.speed = 15

    def update(self):
        self.rect.center = self.pos


class Turret(pygame.sprite.Sprite):
    def __init__(self, size, pos, surface, price, range_size, range_ratio):
        """
        Constructor.

        Args:
            size (int): Size of the turret
            pos (tupel): Position of the turret (x, y)
            range_size (int): size of the range

        """
        super().__init__()
        self.import_turret_assets()

        # Setup
        self.pos = pos
        self.size = size
        self.display_surface = surface
        self.price = price

        # Animations
        self.frame_index = 0
        self.animation_speed = 0.20
        self.status = 'idle'

        # Image and pos
        self.is_leafy = 0
        self.image = self.animations[self.status][self.frame_index]
        self.rect = self.image.get_rect(center=self.pos)
        self.build_zone = pygame.Rect(
            self.pos[0] - int(size / 2), self.pos[1] - int(size / 2), size, size)

        if self.is_leafy == 0:
            self.wall = pygame.image.load(
                'graphics/turret/blue/towers_wall.png')
        elif self.is_leafy == 1:
            self.wall = pygame.image.load(
                'graphics/turret/blue/towers_wall_leafy.png')

        # Shoot
        self.shooting_range = pygame.Rect(
            self.rect.x - int(size * range_ratio), self.rect.y - int(size * range_ratio), range_size, range_size)
        self.is_shooting = False
        self.sbire_target = None
        self.shoot_speed = 400

    def import_turret_assets(self):
        turret_path = 'graphics/turret/blue/'
        self.animations = {'idle': [], 'fire': []}

        for animation in self.animations.keys():
            full_path = turret_path + animation
            self.animations[animation] = import_folder(full_path, True, 'mk2')

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

    def update(self):
        self.animate()
        self.get_status()
        self.rotate()

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
