# -*- coding: utf-8 -*-
"""
Created on Sun Sep 12 15:27:22 2021

@author: Fetibek Aliev
"""
import numpy as np

#OX = input()
#OY = input()

OX = '-8.9 -8.5 -8.0 -7.1 -6.8 -6.1 -5.6 -5.5 -5.2 -5.2 -5.2 -4.2 -4.1 -3.5'
OY = '-1.4 -1.2 -1.1 -0.9 -0.8 -0.6 -0.5 -0.4 -0.3 -0.3 -0.3 -0.1 0.1 0.1'

OX_list = list(map(float, OX.split()))
OY_list = list(map(float, OY.split()))

OX_list_array = np.array(OX_list)
OY_list_array = np.array(OY_list)

p_1 = np.polyfit(OX_list_array, OY_list_array, 1)
p_2 = np.polyfit(OX_list_array, OY_list_array, 2)

def get_trend_p_1(x, p_1):
    y = p_1[0]* x + p_1[1]
    return y

def get_trend_p_2(x, p_2):
    y = p_2[0] * x **2 + p_2[1]* x + p_2[2]
    return y

OX_list_array_p_1 = [get_trend_p_1(OX_list_array[i], p_1)
                    for i in range(len(OX_list_array))]

OX_list_array_p_2 = [get_trend_p_2(OX_list_array[i], p_2)
                    for i in range(len(OX_list_array))]

OX_list_array_p_1_error = (np.abs(OX_list_array_p_1 - OY_list_array)/OY_list_array) * 100
OX_list_array_p_2_error = (np.abs(OX_list_array_p_2 - OY_list_array)/OY_list_array) * 100

OX_list_array_p_1_error_mean = np.mean(OX_list_array_p_1_error)
OX_list_array_p_2_error_mean = np.mean(OX_list_array_p_2_error)

if OX_list_array_p_1_error_mean < OX_list_array_p_2_error_mean:
    print("%5.3f %5.3f"
          %(p_1[0], p_1[1]))
else:
    print("%5.3f %5.3f %5.3f"
          %(p_1[0], p_1[1], p_1[2]))