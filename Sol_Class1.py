# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 17:33:29 2020

@author: dell
"""

class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
      



# 1 Instantiate the Cat object with 3 cats
Cat1 = Cat('Jenifer',4)
Cat2 = Cat('Jelly',7)
Cat3 = Cat('Marget',5)


# 2 Create a function that finds the oldest cat
def oldest_cat(*args):
    return max(args)


# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2

print(f'the oldest cat is {oldest_cat(Cat1.age,Cat2.age, Cat3.age)} years old')