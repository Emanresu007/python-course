# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 23:06:13 2021

@author: Fetibek Aliev
"""
# Подключаем пакеты

import math

# Ввод данных

OX = '27 53 44 88 35 86 92 20 10 73 81'
OY = '97 22 57 58 37 55 34 29 80 55 71'
k = 7
r = 68

# Подготовка данных

OX_split_int = list(map(int, OX.split()))
OY_split_int = list(map(int, OY.split()))
k_int = int(k)
r_int = int(r)

# Выявление координат города откуда транслирует радиостанция
OX_k = OX_split_int[k_int]
OY_k = OY_split_int[k_int]

def f(x1, y1, xn, yn):
    f = math.sqrt((xn - x1)**2 + (yn - y1)**2)
    return f

rastoyanie = []

rastoyanie = [f(OX_k, OY_k, OX_split_int[i], OY_split_int[i]) 
                     for i in range(len(OX_split_int))]

rastoyanie_true = [rastoyanie[i] <= r_int
                   for i in range(len(rastoyanie))]

count_town = sum(rastoyanie_true)

print(count_town)