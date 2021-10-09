# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 11:45:14 2021

@author: Fetibek Aliev
"""

t_0 = input()
t_12 = input()

t_avg = 4.5

t_0_List_float = list(map(float, t_0.split()))

t_12_List_float = list(map(float, t_12.split()))

t_avg_list = [(t_0_List_float[i] + t_12_List_float[i])/2
              for i in range(len(t_0_List_float))]

index = []

for i in t_avg_list:
        if i > t_avg:
            index.append(t_avg_list.index(i))
    
for i in index:
    print(i)