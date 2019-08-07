# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 23:08:39 2019

@author: satya
"""
"""
The sum of the squares of the first ten natural numbers is,

12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""
sum1,sum2=0,0
square1,square2=0,0

for i in range(101):
    sum1=sum1+i
    square1=i*i+square1

print(sum1*sum1-square1)