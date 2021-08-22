# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 19:25:11 2020

@author: dell
"""

class Pets():
    animals = []
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Simon(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Sally(Cat):
    def sing(self, sounds):
        return f'{sounds}'

#1 Add nother Cat
class Sinonara(Cat):
    def sing(self, sounds):
        return f'{sounds}'


#2 Create a list of all of the pets (create 3 cat instances from the above)
my_cats = [Simon('c1', 5), Sally('c2', 6), Sinonara('c3',4)]
#print(my_cats)

#3 Instantiate the Pet class with all your cats use variable my_pets

my_pets=Pets(my_cats)
print(my_pets.animals)



#4 Output all of the cats walking using the my_pets instance

my_pets.walk()

