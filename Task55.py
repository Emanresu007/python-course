# -*- coding: utf-8 -*-
"""
Created on Sun Sep 19 10:52:40 2021

@author: Fetibek Aliev
"""

x = [1, 2, 3] 

print(id(x))

print(id(x[0]))

y = x

x.append(4)

print(x)
print(y)
print(id(x))
print(id(y))

type(id(x))


x = [1, 2, 3]
y = x
y.append(4)

s = "123"
t = s
t = t + "4"

print(str(x) + " " + s)

k = 27
j = 27
f = 27

ff = []
kk = []

print(id(k))
print(id(j))
print(id(f))

print(id(ff))
print(id(kk))