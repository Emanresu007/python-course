# -*- coding: utf-8 -*-
"""
Created on Thu May 13 22:31:25 2021

@author: Fetibek Aliev
"""

from math import atan, pi
import matplotlib.pyplot as plt

def compute_population(t):
   N = (172/45) * ((pi/2) - atan((2000 - t)/45))
   return N

a = int(input())

b = int(input())

n = int(input())


h = (b-a)/(n-1)

x_list = [a + h * i for i in range(n)]

f_list = [compute_population(x) for x in x_list]

feti = [x_list, f_list]

line = plt.plot(x_list, f_list)

plt.show()

print(f_list)
print(x_list)