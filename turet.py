import pygame


class Bullet(pygame.sprite.Sprite):
    def __init__(self, turet, sbire_target):
        super().__init__()
        self.turet = turet
        self.sbire_target = sbire_target
        self.pos = turet.pos

        self.image = pygame.Surface((5, 5))
        self.image.fill("blue")
        self.rect = self.image.get_rect(center=self.pos)

        self.speed = 15

    def update(self):
        self.rect.center = self.pos


class Turet(pygame.sprite.Sprite):
    def __init__(self, size, pos, surface, price, range_size, range_ratio):
        """ 
        Constructor. 

        Args:
            size (int): Size of the turret
            pos (tupel): Position of the turret (x, y)
            range_size (int): size of the range

        """
        super().__init__()
        self.pos = pos
        self.size = size
        self.display_surface = surface
        self.price = price

        self.image = pygame.Surface((size, size))
        self.image.fill("#bcbcbc")
        self.rect = self.image.get_rect(center=self.pos)
        self.build_zone = pygame.Rect(
            self.pos[0] - int(size / 2), self.pos[1] - int(size / 2), size, size)

        self.shooting_range = pygame.Rect(
            self.rect.x - int(size * range_ratio), self.rect.y - int(size * range_ratio), range_size, range_size)
        self.is_shooting = False
        self.sbire_target = None
        self.shoot_speed = 400

    def update(self):
        if self.is_shooting == True:
            # Line
            self.start = pygame.math.Vector2(self.pos)
            self.end = pygame.math.Vector2(self.sbire_target.pos)
            pygame.draw.line(self.display_surface, "blue",
                             self.start, self.end, width=1)

        # Shooting range
        pygame.draw.rect(self.display_surface, "red", self.shooting_range, 2)
