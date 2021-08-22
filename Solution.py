# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#import numpy as np
import math


x = 0.5
denominator = 0
true_value=0.6065307
present_approx_value = 0
previous_approx_value = 0
true_error=0
relative_error=0
approx_error=0
relative_approx_error=0
counter = 0;
n = 0

print("-------------------------------------------------------------\n")   
print("Case A:")
print("---------------------------------------------------------------")


while True:
    denominator += round((math.pow(x,n))/(math.factorial(n)),5)
    present_approx_value = round(1 / denominator,7)
    print(f"the value of present_approx_value is {present_approx_value}\n")
    true_error=round(abs(true_value - present_approx_value), 15)
    
    print(f"the value of true_error is {true_error}\n")
    relative_error = round((true_error/true_value)*100,7)
    print(f"the value of relative_error is {relative_error}\n")
    
    approx_error= round(abs(present_approx_value - previous_approx_value),15)
    previous_approx_value = present_approx_value
    relative_approx_error=round((approx_error/present_approx_value)*100,7)
    print(f"the value of relative_approx_error is {relative_approx_error}\n")
    n = n+1
    counter = counter + 1
    if(relative_approx_error < relative_error):
        print(f"the total iterations are {counter}")
        break
   


print("-------------------------------------------------------------\n")   
print("Case B:")
print("---------------------------------------------------------------")

y = -0.5
present_approx_valuey = 0
previous_approx_valuey = 0
true_errory=0
relative_errory=0
approx_errory=0
relative_approx_errory=0
counter=0
n=0

while True:
    present_approx_valuey += round((math.pow(y,n))/(math.factorial(n)),5)
    print(f"the value of present_approx_value is {present_approx_valuey}\n")
    true_errory=round(abs(true_value - present_approx_valuey), 15)
    
    print(f"the value of true_error is {true_errory}\n")
    relative_errory = round((true_errory/true_value)*100,7)
    print(f"the value of relative_error is {relative_error}\n")
    
    approx_errory= round(abs(present_approx_valuey - previous_approx_valuey),15)
    previous_approx_valuey = present_approx_valuey
    relative_approx_errory=round((approx_errory/present_approx_valuey)*100,7)
    print(f"the value of relative_approx_error is {relative_approx_errory}\n")
    n = n+1
    counter = counter + 1
    if(relative_approx_errory < relative_errory):
        print(f"the total iterations are {counter}")
        break 
    