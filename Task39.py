# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 12:17:13 2021

@author: Fetibek Aliev
"""

#E = input()
#n = input()
#a = input()
#b = input()

E = '150 132 110 186 103 229 179 224 230 113 224 202'
n = 148
a = 3.67
b = 4.83

energy = list(map(float, E.split()))
n = float(n)
a = float(a)
b = float(b)

energy_sum = sum(energy)

energy_norm = []

def f1(i, n):
    if i > n:
        y = n
    else:
        y = i
    return y

energy_norm = [f1(energy[i], n)
                  for i in range(len(energy))]


energy_unnorm = []

def f2(i, n):
    if i <= n:
        y = 0
    else:
        y = i - n
    return y

energy_unnorm = [f2(energy[i], n)
                  for i in range(len(energy))]

energy_norm_sum = sum(energy_norm) * a

energy_unnorm_sum = sum(energy_unnorm) * b

energy_sum_rub = energy_norm_sum + energy_unnorm_sum

print("Сумма: %6d кВт ч, стоимость %7.2f руб"
          % (energy_sum, energy_sum_rub))