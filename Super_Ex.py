# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 19:07:55 2020

@author: dell
"""

class User():
    def __init__(self, email):
        self.email = email
        
    def signin(self):
        print('logged in')
        
class Wizard(User):
    def __init__(self,name,power,email):
        super().__init__(email)
        self.name=name
        self.power=power
        #
    def attack(self):
        
        print(f'Attacking with the power {self.power}')
    
    



wizard1 = Wizard('Merlin',50, 'merlin@123')    



print(wizard1.attack())
