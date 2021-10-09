# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 12:56:00 2021

@author: Fetibek Aliev
"""
# input data

#S = input()
#n = input()
#k = input()

S = 1000000
n = 12
k = 15

# Preparing Data Sample

S = int(S)
n = int(n)
k = int(k)

def dif(S, n, k, t):
    y = (S/n) + (S - (t-1) * (S/n)) * (k/(1200))
    return y

list_k = [i
          for i in range(n)]

list_t = [i + 1
          for i in range(n)]

dif_list = [dif(S, n, k, list_t[i])
            for i in range(len(list_t))]

incom_dif = sum(dif_list) - S

def anu(S, n, k):
    ka = k/(12 * 100)
    y = ((ka * (1 + ka)**n)/((1 + ka)**n - 1)) * S
    return y

anu_list = [anu(S, n, k) 
            for i in range(n)]

incom_anu = sum(anu_list) - S

for i in list_k:
    print("%2d месяц - (диф.) %8.2f руб - (анн.) %8.2f руб"
          %(list_t[i], dif_list[i], anu_list[i]))    
print("Доход банка - (диф.) %6.2f руб - (анн.) %6.2f руб"
      %(incom_dif, incom_anu))