from combat import Action

characters = [
        {
        "name": "Durak the Barbarian",
        "type": "player",
        "level": 5,
        "hp": 90,
        "ac": 22,
        "attributes": {
            "strength": 15,
            "dexterity": 10,
            "constitution": 14,
            "intelligence": 8,
            "wisdom": 12,
            "charisma": 9
        },
        "proficiency_bonus": 3,
        "actions": [
            {
                "name": "Sword Attack",
                "action_type": "melee",
                "dice": "1d12+3",
                "to_hit_bonus": 5,
                "damage_bonus": 3
            }
        ]
    },
    {
        "name": "Red Dragon",
        "type": "monster",
        "level": 10,
        "hp": 50,
        "ac": 22,
        "attributes": {
            "strength": 18,
            "dexterity": 12,
            "constitution": 16,
            "intelligence": 12,
            "wisdom": 12,
            "charisma": 11
        },
        "proficiency_bonus": 5,
        "actions": [
            {
                "name": "Fire Breath",
                "action_type": "ranged",
                "dice": "2d10+2",
                "to_hit_bonus": 3,
                "damage_bonus": 2
            }
        ]
    }
]
