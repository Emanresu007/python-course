# -*- coding: utf-8 -*-
"""
Created on Sat May 29 18:00:31 2021

@author: Fetibek Aliev
"""

f = open("test.txt", "r")
number_list = []

for line in f:
    number = float(line)
    number_list.append(number)

sum_number = sum(number_list)

print("sum = ", sum_number)

f.close()