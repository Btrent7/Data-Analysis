class Vault:
    def __init__(self, gold=0, silver=0, copper=0):
        self.gold = gold
        self.silver = silver
        self.copper = copper
    
    def __str__(self):
        return f"Gold: {self.gold} , Silver: {self.silver} , Copper: {self.copper}"
    
    def __add__(self, other):
        gold = self.gold + other.gold
        silver = self.silver + other.silver
        copper = self.copper + other.copper
        return Vault(gold, silver, copper)

potter = Vault(100, 50, 25)
print(potter)

weasly = Vault(25, 50, 100)
print(weasly)

total = potter + weasly
print(total)