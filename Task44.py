# -*- coding: utf-8 -*-
"""
Created on Sat Sep 11 22:37:57 2021

@author: Fetibek Aliev
"""
import numpy as np

#S = input()
#V = input()
#k = input()
#p = input()


S = '20 8 9 18 5 12 16 16 6 7'
V = '44 70 44 66 46 38 38 37 66 67'
k = 4
p = 7

S_list = list(map(int, S.split()))
V_list = list(map(int, V.split()))

S_list_array = np.array(S_list)
V_list_array = np.array(V_list)

S_k = S_list_array[k:p+1]
V_k = V_list_array[k:p+1]

S_k_sum = np.sum(S_k)

T_k = S_k / V_k

T_k_sum = sum(T_k)

V_k_avg = S_k_sum/T_k_sum

print("S = %3d км, T = %5.2f час, V = %5.2f км/ч"
      %(S_k_sum, T_k_sum, V_k_avg))