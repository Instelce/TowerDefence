import pygame

from tiles import *
from settings import *
from support import *
from game_data import levels
from sbire import Sbire
from turet import *
from random import randint
from time import sleep


class Level:
    def __init__(self, surface, coins_amount, change_coins, change_life):
        super(Level, self).__init__()
        self.display_surface = surface

        # Levels data
        self.current_level = 0
        self.level_data = levels[self.current_level]

        # User interface connexion
        self.coins_amount = coins_amount
        self.change_coins = change_coins
        self.change_life = change_life

        # Checkpoint and sbire setup
        self.sbire_speed = 4
        self.sbire_moving = True
        self.sbire_sprites = pygame.sprite.Group()
        checkpoint_layout = import_csv_layout(self.level_data['checkpoints'])
        self.setup_checkpoint(checkpoint_layout, self.sbire_speed)
        self.checkpoint_index = 0

        # List of pos checkpoints
        self.points = [self.checkpoint_sprites.sprites()[index].get_pos()
                       for index, node in enumerate(self.checkpoint_sprites)]

        # Wave managements
        self.last_time = pygame.time.get_ticks()

        # Turet
        self.tile_is_build = False
        self.turet_sprites = pygame.sprite.Group()

        # Bullet
        self.bullet_last_time = pygame.time.get_ticks()
        self.bullet_sprites = pygame.sprite.Group()

    def input(self):
        keys = pygame.key.get_pressed()
        now = pygame.time.get_ticks()

        if keys[pygame.K_SPACE]:
            self.wave_management(self.level_data['wave'])
        elif keys[pygame.K_a] and now - self.last_time >= 500:
            self.last_time = now
            self.create_sbire()
        elif pygame.mouse.get_pressed() == (1, 0, 0):
            self.create_turet()
        elif pygame.mouse.get_pressed() == (0, 0, 1):
            self.delete_turet()

    def create_tile_group(self, layout, type, sbire_speed):
        sprite_group = pygame.sprite.Group()

        for row_index, row in enumerate(layout):
            for col_index, val in enumerate(row):
                if val != '-1':
                    x = col_index * tile_size
                    y = row_index * tile_size

                    if type == 'checkpoints':
                        sprite = Checkpoint(tile_size, x, y, sbire_speed)

                    sprite_group.add(sprite)
        return sprite_group

    def setup_checkpoint(self, layout, sbire_speed):
        self.checkpoint_sprites = pygame.sprite.Group()

        for row_index, row in enumerate(layout):
            for col_index, val in enumerate(row):
                if val != '-1':
                    x = col_index * tile_size
                    y = row_index * tile_size + 64

                    sprite = Checkpoint(tile_size, x, y, sbire_speed)
                    self.checkpoint_sprites.add(sprite)

    def grid(self):
        self.grid_sprites = []
        for x in range(0, screen_width, tile_size):
            for y in range(0, screen_height, tile_size):
                grid_tile = pygame.Rect(x, y, tile_size, tile_size)
                self.grid_sprites.append(grid_tile)

        for tile in self.grid_sprites:
            mouse_pos = pygame.mouse.get_pos()
            border_size = 4

            if tile.collidepoint(mouse_pos):
                self.grid_tile_selected = tile

                for turet in self.turet_sprites:
                    if turet.build_zone.collidepoint((tile.x, tile.y)):
                        self.tile_is_build = True
                    else:
                        self.tile_is_build = False

                if self.tile_is_build:
                    pygame.draw.rect(self.display_surface,
                                     "red", tile, border_size)
                else:
                    pygame.draw.rect(self.display_surface,
                                     "white", tile, border_size)

            else:
                pygame.draw.rect(self.display_surface,
                                 "black", tile, 0)

    def wave_management(self, wave_data):
        now = pygame.time.get_ticks()
        wave_index = 1
        sbire_index = 0
        start_wave = True
        sbire_count = wave_data[wave_index]

        for sbire in range(sbire_count):
            self.create_sbire()

        print(f"Now {now} - Last {self.last_time} = {now - self.last_time} ")
        print(
            f"Sbire count: {sbire_index} / {sbire_count} for wave {wave_index}")

    def create_sbire(self):
        sbire = Sbire(self.display_surface, 32, self.points[0], 15)
        self.sbire_sprites.add(sbire)

    def get_sprite_movement(self, start_pos, end_pos):
        start = pygame.math.Vector2(start_pos)
        end = pygame.math.Vector2(end_pos)

        return (end - start).normalize()

    def apply_sbire_movement(self):
        self.all_sbire_direction = []
        self.all_target_checkpoint = []

        # Insert sbire data in list
        for sbire in self.sbire_sprites:
            self.all_sbire_direction.append(self.get_sprite_movement(
                self.points[sbire.checkpoint_target], self.points[sbire.checkpoint_target + 1]))
            self.all_target_checkpoint.append(self.checkpoint_sprites.sprites()[
                                              sbire.checkpoint_target + 1])

        # For all directions of all sprites apply movement
        for index, sbire_direction in enumerate(self.all_sbire_direction):
            sbire = self.sbire_sprites.sprites()[index]
            sbire.pos += sbire_direction * sbire.speed

            print(
                f"Checkpoint : {sbire.checkpoint_target} / {len(self.points) - 2}")

            # Check if the sbire touch a checkpoint
            if self.all_target_checkpoint[index].detection_zone.collidepoint(sbire.pos) and sbire.checkpoint_target < len(self.points) - 2:
                sbire.checkpoint_target += 1

            # Check if the sbire is not on the screen or if the sbire was dead
            if sbire.pos[0] > screen_width:
                self.change_life(-1)
                self.all_sbire_direction.remove(sbire_direction)
                self.all_target_checkpoint.remove(
                    self.all_target_checkpoint[index])
                sbire.kill()

            elif sbire.current_health <= 0:
                self.all_sbire_direction.remove(sbire_direction)
                self.all_target_checkpoint.remove(
                    self.all_target_checkpoint[index])
                sbire.kill()

    def draw_paths(self):
        pygame.draw.lines(self.display_surface,
                          'purple', False, self.points, 6)

    def create_turet(self):
        if self.coins_amount > 0:
            if self.tile_is_build:
                self.change_coins(0)
            else:
                pos = self.grid_tile_selected.center
                turet = Turet(64, pos, self.display_surface,
                              20, 3 * tile_size, 1)

                self.coins_amount -= turet.price
                self.change_coins(-turet.price)

                self.turet_sprites.add(turet)

    def delete_turet(self):
        pos = self.grid_tile_selected.center
        for turet in self.turet_sprites:
            if turet.build_zone.collidepoint(pos):
                self.coins_amount += turet.price
                self.change_coins(turet.price)
                turet.kill()
            if len(self.turet_sprites.sprites()) == 0:
                self.tile_is_build = False

    def create_bullet(self, turet, sbire_target):
        bullet = Bullet(turet, sbire_target)
        self.bullet_sprites.add(bullet)

    def turet_detection(self):
        for turet in self.turet_sprites:
            for sbire in self.sbire_sprites:
                if turet.shooting_range.collidepoint((sbire.pos[0], sbire.pos[1])):
                    now = pygame.time.get_ticks()

                    if now - self.bullet_last_time >= turet.shoot_speed:
                        self.bullet_last_time = now
                        self.create_bullet(turet, sbire)
                        print("SHOOT")

                    turet.sbire_target = sbire
                    turet.is_shooting = True
                else:
                    turet.sbire_target = None
                    turet.is_shooting = False

    def apply_bullet_movement(self):
        self.all_bullet_direction = []

        # Insert bullet data in list
        for bullet in self.bullet_sprites:
            self.all_bullet_direction.append(
                self.get_sprite_movement(bullet.turet.pos, bullet.sbire_target.pos))

        for index, bullet_direction in enumerate(self.all_bullet_direction):
            bullet = self.bullet_sprites.sprites()[index]
            bullet.pos += bullet_direction * bullet.speed

            # print(
            # f"[{index}] {bullet} | TARGET > {bullet.sbire_target} | POS > {bullet.pos}")

            if pygame.sprite.spritecollide(bullet, self.sbire_sprites, False):
                self.all_bullet_direction.remove(bullet_direction)

                bullet.sbire_target.take_damage(-5)
                bullet.kill()

    def run(self):
        self.input()
        self.grid()
        self.draw_paths()
        self.turet_detection()
        self.apply_sbire_movement()
        self.apply_bullet_movement()

        print(
            f"Sbire : {len(self.sbire_sprites.sprites())} | Turet : {len(self.turet_sprites.sprites())} | Bullet : {len(self.bullet_sprites.sprites())}")

        # Checkpoint
        self.checkpoint_sprites.draw(self.display_surface)

        # Sbire
        self.sbire_sprites.update()
        self.sbire_sprites.draw(self.display_surface)

        # Turet
        self.turet_sprites.update()
        self.turet_sprites.draw(self.display_surface)

        # Bullet
        self.bullet_sprites.update()
        self.bullet_sprites.draw(self.display_surface)
