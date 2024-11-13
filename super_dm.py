from data.characters import characters
from character import PlayerCharacter, MonsterCharacter
from combat_encounter_dm import CombatEncounterDM

class SuperDM:
    def __init__(self):
        self.characters = self.load_characters()
        self.combat_encounter = CombatEncounterDM(self.characters)

    def load_characters(self):
        character_objects = []
        for char_data in characters:
            if char_data["type"] == "player":
                character_objects.append(PlayerCharacter.from_data(char_data))
            else:
                character_objects.append(MonsterCharacter.from_data(char_data))
        return character_objects


    def start_encounter(self):
        print("Starting combat encounter!")
        self.combat_encounter.start_combat()
