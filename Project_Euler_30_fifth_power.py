# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 15:20:41 2019

@author: 1029693
"""

s,add,li=0,0,[]
for i in range(2,1000000):
    s,j=0,i
    while(i!=0):
        num=i%10
        s,i=s+num**5,i//10
    if(s==j):
        li.append(s)
    else:
        continue           
print("list of all the terms is {}".format(li))
#adding the terms of the list
for i in range(len(li)):
    add=add+li[i]
print("Sum of the terms is {}".format(add))
