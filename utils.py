import random

def roll_dice(dice_string, crit):
    num_dice, rest = dice_string.split("d")
    num_dice = int(num_dice)
    
    if "+" in rest:
        dice_type, modifier = rest.split("+")
        modifier = int(modifier)
    elif "-" in rest:
        dice_type, modifier = rest.split("-")
        modifier = -int(modifier)
    else:
        dice_type = rest
        modifier = 0 
    
    dice_type = int(dice_type)

    if crit == True:
        total = (dice_type * num_dice) + sum(random.randint(1, dice_type) for _ in range(num_dice)) + modifier
    else:
        total = sum(random.randint(1, dice_type) for _ in range(num_dice)) + modifier
    return total
