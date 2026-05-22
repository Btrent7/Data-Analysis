import pandas as pd
import numpy as np

class Person:
    def __init__(self, name, eyecolor, age):
        self.name = name
        self.eyecolor = eyecolor
        self.age = age

class Name:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

def capitalizeName(name):
    name.firstname = name.firstname.upper()
    name.lastname = name.lastname.upper()

me = Person(Name("Brandon", "Trent"), "blue", 35)

print(me.name.firstname)
print(me.name.lastname)

capitalizeName(me.name)
print(me.name.firstname)
print(me.name.lastname)
print(me.eyecolor)
print(me.age)