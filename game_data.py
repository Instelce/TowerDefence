from settings import *


# Levels
level_0 = {
    'wave': [4, 6, 2],
    'checkpoints': 'levels/0/level_0_checkpoints.csv',
    'terrain': 'levels/0/level_0_terrain.csv',
    'road': 'levels/0/level_0_road.csv',
}

levels = {
    0: level_0
}


# Sounds
sounds_path = {
    'hit': 'sound/hit.wav',
    'select': 'sound/select.wav',
    'shoot': 'sound/shoot.wav',
    'turret_spawn': 'sound/turret_spawn.wav',
}

# Turrets
turrets_levels = {
    1: 'graphics/turret/level/1.png',
    2: 'graphics/turret/level/2.png',
    3: 'graphics/turret/level/3.png',
}

turrets_data = {
    '01': {
        'category': 1,
        'is_selected': True,
        'card_normal': 'graphics/turret/cards/normal/card_normal_0.png',
        'card_hover': 'graphics/turret/cards/hover/card_hover_0.png',

        'price': 20,

        'levels_stats': {
            1: {
                'damage': 5,
                'range_size': tile_size * 5,
                'range_ratio': 2,
            },
            2: {
                'damage': 8,
                'range_size': tile_size * 5,
                'range_ratio': 2,
            },
            3: {
                'damage': 8,
                'range_size': tile_size * 7,
                'range_ratio': 3,
            },
        },

        'levels_price': {
            2: 25,
            3: 30
        },

        'fire': 'graphics/turret/fire/01/',
        'idle': 'graphics/turret/idle/01/',
        'bullet_path': 'graphics/turret/bullet/01/bullet_01.png',

    },
    '02': {
        'category': 2,
        'is_selected': False,
        'card_normal': 'graphics/turret/cards/normal/card_normal_1.png',
        'card_hover': 'graphics/turret/cards/hover/card_hover_1.png',

        'damage': 10,
        'range_size': tile_size * 3,
        'range_ratio': 1,
        'price': 25,

        'levels_stats': {
            1: {
                'damage': 10,
                'range_size': tile_size * 3,
                'range_ratio': 1,
            },
            2: {
                'damage': 15,
                'range_size': tile_size * 3,
                'range_ratio': 1,
            },
            3: {
                'damage': 20,
                'range_size': tile_size * 5,
                'range_ratio': 2,
            },
        },

        'levels_price': {
            2: 30,
            3: 40
        },

        'fire': 'graphics/turret/fire/02/',
        'idle': 'graphics/turret/idle/02/',
        'bullet_path': 'graphics/turret/bullet/02/bullet_02.png',
    },
    '03': {
        'category': 3,
        'is_selected': False,
        'card_normal': 'graphics/turret/cards/normal/card_normal_2.png',
        'card_hover': 'graphics/turret/cards/hover/card_hover_2.png',

        'price': 30,

        'levels_stats': {
            1: {
                'damage': 10,
                'range_size': tile_size * 7,
                'range_ratio': 3,
            },
            2: {
                'damage': 12,
                'range_size': tile_size * 7,
                'range_ratio': 3,
            },
            3: {
                'damage': 15,
                'range_size': tile_size * 7,
                'range_ratio': 3,
            },
        },

        'levels_price': {
            2: 35,
            3: 40
        },

        'fire': 'graphics/turret/fire/03/',
        'idle': 'graphics/turret/idle/03/',
        'bullet_path': 'graphics/turret/bullet/03/bullet_03.png',
    },
}
