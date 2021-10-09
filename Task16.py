# -*- coding: utf-8 -*-
"""
Created on Wed May 12 07:48:19 2021

@author: Fetibek Aliev
"""

f_list = [26 * i - 1 for i in range(8)]
print(f_list)

k_list = [5 * 6 * i**3 - 123 for i in range(25)]
print(k_list)

x_list = [5, 8, -5]
y_list = [x ** 2 for x in x_list]
print(y_list)


import math

def f_x(x):
   try:
       y = 1 / (x+1) + x / (x-3)
   except:
       y = math.inf
   return y

s = input(("x_list = "))

str_list = s.split()

x_list = [float(x) for x in str_list]

for x in x_list:
    y = f_x(x)
    print("f(%4.2f) = %6.3f" % (x,  y))