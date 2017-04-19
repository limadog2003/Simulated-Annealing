# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import random
import math

t = 0
T = 10000
random.seed(1234567)
x1 = random.uniform(-10, 10)
x2 = random.uniform(-10, 10)
x3 = random.uniform(-10, 10)

def eval (x, y, z): 
    return(x*x + y*y + z*z)
    
curr = eval(x1, x2, x3)

while (t < 3500):
    count = 0
    while (count < 3500):
        x11 = random.uniform(-.3, .3) + x1
        x22 = random.uniform(-.3, .3) + x2
        x33 = random.uniform(-.3, .3) + x3
        
        test = eval(x11, x22, x33)
        #print("test:", test, "curr:", curr, x11, x22, x33)
        if (test < curr):
            #print ("test is better")
            curr = test
            x1 = x11
            x2 = x22
            x3 = x33
        elif((random.random()) < math.exp((curr - test)/T)):
            #print("Random switch")
            curr = test
            x1 = x11
            x2 = x22
            x3 = x33
        count = count + 1
    T = T/2 + .00001
    t = t + 1

print(x1, x2, x3)
print (eval(x1, x2, x3))

    
    
    
    
    
    
    
    
    
    
    
    