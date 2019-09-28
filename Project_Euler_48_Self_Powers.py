# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 22:15:32 2019

@author: satya
"""
s=0
for i in range(1,11):
    num=i**i
    s=num+s

for i in range(11,1000):
    num=str(i**i)
    rem=num[(len(num)-10):len(num)]
    s=int(rem)+s
    
s=str(s)
print(s[(len(s)-10):len(s)])

