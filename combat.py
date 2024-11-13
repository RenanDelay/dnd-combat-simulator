# combat.py

from utils import roll_dice

class Combat:
    def __init__(self, name, action_type):
        self.name = name
        self.action_type = action_type

    def execute(self, target):
        raise NotImplementedError("Subclasses should implement this method.")

class Action(Combat):
    def __init__(self, name, action_type, dice, to_hit_bonus=0, damage_bonus=0):
        super().__init__(name, action_type)
        self.dice = dice
        self.to_hit_bonus = to_hit_bonus
        self.damage_bonus = damage_bonus

    def execute(self, target):
        dice_result = roll_dice("1d20", False)
        hit_roll = dice_result + self.to_hit_bonus
        crit = dice_result == 20
        if hit_roll >= target.ac:
            damage = roll_dice(self.dice, crit) + self.damage_bonus
            target.hp -= damage
            return f"rolled {dice_result}, {self.name} hits {target.name} for {damage} damage!"
        else:
            return f"rolled {dice_result}, {self.name} misses {target.name}."
