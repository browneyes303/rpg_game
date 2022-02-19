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
        if (self.character_name == "hero"):
            roll = random.randint(1,5)
            if roll == 1:
                self.power = int(self.power*2)
                enemy.health -= self.power
                print(f"You do {self.power} damage to the {enemy.character_name}.")
                self.power = int(self.power/2)
            else:
                enemy.health -= self.power
                print(f"You do {self.power} damage to the {enemy.character_name}.")

        elif (self.character_name == "goblin"):
            enemy.health -= self.power
            print(f"The {self.character_name} does {self.power} damage to you.")

        elif (self.character_name == "medic"):
            roll = random.randint(1,5)
            if roll == 5:
                self.health = int(self.health+2)
                enemy.health -= self.power
                print(f"You do {self.power} damage to the {enemy.character_name}.")
            else:
                enemy.health -= self.power
            print(f"The {self.character_name} does {self.power} damage to you.")

        elif (self.character_name == "medic"):
            roll = random.randint(1,5)
            if roll == 5:
                self.health = int(self.health+2)
                enemy.health -= self.power
                print(f"You do {self.power} damage to the {enemy.character_name}.")
            else:
                enemy.health -= self.power
            print(f"The {self.character_name} does {self.power} damage to you.")

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
    goblin = Goblin(6, 2)
    medic = Medic(100, 3)

    while goblin.alive() and hero.alive():
        hero.print_status()
        print("What do you want to do?")
        print("1. fight goblin")
        print("2. fight medic")
        print("3. do nothing")
        print("4. flee")
        print("> ", end=" ")
        raw_input = input()
        if raw_input == "1":
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
        elif raw_input == "2":
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
        elif raw_input == "3":
            pass
        elif raw_input == "4":
            print("Goodbye.")
            break
        else:
            print("Invalid input {}".format(raw_input))


main()
