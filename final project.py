import random

class Humanoid:
    def __init__(self, height, weight, hair_color, eye_color, strength, dexterity, constitution, intelligence, wisdom, charisma):
        self.height = height
        
        self.weight = weight
        
        self.hair_color = hair_color
        
        self.eye_color = eye_color
        
        self.strength = strength
        
        self.dexterity = dexterity
        
        self.constitution = constitution
        
        self.intelligence = intelligence
        
        self.wisdom = wisdom
        
        self.charisma = charisma

class Human(Humanoid):
    def __init__(self, height, weight, hair_color, eye_color, strength, dexterity, constitution, intelligence, wisdom, charisma):
        super().__init__(height, weight, hair_color, eye_color, strength, dexterity, constitution, intelligence, wisdom, charisma)
        self.add_two_points()

    def add_two_points(self):
        attribute_choice = input("As a Human, you may add +2 bonus points to a single attribute of your choosing (Enter one of these: strength, dexterity, constitution, intelligence, wisdom, charisma): ").lower()
        if attribute_choice in ["strength", "dexterity", "constitution", "intelligence", "wisdom", "charisma"]:
            setattr(self, attribute_choice, getattr(self, attribute_choice) + 2)
        else:
            print("Invalid attribute choice. No points added.")

class Elf(Humanoid):
    def __init__(self, height, weight, hair_color, eye_color, strength, dexterity, constitution, intelligence, wisdom, charisma):
        super().__init__(height, weight, hair_color, eye_color, strength, dexterity, constitution, intelligence, wisdom, charisma)
        self.resistance_to_sleep = True
        self.dexterity += 2
        self.charisma += 2

class Dwarf(Humanoid):
    def __init__(self, height, weight, hair_color, eye_color, strength, dexterity, constitution, intelligence, wisdom, charisma):
        super().__init__(height, weight, hair_color, eye_color, strength, dexterity, constitution, intelligence, wisdom, charisma)
        self.magic_resistance = 20
        self.strength += 2
        self.constitution += 2
        self.charisma -= 2

def characterCreation():
    print("Welcome to The Final Time! GAME OF CHAMPIONS")
    print("You may choose from the following playable races:")
    print(" 1. Human\n 2. Elf\n 3. Dwarf")

    race_choice = input("Which race have you chosen for your starting character? ").lower()

    height = float(input("Please enter the height of your character from 3ft - 7ft: "))
    
    weight = float(input("Please enter the weight for your character from 60 - 300lbs: "))
    
    hair_color = input("Please enter the hair color for your character: ")
    
    eye_color = input("Please enter the eye color for your character: ")

    strength = random.randint(1, 18)
    
    dexterity = random.randint(1, 18)
    
    constitution = random.randint(1, 18)
    
    intelligence = random.randint(1, 18)
    
    wisdom = random.randint(1, 18)
    
    charisma = random.randint(1, 18)

    if race_choice == "1" or race_choice.lower() == "human":
        character = Human(height, weight, hair_color, eye_color, strength, dexterity, constitution, intelligence, wisdom, charisma)
    elif race_choice == "2" or race_choice.lower() == "elf":
        character = Elf(height, weight, hair_color, eye_color, strength, dexterity, constitution, intelligence, wisdom, charisma)
    elif race_choice == "3" or race_choice.lower() == "dwarf":
        character = Dwarf(height, weight, hair_color, eye_color, strength, dexterity, constitution, intelligence, wisdom, charisma)
    else:
        print("Invalid race choice.")
        return

    print("\n**** Now randomly rolling stat attributes for your character ****\n")

    print(f"You character has the following attributes:")
    
    print(f"\n Height: {character.height}ft\n Weight: {character.weight}lbs\n Hair Color: {character.hair_color}\n Eye Color: {character.eye_color}")
    
    print(f"\n Str: {character.strength}\n Dex: {character.dexterity}\n Con: {character.constitution}\n Int: {character.intelligence}\n Wis: {character.wisdom}\n Char: {character.charisma}")

    if isinstance(character, Human):
        character.add_two_points()

        print("\nYou character's final attributes are: ")
    
        print(f"\n Height: {character.height}ft\n Weight: {character.weight}lbs\n Hair Color: {character.hair_color}\n Eye Color: {character.eye_color}")
    
        print(f"\n Str: {character.strength}\n Dex: {character.dexterity}\n Con: {character.constitution}\n Int: {character.intelligence}\n Wis: {character.wisdom}\n Char: {character.charisma}")

def main():
    print("Welcome to the Final time! GAME OF CHAMPIONS")
    characterCreation()

if __name__ == "__main__":
    main()
