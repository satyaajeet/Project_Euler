# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 21:17:13 2019

@author: satya
"""
#
num=600851475143
factors=[]
for i in range(1000000):
    if(num%(i+2)==0):
        factors.append(i+2)
        num=num//(i+2)
    else:
        continue
print(factors)

mult=1
for i in factors:
    mult=mult*i
    
print(mult)