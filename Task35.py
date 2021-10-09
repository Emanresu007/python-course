# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 19:11:55 2021

@author: Fetibek Aliev
"""

t_0 = '3.4 0.7 2.0 0.4 2.5 2.6 1.7 0.2 4.0 2.5'
t_12 ='6.4 8.3 6.8 6.7 7.4 6.4 8.9 4.7 5.3 7.6'

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