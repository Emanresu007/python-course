# -*- coding: utf-8 -*-
"""
Created on Sat May 15 14:42:04 2021

@author: Fetibek Aliev
"""

import matplotlib.pyplot as plt

from math import e, cos, log, sin, radians

def f_x(x):
    y = (e**cos(x)) + log(sin(0.8 * x)**2 + 1) * cos(x)
    return y

def y_x(x):
    y = (-1) * log((cos(x) + sin(x))**2 + 1.7) + 2
    return y

a = float(input())
a = radians(a)

b = float(input())
b = radians(b)

n = 500

h = (b-a)/(n-1)

x_list = [a + h * i for i in range(n)]

f_x_list = [f_x(x) for x in x_list]

y_x_list = [y_x(x) for x in x_list]

line_f = plt.plot(x_list, f_x_list, label='f(x)')

line_y = plt.plot(x_list, y_x_list, label='y(x)')

plt.gca().spines["left"].set_position("zero")

plt.gca().spines["bottom"].set_position("zero")

plt.gca().spines["top"].set_visible(False)

plt.gca().spines["right"].set_visible(False)

plt.legend()

plt.show()

x = float(71)

x = radians(x)

print(f_x(x), y_x(x))