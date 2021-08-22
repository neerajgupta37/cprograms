# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 20:19:53 2020

@author: dell
"""

#performance dcorators
from time import time

def performance(func):
    def wrap_func(*args,**kargs):
        t1 = time()
        result=func(*args,**kargs)
        t2 = time()
        print(f'took {t2-t1}')
        return result
    return wrap_func 

@performance        
def long_time():
    for i in range(1000000):
        i*5
        
long_time()        