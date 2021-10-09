# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 00:35:06 2021

@author: Fetibek Aliev
"""

import numpy as np
import math

count = int(input())

array_list_OX_OY = [ ]

for i in range(count):
    
    line = input()

    array_str = line.split()

    array_list_OX_OY.append(array_str)

a = np.array(array_list_OX_OY, dtype = float)

a_mean = np.mean(a, 0)

def radius(a, a_mean, i):
    y = math.sqrt((a[i, 0] - a_mean[0])**2 + (a[i, 1] - a_mean[1])**2)
    return y

radius_list = []

t = list(range(count))

for i in t:
    radius_list.append(radius(a, a_mean, t[i]))

r = max(radius_list)

print("центр в точке (%6.3f, %6.3f), r = %6.3f"
      %(a_mean[0], a_mean[1], r))
