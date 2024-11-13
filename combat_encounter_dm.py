from character import PlayerCharacter, MonsterCharacter
import random

class CombatEncounterDM:
    def __init__(self, characters):
        self.characters = characters
        self.initiative_order = self.roll_initiative()
        self.round_count = 1

    def roll_initiative(self):
        return sorted(self.characters, key=lambda char: char.roll_initiative(), reverse=True)

    def start_combat(self):
        while not self.check_end_condition():
            print(f"--- Round {self.round_count} ---")
            for character in self.initiative_order:
                if character.is_alive():
                    self.take_turn(character)
            self.round_count += 1
        self.announce_winner()

    def take_turn(self, character):
        action = character.choose_action(self)
        target = random.choice([char for char in self.characters if char != character and char.is_alive()])
        result = action.execute(target)
        print(result)

    def check_end_condition(self):
        players_alive = any(isinstance(char, PlayerCharacter) and char.is_alive() for char in self.characters)
        monsters_alive = any(isinstance(char, MonsterCharacter) and char.is_alive() for char in self.characters)
        return not (players_alive and monsters_alive)

    def announce_winner(self):
        players_alive = [char for char in self.characters if isinstance(char, PlayerCharacter) and char.is_alive()]
        monsters_alive = [char for char in self.characters if isinstance(char, MonsterCharacter) and char.is_alive()]

        if players_alive:
            winner = "Players"
            survivors = players_alive
        else:
            winner = "Monsters"
            survivors = monsters_alive

        total_hp = sum(char.hp for char in survivors)
        survivor_names = ', '.join([char.name for char in survivors])
        
        print(f"\n--- Combat Encounter Ended ---")
        print(f"Winner: {winner}")
        print(f"Survivors: {survivor_names}")
        print(f"Remaining total HP of the winning side: {total_hp}")
