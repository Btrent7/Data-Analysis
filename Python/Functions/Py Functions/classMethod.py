import random

class Hat:
    houses = ["Gryffindor", "Hufflepuff", "Slitheryn", "Other"] #Class variables shared by all instances

    @classmethod
    def sort(cls, name): #Using 'cls' not 'self'
        print(name, "is in", random.choice(cls.houses))

# hat = Hat() --Do not need to create the instance of the "Hat" class
Hat.sort("Harry")