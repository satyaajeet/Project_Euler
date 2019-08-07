# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 11:32:52 2019

@author: 1029693
"""
f1=1
f2=1
fib=[1,1]
f3=1
while(len(str(f3))<1000):
    f3=f1+f2
    f1=f2
    f2=f3
    fib.append(f3)

print("Length of last number {} in the series is {}".format(f3,len(str(f3))))

print("The first term with 1000 digit is {}".format(len(fib)))
