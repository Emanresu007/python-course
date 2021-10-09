# -*- coding: utf-8 -*-
"""
Created on Wed May 12 23:37:41 2021

@author: Fetibek Aliev
"""

import matplotlib.pyplot as plt

plt.plot([1, 7, -3, -0.5], [7, 25, 9, 0.15 ])

plt.show()

plt.plot( [7, 25, 9, 0.15 ])

plt.show()

plt.plot([1, 7, -3, -0.5], [7, 25, 9, 0.15 ], color="green", marker="o", linestyle="dashed",linewidth=2, markersize=12)

plt.show()

# формируем линию

line = plt.plot([1, 5, -3, -0.5], [1, 25, 9, 0.25 ])

# задаем формат ее вывода

plt.setp(line, color="red", linewidth=2, marker="o" )

# устанавливаем две оси в положение zero

plt.gca().spines["left"].set_position("zero")

plt.gca().spines["bottom"].set_position("zero")

# скрываем остальные две

plt.gca().spines["top"].set_visible(False)

plt.gca().spines["right"].set_visible(False)

# отображаем область построения

plt.show()


import matplotlib.pyplot as plt

def f_x(x):

   y = x ** 3 - 9 * x ** 4 +  x + 5

   return y

a = -2

b = 6

n =200

h = (b-a)/(n-1)

x_list = [a + h * i for i in range(n)]

f_list = [f_x(x) for x in x_list]

line = plt.plot(x_list, f_list)

plt.setp(line, color="blue", linewidth=2)

plt.gca().spines["left"].set_position("zero")

plt.gca().spines["bottom"].set_position("zero")

plt.gca().spines["top"].set_visible(False)

plt.gca().spines["right"].set_visible(False)

