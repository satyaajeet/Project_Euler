# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 21:06:29 2019

@author: satya
"""
sum=0
for i in range(1000):
    if (i%3==0 or i%5==0):
        sum=sum+i
        
print(sum)