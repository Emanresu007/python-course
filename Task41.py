# -*- coding: utf-8 -*-
"""
Created on Sat Sep 11 11:14:44 2021

@author: Fetibek Aliev
"""

import numpy as np

a = np.array([2, 5, -2, 0, 8])

b = np.array([5, -1, -3, 6, 2])

c = np.round(a, 2)

print(c)

path = np.array([15, 5, 12, 2, 21, 17, 21, 3, 10, 5])

speed = np.array([60, 30, 60,45, 50, 60, 50, 40, 60, 40])

len_path = path.sum()

print("Расстояние между пунктами А и В :", len_path)

len_path = np.sum(path)

print("Расстояние между пунктами А и В :", len_path)

time = path / speed

print("Время на каждом участке :", np.round(time, 2))

sum_time = time.sum()

print("Общее время в пути : ", round(sum_time, 2))

avg_speed = len_path / sum_time

print("Средняя скорость : ", round(avg_speed, 2))