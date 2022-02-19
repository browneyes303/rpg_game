    
    import random
    
    def attack(self, enemy):
        # Hero attacks enemy
        roll = random.randint(1,5)
        if roll == 1:
            self.power = (self.power * 2)
            enemy.health -= self.power
            self.power = (self.power/2)
        else:
            enemy.health -= self.power