# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 15:43:34 2021

@author: Fetibek Aliev
"""

import numpy as np

import math as mt

c = int(input())

array_list_OX_OY = [ ]

for i in range(c):
    
    line = input()

    array_str = line.split()

    array_list_OX_OY.append(array_str)

a = np.array(array_list_OX_OY, dtype=int)

angle = int(input())

angle_radians = np.array([[mt.cos(mt.radians(angle)), mt.sin(mt.radians(angle))], 
                         [-1 * mt.sin(mt.radians(angle)), mt.cos(mt.radians(angle))]])

a_dot = np.dot(a, angle_radians)

a_dot_mean = np.mean(a_dot, 0)

print("avg_x = %6.2f, avg_y = %6.2f"
      %(a_dot_mean[0], a_dot_mean[1]))