# -*- coding: utf-8 -*-
"""
Created on Sun Aug  8 19:19:14 2021

@author: Fetibek Aliev
"""

import numpy as np

list_test = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

sq = lambda x: x**2

b = list(map(sq, list_test))

print(b)

b.reverse()

print(b)

def sq2(x):
    y = x**2
    return y

c = [sq2(x) for x in list_test]

print(c)

range_k = list(range(1000 - 1))

print(range_k)

k = list(range(10, 100, 10))
print(k)


i = 0

length = len(k) - 1

print(length)

while i <= length:
    print(k[i])
    i+=1
    
for i in k:
    print(i)
    
for k in range(10):
    print('Привет, Фетибек!')
    


k = list(range(1000))

a = 0
b = 0
c = 0

for x in range(1000):

 print(a,b,c)

 c += 1
 
 if c>9:
     c=0
     b+=1
 if b>9:
     b=0
     a+=1
    
g = 7
for x in range(100):
    print(g)
    g += -7

a = 0
b = 0
c = 0
d = 0

for x in range(10000):
    print(a, b, c, d)
    d+=1
    if d>9:
        d=0
        c+=1
        
    