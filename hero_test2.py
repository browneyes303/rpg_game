# In this simple RPG game, the hero fights the goblin. He has the options to:

# 1. fight goblin
# 2. do nothing - in which case the goblin will attack him anyway
# 3. flee

import random

class Character:
    def __init__(self, health, power):
        self.health = health
        self.power = power

    def alive(self):
        if self.health > 0:
            return True
        else:
            return False

    def attack(self, enemy):
        def attack_status(self):
            print(f"You do {self.power} damage to the {enemy.character_name}.")

        if (self.character_name == "hero"): # HERO doubles power 20% of the time
            hero_roll = 1 # random.randint(1,5)
            if self.character_name != "shadow":
                hero_roll = 1 # random.randint(1,5)
                if hero_roll == 1:
                    self.power = int(self.power*2)
                    enemy.health -= self.power
                    attack_status(self)
                    self.power = int(self.power/2)
                else:
                    enemy.health -= self.power
            elif self.character_name != "shadow": 
                hero_roll == 1
                self.power = int(self.power*2)
                enemy.health -= self.power
                self.power = int(self.power/2)
            else:
                enemy.health -= self.power
                attack_status(self)

        elif (self.character_name == "goblin"): # GOBLIN does nothing extra
            enemy.health -= self.power
            print(f"The {self.character_name} does {self.power} damage to you.")

        elif (self.character_name == "medic"): # MEDIC adds 2 health points 20% of the time
            medic_roll = random.randint(1,5)
            if medic_roll == 5:
                self.health += 2
            enemy.health -= self.power  # medic attacks hero
            print(f"The {self.character_name} does {self.power} damage to you.")

        elif (self.character_name == "shadow"): # SHADOW only takes damage 10% of the time
            shadow_roll = 1 #random.randint(1,10)
            if shadow_roll == 10:
                print(f"You do {enemy.power} damage to the {self.character_name}.") # shadow takes a hit
            else:
                self.health += enemy.power    # shadow doesn't lose health
                print(f"You do zero damage to the {self.character_name}")
            enemy.health -= self.power          # shadow attacks hero

# zombie
        elif (self.character_name == "zombie"): 
            enemy.health -= self.power
            attack_status()
# wizard
# dragon

    def print_status(self):
        if (self.character_name == "hero"):
            print(f"You have {self.health} health and {self.power} power.")
        elif (self.character_name == "goblin"):
            print(f"The {self.character_name} has {self.health} health and {self.power} power.")
        elif (self.character_name == "medic"):
            print(f"The {self.character_name} has {self.health} health and {self.power} power.")
        elif (self.character_name == "shadow"):
            print(f"The {self.character_name} has {self.health} health and {self.power} power.")
    



class Hero(Character):
    def __init__(self, health, power):
        self.character_name = "hero"
        self.double_power = power*2
        super(Hero, self).__init__(health, power)


class Goblin(Character):
    def __init__(self, health, power):
        self.character_name = "goblin"
        super(Goblin, self).__init__(health, power)


class Medic(Character):
    def __init__(self, health, power):
        self.character_name = "medic"
        super(Medic, self).__init__(health, power)

class Shadow(Character):
    def __init__(self, health, power):
        self.character_name = "shadow"
        super(Shadow, self).__init__(health, power)


def main():

    hero = Hero(100, 5)
    goblin = Goblin(100, 2)
    medic = Medic(100, 3)
    shadow = Shadow(100, 1)

    while hero.alive():
        hero.print_status()
        print("What do you want to do?")
        print("0. flee")
        print("1. fight goblin")
        print("2. fight medic")
        print("3. fight shadow")
        print("4. fight zombie")
        print("5. fight wizard")
        print("6. fight dragon")
        print("7. do nothing")
        print("> ", end=" ")
        raw_input = input()

        if raw_input == "1": #goblin
            if not hero.alive():
                print("You are dead.")
            else:
                hero.attack(goblin)
            
            if not goblin.alive():
                print("The goblin is dead.")
                break
            else:
                goblin.attack(hero)
                goblin.print_status()

        elif raw_input == "2": #medic
            if not hero.alive():
                print("You are dead.")
            else:
                hero.attack(medic)

            if not medic.alive():
                print("The medic is dead.")
            else:
                medic.alive()
                medic.attack(hero)
                medic.print_status()

        elif raw_input == "3": # shadow
            if not hero.alive():
                print("You are dead.")
            else:
                hero.attack(shadow)

            if not shadow.alive(): 
                print("The shadow is dead.")
            else:
                shadow.alive()
                shadow.attack(hero)
                shadow.print_status()
        elif raw_input == "4":
            pass
        elif raw_input == "5":
            pass
        elif raw_input == "6":
            pass
        elif raw_input == "7":
            pass
        elif raw_input == "0":
            print("Goodbye.")
            break
        else:
            print("Invalid input {}".format(raw_input))


main()
