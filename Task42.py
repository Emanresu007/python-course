# -*- coding: utf-8 -*-
"""
Created on Sat Sep 11 12:42:27 2021

@author: Fetibek Aliev
"""

import numpy as np

#S = input()
#T = input()

S = '14 11 11 19 7 18 9 10 13'
V = '42 50 30 43 39 36 53 60 49'

S_list = list(map(int, S.split()))
V_list = list(map(int, V.split()))

S_array = np.array(S_list)
V_array = np.array(V_list)

S_sum = np.sum(S_array)
T_sum = np.sum(S_array/V_array)
V_avg = S_sum/T_sum

print("S = %3d км, T = %5.2f час, V = %5.2f км/ч"
      %(S_sum, T_sum, V_avg))

import numpy as np

a = np.array([2, 5, 2, 0, 0])

b = np.array([5, -1, -1, 6, 2])

c = np.where(np.logical_or(a >= 0, b == 6))[0]

print(c)