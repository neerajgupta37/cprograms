# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 10:15:55 2020

@author: dell
"""

class Superlist(list):
   # list1 = []
    
        
    def __len__(self):
        return 100
    
    
sl = Superlist()    

print(len(sl))
print(sl)

print(sl.append(4))

print(sl)
print(issubclass(Superlist,list))

    
    