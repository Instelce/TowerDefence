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

# Turrets
turrets_data = {
    '01': {
        'category': 1,
        'card': 'graphics/turret/blue/01/card.png',
        'mk1': {
            'level': 1,
            'price': '20',
            'damage': '5',
            'upgrade': 'mk2',
            'fire': 'graphics/turret/blue/fire/01/mk1/',
            'idle': 'graphics/turret/blue/idle/01/mk1/',
        },
        'mk2': {
            'level': 2,
            'price': '25',
            'damage': '7',
            'upgrade': 'mk3',
            'fire': 'graphics/turret/blue/fire/01/mk2/',
            'idle': 'graphics/turret/blue/idle/01/mk2/',
        },
        'mk3': {
            'level': 3,
            'price': '30',
            'damage': '10',
            'upgrade': None,
            'fire': 'graphics/turret/blue/fire/01/mk3/',
            'idle': 'graphics/turret/blue/idle/01/mk3/',
        },
    },
    '02': {
        'category': 2,
        'card': 'graphics/turret/blue/02/card.png',
        'mk1': {
            'level': 1,
            'price': '20',
            'damage': '5',
            'upgrade': 'mk2',
            'fire': 'graphics/turret/blue/fire/02/mk1/',
            'idle': 'graphics/turret/blue/idle/02/mk1/',
        },
        'mk2': {
            'level': 2,
            'price': '25',
            'damage': '7',
            'upgrade': 'mk3',
            'fire': 'graphics/turret/blue/fire/02/mk2/',
            'idle': 'graphics/turret/blue/idle/02/mk2/',
        },
        'mk3': {
            'level': 3,
            'price': '30',
            'damage': '10',
            'upgrade': None,
            'fire': 'graphics/turret/blue/fire/02/mk3/',
            'idle': 'graphics/turret/blue/idle/02/mk3/',
        }
    },
}
