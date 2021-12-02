import pygame


class Tile(pygame.sprite.Sprite):
    def __init__(self, size, x, y):
        """ 
        Constructor. 
        
        Args:
            size (int): Size of the tile
            x (int): x position
            y (int): y position

        """
        super().__init__()
        self.size = size
        self.pos = (x, y)
        self.image = pygame.Surface((size, size))
        self.image.fill("purple")
        self.rect = self.image.get_rect(topleft=(x, y))


class Checkpoint(Tile):
    def __init__(self, size, x, y, sbire_speed):
        super(Checkpoint, self).__init__(size, x, y)

        self.detection_zone = pygame.Rect(self.rect.centerx - (
            sbire_speed / 2), self.rect.centery - (sbire_speed / 2), sbire_speed, sbire_speed)

    def get_pos(self):
        return (self.pos[0] + int(self.size / 2), self.pos[1] + int(self.size / 2))
