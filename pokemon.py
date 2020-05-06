from random import randint

class Pokemon:

    def __init__(self, name, variety, level=1, max_health=50, current_health=50):
        self.name = name.title()
        self.level = level
        self.variety = variety #(There are 3 types 'Fire', 'Water', and 'Grass.' Could be done with list?)
        self.max_health = max_health
        self.current_health = current_health
        self.knocked_out = False
        self.hierarchy = {'Fire': 0, 'Water': 1, 'Grass': 2}
    
    def lose_health(self, value):
        self.current_health -= value
        print(f"{self.name.title()} has lost {value} health and now has {self.current_health} health.\n")
        if self.current_health <= 0:
            self.knocked_out = True
            print(f"{self.name.title()} has been knocked out.\n")

    def gain_health(self, value):
        if (self.current_health + value) > self.max_health: 
            diff = self.max_health - self.current_health
            self.current_health = self.max_health
            print(f"{self.name.title()} has gained {diff} health and now has {self.current_health}.\n")
        elif (self.current_health + value) <= self.max_health:  
            self.current_health += value
            print(f"{self.name.title()} has gained {value} health and now has {self.current_health} health.\n")
        elif self.current_health == self.max_health:
            print(f"{self.name.title()} is already at maximum health!\n")
        else:
            print(f"{self.name.title()} is knocked out. He must be revived first.\n")  
        
    def revive(self):
        if self.knocked_out == True:
            self.knocked_out == False
            self.current_health == self.current_health + self.max_health
            print("You've been revived!")
        else:
            print("You can only be revived when you're knocked out.\n")
    
    def attack(self, opponent):
        self.opponent = opponent
        self.damage = self.level
        if opponent.current_health <= 0:
            print("You can't attack a knocked out opponent.\n")
        else:
            if (self.variety == "fire" and (opponent.variety == "water" or opponent.variety == "grass")) or (self.variety == "water" and opponent.variety == "grass"):
                self.damage = (self.damage * 2)
                print(f"{self.name} has dealt {self.damage} damange to {opponent.name}.\n")
            elif (self.variety == "grass" and (opponent.variety == "water" or opponent.variety == "fire")) or (self.variety == "water" and opponent.variety == "fire"):
                self.damage = (self.damage * .5)
                print(f"{self.name} has dealt {self.damage} damange to {opponent.name}.\n")
            else:
                self.damage = self.damage * 1
                print(f"{self.name} has dealt {self.damage} damange to {opponent.name}.\n")
            opponent.lose_health(self.damage)
        

billy = Pokemon("billy", "water", 10)
randy = Pokemon("randy", "grass")

billy.attack(randy)
billy.attack(randy)
billy.attack(randy)
randy.revive()
randy.gain_health(6)