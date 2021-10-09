# -*- coding: utf-8 -*-
"""
Created on Sun May  9 14:48:55 2021

@author: Fetibek Aliev
"""

"""
Задача
Дан треугольник ABC на плоскости, заданный координатами своих вершин. 
Для этого треугольника вычислить:

-радиус вписанной в треугольник окружности;
-радиус описанной вокруг треугольника окружности;
-сумму длин трех медиан треугольника.

"""

# подключить модуль math или импортировать из него все нужные функции

from math import sqrt

# Длина сторон

def compute_len(x_0,y_0,x_1,y_1):
    
    len_line = sqrt((x_1 - x_0) ** 2 + (y_1 - y_0) ** 2)
    
    return len_line

def compute_median(x_1, x_2, x_3):
    
    median_line = 1/2 * sqrt(2 * (x_3**2 + x_2**2) - x_1**2)
    return median_line

x_a = float(input())

y_a = float(input())

x_b = float(input())

y_b = float(input())

x_c = float(input())

y_c = float(input())

# реализовать решение задачи

c = compute_len(x_a, y_a, x_b, y_b)

a = compute_len(x_b, y_b, x_c, y_c)

b = compute_len(x_a, y_a, x_c, y_c)

if a + b <= c or b + c <= a or a +c <= b:
    
    print("error")
    
else: 

    p = a + b + c

    r_v = sqrt((((p/2)-a)*((p/2)-b)*((p/2)-c))/(p/2))

    s = (p * r_v)/2

    r_o = (a * b * c)/(4 * s)

    a_median = compute_median(a, b, c)

    b_median = compute_median(b, c, a)

    c_median = compute_median(c, b, a)

    median_sum = a_median + b_median + c_median

# вывести результаты

    print(round(r_v, 4), round(r_o, 4), round(median_sum, 4))