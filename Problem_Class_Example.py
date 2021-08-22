# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 17:11:57 2020

@author: dell
"""

class User():
    def signin(self):
        print('logged in')
        
class Wizard(User):
    def __init__(self,name,power):
        self.name=name
        self.power=power
        #
    def attack(self):
        print(f'Attacking with the power {self.power}')
    
    
class Archers(User):
    
    def __init__(self,name,num_arrows):
        self.name=name
        self.num_arrows=num_arrows      
    
    def attack(self):
        print(f'Attacking with the arrows {self.num_arrows}')
    pass


wizard1 = Wizard('Merlin',50)    
archer1 = Archers('Robin',560)


print(wizard1.attack())
print(archer1.attack())


wizard1.signin()
archer1.signin()


#def player_attack(char):
#    char.attack()
    
#player_attack(wizard1)    

for char in [wizard1, archer1]:
    char.attack()

