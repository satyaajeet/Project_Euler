# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 15:21:40 2019

@author: 1029693
"""
"""
2**15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2**1000?
"""
num=1
for i in range(1000):
    num=num*2
sum=0
while(num!=0):
    sum=sum+(num%10)
    num=num//10
print(sum)

