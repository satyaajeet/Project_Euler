# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 21:59:08 2019

@author: satya
"""
num=0
n=[]
for i in range(5000):
    for j in range(10):
        if((i+1)%(j+1)==0 and (i+1)%(j+2)==0 and (i+1)%(j+3)==0 and (i+1)%(j+4)==0 and (i+1)%(j+5)==0):
            n.append(i+1)
            break
        else:
            continue
            
print(n)

2*2*2*2*3*3*5*7*11*13*17*19

num=1
for i in range(21):
    num=(i+1)*num

print(num)

num=int(input("Enter"))
fact=[]
for i in range(num):
    while(num%(i+2)==0):
        num=num//(i+2)
        if((i+2)<21):
            fact.append(i+2)
        else:
            break
        
print(fact)