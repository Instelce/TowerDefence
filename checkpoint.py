import pygame


class Checkpoint(pygame.sprite.Sprite):
    def __init__(self, size, x, y):
        super(Checkpoint, self).__init__()
        self.image = pygame.Surface((size, size))
        self.image.fill('yellow')
        self.rect = self.image.get_rect(topleft=(x, y))
        self.pos = (x, y)
        self.size = size

    def get_pos(self):
        return (self.pos[0] + int(self.size / 2), self.pos[1] + int(self.size / 2))
