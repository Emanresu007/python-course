# -*- coding: utf-8 -*-
"""
Created on Sat May 15 10:05:29 2021

@author: Fetibek Aliev
"""
import matplotlib.pyplot as plt

def f_x(x):

   y = x ** 3 - 6 * x ** 2 +  x + 5

   return y

def y_x(x):

    y = (x - 2) ** 2 -6

    return y

a = -2

b = 6

n =100

h = (b-a)/(n-1)

x_list = [a + h * i for i in range(n)]

f_list = [f_x(x) for x in x_list]

y_list = [y_x(x) for x in x_list]

line_f = plt.plot(x_list, f_list, label='f(x)')

line_y = plt.plot(x_list, y_list, label='y(x)')

plt.title("Графики функций")

plt.show()
