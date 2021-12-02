import pygame


class Sbire(pygame.sprite.Sprite):
    def __init__(self, surface, size, pos, health):
        super().__init__()
        self.pos = pos
        self.size = size
        self.display_surface = surface

        self.image = pygame.Surface((size, size))
        self.image.fill('orange')
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
        self.health_bar.fill("#FFFFFF")

    def draw_health_bar(self, current_health, full):
        self.health_bar_center = (
            self.pos[0] - int(self.bar_max_width / 2), self.pos[1] + 25)

        self.display_surface.blit(self.health_bar, self.health_bar_center)

        current_health_ratio = current_health / full
        current_bar_width = self.bar_max_width * current_health_ratio
        health_bar_rect = pygame.Rect(
            self.health_bar_center, (current_bar_width, self.health_bar.get_height()))

        pygame.draw.rect(self.display_surface, '#F63737', health_bar_rect)

    def take_damage(self, amount):
        self.current_health += amount

    def update(self):
        self.rect.center = self.pos
        self.draw_health_bar(self.current_health, self.max_health)
