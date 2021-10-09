# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 00:42:48 2021

@author: Fetibek Aliev
"""

def fib(x):
    if x == 0 or x == 1:
        return x
    else:
        return fib(x-1) + fib(x-2)

y = fib(5)

print(y)
