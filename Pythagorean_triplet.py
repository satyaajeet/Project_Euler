# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 20:47:39 2019

@author: satya
"""
#(a+b+c==1000) and 
for a in range(500):
    for b in range(500):
        for c in range(500):
            if(a**2 + b**2==c**2) and (a+b+c==1000):
                print(a*b*c)
                print(a,b,c)
            else:
                continue
            
