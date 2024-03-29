import time

class FirstSword: # Found in begining of game
    def __init__(self, damage, range, attack_speed):
        self.damage = 5 # Enemies in the begging will range from 30-50 hp
        self.range = 0.5 # Range of half a tile
        self.attack_speed = 2 # Can fit 2 attacks in a second

    def useAtkCooldown(self):
        #time.sleep(1/self.attack_speed)
        pass

class WpnPlaceHolder1: # Placeholder weapon, cant be picked up
    def __init__(self, damage, range, attack_speed):
        self.damage = 20 # Enemies in this stage would have to be 100-130 hp
        self.range = 0.7 # Range of a 7th of a tile, basically a long sword
        self.attack_speed = 1 # Can fit 1 attacks in a second

    def useAtkCooldown(self):
        #time.sleep(1/self.attack_speed)
        pass