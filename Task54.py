# -*- coding: utf-8 -*-
"""
Created on Sun Sep 19 10:17:01 2021

@author: Fetibek Aliev
"""

n = int(input())

n_list = []

for i in range(n):
    n_list.append(float(input()))

n_list_sum = sum(n_list)

print(n_list_sum)

