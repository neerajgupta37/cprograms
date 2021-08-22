# -*- coding: utf-8 -*-
"""
Created on Thu Dec 31 05:42:22 2020

@author: dell
"""

def special_for(iterable):
    iterator = iter(iterable)
    while True:
        try:
            print(iterator)
            print(next(iterator))
        except StopIteration:
            break
        
special_for([1,2,3]) 