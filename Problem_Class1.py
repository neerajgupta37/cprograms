# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 17:18:20 2020

@author: dell
"""

class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def oldest_cat(self):
        if(Cat1.age > Cat2.age and Cat1.age > Cat3.age):
            print(f'the oldest cat is {Cat1.age}')
        elif (Cat2.age > Cat3.age):
            print(f'the oldest cat is {Cat2.age}')
        else: 
            print(f'the oldest cat is {Cat3.age}')
        



# 1 Instantiate the Cat object with 3 cats
Cat1 = Cat('Jenifer',4)
Cat2 = Cat('Jelly',7)
Cat3 = Cat('Marget',5)

Cat1.oldest_cat()




# 2 Create a function that finds the oldest cat



# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2