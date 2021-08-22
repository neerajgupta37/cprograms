# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 04:54:47 2020

@author: dell
"""

my_list = [5,4,3]

print(list(map(lambda item: item**2, my_list)))

my_list1 = [(0,2),(4,3), (9,9), (10,-1)]

#print(sorted(my_list1, key = lambda my_list1: my_list1[1]))

my_list1.sort(key = lambda x : x[1])
print(my_list1)