
# Soldier

class Soldier():
    def __init__ (self, health, strength):
        self.health = health
        self.strength = strength 
        
    def attack(self):
            return self.strength
    
    def receiveDamage(self, damage):
        self.health -= damage


# Viking

class Viking(Soldier):
    def __init__ (self, name, health, strength):   
        super().__init__(health, strength)
        self.name = name 

    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return "{} has received {} points of damage".format(self.name, damage)
        else:
            return "{} has died in act of combat".format(self.name)
    
    def battleCry(self):
        return "Odin Owns You All!"


# Saxon

class Saxon(Soldier):
    def __init__ (self, health, strength):
        super().__init__(health, strength)
    
    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return "A Saxon has received {} points of damage".format(damage)  
        else:
            return "A Saxon has died in combat"


# War
import random

class War:
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []
        
    def addViking(self, Viking):
        self.vikingArmy.append(Viking)
    
    def addSaxon(self, Saxon):
        self.saxonArmy.append(Saxon)
        
    def vikingAttack(self):
        s = random.choice(self.saxonArmy)
        v = random.choice(self.vikingArmy)
        result = s.receiveDamage(v.strength)
        if s.health <= 0:
            self.saxonArmy.remove(s)
        return result

    def saxonAttack(self):
        s = random.choice(self.saxonArmy)
        v = random.choice(self.vikingArmy)
        result = v.receiveDamage(s.strength)
        if v.health <= 0:
            self.vikingArmy.remove(v)
        return result

    def showStatus(self):
        if len(self.saxonArmy) == 0:
            return "Vikings have won the war of the century!"
        elif len(self.vikingArmy) == 0:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."


