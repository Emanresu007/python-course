# -*- coding: utf-8 -*-
"""
Created on Sun Sep 12 11:28:48 2021

@author: Fetibek Aliev
"""

import numpy as np

OX = input()
OY = input()
OX_mishen = input()
OY_mishen = input()

#OX = '255.7 407.2 559.2 798.3 820.5 971.6 1221.1 1389.2'
#OY = '256.9 340.3 390.3 400.4 397.1 355.4 213.5 66.5'
#OX_mishen = 1380.4
#OY_mishen = 65.4

OX_list = list(map(float, OX.split()))
OY_list = list(map(float, OY.split()))
OX_mishen = float(OX_mishen)
OY_mishen = float(OY_mishen)

OX_list_array = np.array(OX_list)
OY_list_array = np.array(OY_list)

a = np.polyfit(OX_list_array, OY_list_array, 2)

def get_trend(x, a):
    y = a[0] * x **2 + a[1]* x + a[2]
    return y

h_zero = get_trend(0, a)




h_target = get_trend(OX_mishen, a)

delta_h = abs(OY_mishen - h_target)

if delta_h <= 0.5:

    y = 'yes'

else:

    y = 'no'
    
print("h0 = %6.2f, %2s"
      %(h_zero, y))