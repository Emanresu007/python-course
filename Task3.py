# -*- coding: utf-8 -*-
"""
Created on Sun May  2 13:45:51 2021

@author: Fetibek Aliev
"""

# загрузка модуля

from math import sqrt, pi, cos, asin, pow

# подключить модуль math или импортировать из него все нужные функции

x = float(input())

y = float(input())

# вычислить выражение, результат занести в переменную z        

z1 = asin(cos(x + (sqrt(3)/2) * pi))

z2 = 1.2 * sqrt(2 - pow(cos(y), 2))

z3 = pow(x, 2) + pow(y, 2) + 1


z = (z1 + z2)/ z3

print(round(z, 5))