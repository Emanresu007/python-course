# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 00:00:11 2021

@author: Fetibek Aliev
"""

x = int(input())

def closest_mod_5(x):
    if (x%5) == 0:
        y = int((x//5))
    else:
        y = (int((x//5) + 1)) * 5
    return y

y = closest_mod_5(x)

print(y)

