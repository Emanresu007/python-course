# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 11:38:41 2021

@author: Fetibek Aliev
"""

import math

OX = input()
OY= input()
k = input()
r = input()

OX_split_int = list(map(int, OX.split()))
OY_split_int = list(map(int, OY.split()))
k_int = int(k)
r_int = int(r)

# Выявление координат города откуда транслирует радиостанция
OX_k = OX_split_int[k_int]
OY_k = OY_split_int[k_int]

def f(x1, y1, xn, yn):
    f = math.sqrt((xn - x1)**2 + (yn - y1)**2)
    return f

rastoyanie = []

rastoyanie = [f(OX_k, OY_k, OX_split_int[i], OY_split_int[i]) 
                     for i in range(len(OX_split_int))]

rastoyanie_true = [rastoyanie[i] <= r_int
                   for i in range(len(rastoyanie))]

count_town = sum(rastoyanie_true)

print(count_town)