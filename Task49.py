# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 12:28:02 2021

@author: Fetibek Aliev
"""

import numpy.linalg as alg
import numpy as np

a = np.array([[-2, -8.5, -3.4, 3.5], [0, 2.4, 0, 8.2],  [2.5, 1.6, 2.1, 3], [0.3, -0.4, -4.8, 4.6]])

b = np.array([[-1.88], [-3.28], [-0.5], [-2.83]])

inv_a = alg.inv(a)

x = np.dot(inv_a, b)

x_round = np.round(x, 1)

y = np.transpose(x_round, axes=None)

y = y[0]

print(y)

import numpy as np
import matplotlib.pyplot as plt

#задаем координаты точек
points = np.array([[1, 3], [3, -2], [2, 3], [-3, 4], [-2, -1]])

# вычисляем координаты средней точки
mean_point = np.mean(points, 0)
print("Средняя точка: ",np.round(mean_point, 2))

# выводим точки на график
plt.plot(points[:, 0], points[:, 1], "bo")
plt.plot(mean_point[0], mean_point[1], "ro")

# устанавливаем оси  
plt.gca().spines["left"].set_position("zero")
plt.gca().spines["bottom"].set_position("zero")
plt.gca().spines["top"].set_visible(False)
plt.gca().spines["right"].set_visible(False)

plt.show()

import numpy as np

b = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

print(b[:2])

