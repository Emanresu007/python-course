# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 23:24:38 2021

@author: Fetibek Aliev
"""

import numpy as np

n = int(input())

point = []

for i in range(n):
    line = input().split()
    point.append(line)
    
point_array = np.array(point, float)
