from os import walk
import pygame
from csv import reader
from settings import tile_size


def import_csv_layout(path):
    terrain_map = []

    with open(path) as map:
        level = reader(map, delimiter=',')
        for row in level:
            terrain_map.append(list(row))
        return terrain_map
