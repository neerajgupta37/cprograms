# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 20:38:52 2020

@author: dell
"""

user1 = {
    'name': 'Sorna',
    'valid': True #changing this will either run or not run the message_friends function.
}


def message_friends(*args):
    a = args[0]
    if a['valid'] == True:
        print("Go Ahead")
    else:
        print("You are not allowed")
    
    
message_friends(user1)