import pygame

from support import import_folder


class Sbire(pygame.sprite.Sprite):
    def __init__(self, surface, size, pos, health, coins_reward):
        super().__init__()
        self.import_sbire_assets()

        self.pos = pos
        self.size = size
        self.display_surface = surface
        self.coins_reward = coins_reward

        self.status = 'run'
        self.frame_index = 0
        self.animation_speed = 0.20
        self.image = self.animations[self.status][self.frame_index]
        self.rect = self.image.get_rect(center=self.pos)
        self.detection_zone = pygame.Rect(
            self.pos[0] - int(size / 2), self.pos[1] - int(size / 2), size, size)

        self.checkpoint_target = 0
        self.speed = 4

        # Health management
        self.max_health = health
        self.current_health = health

        # Health bar container
        self.bar_max_width = size + 10

        self.health_bar = pygame.Surface((self.bar_max_width, 5))
        self.health_bar.fill("#000000")

    def import_sbire_assets(self):
        sbire_path = 'graphics/sbire/'
        self.animations = {'run': []}

        for animation in self.animations.keys():
            full_path = sbire_path + animation
            self.animations[animation] = import_folder(full_path, 32)

    def animate(self):
        animation = self.animations[self.status]

        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0

        self.image = pygame.transform.rotate(
            animation[int(self.frame_index)], -180)

        # Rotate sbire
        if self.checkpoint_target % 2 == 0:
            self.image = pygame.transform.rotate(
                self.image, 90)
            self.rect = self.image.get_rect(center=self.pos)
        else:
            self.image = pygame.transform.rotate(
                self.image, -90)
            self.rect = self.image.get_rect(center=self.pos)

    def draw_health_bar(self, current_health, full):
        self.health_bar_center = (
            self.pos[0] - int(self.bar_max_width / 2), self.pos[1] + 30)

        self.display_surface.blit(self.health_bar, self.health_bar_center)

        current_health_ratio = current_health / full
        current_bar_width = self.bar_max_width * current_health_ratio
        health_bar_rect = pygame.Rect(
            self.health_bar_center, (current_bar_width, self.health_bar.get_height()))

        pygame.draw.rect(self.display_surface, '#F63737', health_bar_rect)

    def take_damage(self, amount):
        self.current_health += amount

    def update(self):
        self.animate()
        self.rect.center = self.pos
        self.draw_health_bar(self.current_health, self.max_health)
