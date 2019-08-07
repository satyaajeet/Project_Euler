# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 21:32:12 2019

@author: satya
"""
"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""
palindrome=[]

for i in range(1000):
    for j in range(1000):
        if(i>=j): # to reduce number of duplicate iterations
            num=(i+1)*(j+1)
            num=str(num)
            mun="".join(reversed(num))
            if(num==mun):
                palindrome.append(int(num))
            else:
                continue
        else:
            continue
print(palindrome)
maxi=max(palindrome)
print(maxi)
print(len(palindrome))
        
            

