# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 10:19:28 2021

@author: Fetibek Aliev
"""

k = [1, 2, 3]

k = map(int, k)


def sss(*f):
    sum = 0
    for n in f:
        sum += n
    return sum

ff = sss(k)

print(ff)