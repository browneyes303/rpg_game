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


    def attack_status(self, enemy):
        print(f"The {self.character_name} does {enemy.power} damage to you.")


    def enemy_damage(self, enemy):
        enemy.health -= self.power


    def hero_attack(self, enemy, hero_double): #! hero
        hero_roll =  random.randint(1,5)
        if hero_roll == 5:
            hero_double = (self.power*2)
            enemy.health -= hero_double
            if enemy.character_name == "shadow":
                pass
            else:
                print(f"You do {hero_double} damage to the {enemy.character_name}.")
        else:
            enemy.health -= self.power # here enemy is true enemy
            if enemy.character_name == "shadow":
                hero_double = 1
            else:
                print(f"You do {self.power} damage to the {enemy.character_name}.")
        return hero_double


    def shadow_attack(self, enemy, hero_double): # shadow
        shadow_roll = random.randint(1,10)
        if shadow_roll == 10:
            if hero_double != 1:
                print(f"You do {hero_double} damage to the {self.character_name}")
            else:
                print(f"You do {enemy.power} damage to the {self.character_name}")
        else:
            if hero_double != 1:
                self.health += (enemy.power*2)    # shadow doesn't lose health
                print(f"You do zero damage to the {self.character_name}")
            else:
                self.health += enemy.power
                print(f"You do zero damage to the {self.character_name}")
        self.enemy_damage(enemy)
        print(f"The {self.character_name} does {self.power} damage to you.") # shadow status of attack to hero


    def goblin_attack(self, enemy):
        self.enemy_damage(enemy) # enemy is hero
        self.attack_status(enemy)


    def medic_attack(self, enemy):
        medic_roll = random.randint(1,5)
        if medic_roll == 5:
            self.health += 2
        self.enemy_damage(enemy) # enemy is hero
        self.attack_status(enemy)


    def zombie_attack(self, enemy):
        self.enemy_damage(enemy) # enemy is hero
        self.attack_status(enemy)# enemy is hero


    def wizard_attack(self, enemy):
        self.enemy_damage(enemy) # enemy is hero
        self.health += 1 # wizard heals himself +1 after every hit
        self.attack_status(enemy)


    def dragon_attack(self, enemy):
        self.enemy_damage(enemy) # enemy is hero
        self.attack_status(enemy)


    def print_status(self):
        if (self.character_name == "hero"):
            print(f"You have {self.health} health and {self.power} power.")
        elif (self.character_name == "goblin"):
            print(f"The {self.character_name} has {self.health} health and {self.power} power.")
        elif (self.character_name == "medic"):
            print(f"The {self.character_name} has {self.health} health and {self.power} power.")
        elif (self.character_name == "shadow"):
            print(f"The {self.character_name} has {self.health} health and {self.power} power.")
        elif (self.character_name == "zombie"):
            print(f"The {self.character_name} has {self.health} health and {self.power} power.")
        elif (self.character_name == "wizard"):
            print(f"The {self.character_name} has {self.health} health and {self.power} power.")
        elif (self.character_name == "dragon"):
            print(f"The {self.character_name} has {self.health} health and {self.power} power.")


class Hero(Character):
    def __init__(self, health, power):
        self.character_name = "hero"
        self.hero_double = 0
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
        
class Zombie(Character):
    def __init__(self, health, power):
        self.character_name = "zombie"
        super(Zombie, self).__init__(health, power)

class Wizard(Character):
    def __init__(self, health, power):
        self.character_name = "wizard"
        super(Wizard, self).__init__(health, power)

class Dragon(Character):
    def __init__(self, health, power):
        self.character_name = "dragon"
        super(Dragon, self).__init__(health, power)

hero = Hero(50, 5)
goblin = Goblin(10, 2)
medic = Medic(20, 3)
shadow = Shadow(1, 5)
zombie = Zombie(20, 5)
wizard = Wizard(10, 5)
dragon = Dragon(100, 10)

def choose_enemy():
    print("Which enemy would you like to choose")
    print("1. goblin")
    print("2. medic")
    print("3. shadow")
    print("4. zombie")
    print("5. wizard")
    print("6. dragon")
    print("> ", end=" ")
    raw_input = input()
    
    if raw_input == "1":
        enemy = goblin
    elif raw_input == "2":
        enemy = medic
    elif raw_input == "3":
        enemy = shadow
    elif raw_input == "4":
        enemy = zombie
    elif raw_input == "5":
        enemy = wizard
    elif raw_input == "6":
        enemy = dragon
    return enemy

def main():

    exit = False

    while exit == False:

        enemy = choose_enemy()

        while enemy.alive() or hero.alive():
            hero.print_status()
            enemy.print_status()
            print("What do you want to do?")
            print(f"1. fight {enemy.character_name}")
            print("2. do nothing")
            print("3. flee")
            print("4. pick another enemy")
            print("> ", end=" ")
            raw_input = input()

            if raw_input == "1": # fight enemy
                if not hero.alive():
                    print("You are dead.")
                    break
                else:
                    double_power = hero.hero_attack(enemy, hero.hero_double)

                if not enemy.alive():
                    if enemy.character_name == "zombie":
                        enemy.zombie_attack(hero) # zombie attacks hero while dead
                    else:
                        print(f"The {enemy.character_name} is dead.")
                        break
                elif (enemy.character_name == "goblin"):
                    enemy.goblin_attack(hero)
                elif (enemy.character_name == "medic"):
                    enemy.medic_attack(hero)
                elif (enemy.character_name == "shadow"):
                    enemy.shadow_attack(hero, double_power)
                elif (enemy.character_name == "wizard"):
                    enemy.wizard_attack(hero)
                elif (enemy.character_name == "dragon"):
                    enemy.dragon_attack(hero)
                elif (enemy.character_name == "zombie"):
                    enemy.zombie_attack(hero) # zombie attacks hero while alive
                enemy.print_status()


            elif raw_input == "2":
                pass

            elif raw_input == "3":
                print("Goodbye.")
                exit = True
                break

            elif raw_input == "4":
                break

            else:
                print("Invalid input {}".format(raw_input))


main()
