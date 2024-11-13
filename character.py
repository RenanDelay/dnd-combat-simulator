from combat import Action
from utils import roll_dice

class Character:
    def __init__(self, name, level, hp, ac, attributes, proficiency_bonus, actions):
        self.name = name
        self.level = level
        self.hp = hp
        self.ac = ac
        self.attributes = attributes
        self.proficiency_bonus = proficiency_bonus
        self.actions = [Action(**action) for action in actions]

    @classmethod
    def from_data(cls, character_data):
        return cls(
            name=character_data["name"],
            level=character_data["level"],
            hp=character_data["hp"],
            ac=character_data["ac"],
            attributes=character_data["attributes"],
            proficiency_bonus=character_data["proficiency_bonus"],
            actions=character_data["actions"]
        )

    def attribute_modifier(self, attribute):
        return (self.attributes[attribute] - 10) // 2

    def is_alive(self):
        return self.hp > 0

    def roll_initiative(self):
        return roll_dice("1d20", False) + self.attribute_modifier("dexterity")

    def choose_action(self, dm):
        return self.actions[0]

class PlayerCharacter(Character):
    pass

class MonsterCharacter(Character):
    pass
