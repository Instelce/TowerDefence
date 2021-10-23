import pygame

from checkpoint import Checkpoint
from settings import *
from support import *
from game_data import levels


class Level:
    def __init__(self, surface):
        super(Level, self).__init__()
        self.display_surface = surface

        # Levels data
        self.current_level = 0
        level_data = levels[self.current_level]

        # Checkpoint
        checkpoint_layout = import_csv_layout(level_data['checkpoints'])
        self.checkpoint_sprites = self.create_tile_group(
            checkpoint_layout, 'checkpoints')

    def create_tile_group(self, layout, type):
        sprite_group = pygame.sprite.Group()

        for row_index, row in enumerate(layout):
            for col_index, val in enumerate(row):
                if val != '-1':
                    x = col_index * tile_size
                    y = row_index * tile_size

                    if type == 'checkpoints':
                        sprite = Checkpoint(tile_size, x, y)

                    sprite_group.add(sprite)
        return sprite_group

    def draw_paths(self):
        self.points = [self.checkpoint_sprites.sprites()[index].get_pos()
                       for index, node in enumerate(self.checkpoint_sprites)]
        pygame.draw.lines(self.display_surface,
                          '#a04f45', False, self.points, 6)

    def run(self):
        self.draw_paths()

        # Checkpoint
        self.checkpoint_sprites.draw(self.display_surface)
