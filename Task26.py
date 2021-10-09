# -*- coding: utf-8 -*-
"""
Created on Wed May 19 23:39:38 2021

@author: Fetibek Aliev
"""

def credit(t, S, n, k):
    
    p = (S/n) + (S - (t - 1) * (S/n)) * (k/(1200))
    
    return p

S = float(input())

n = int(input())

k = float(input())

t_list = [i + 1 for i in range(0,n)]

credit_list = [credit(t, S, n, k) for t in t_list]

bank_income = sum(credit_list) - S

for i in range(len(t_list)):

    print("%2d месяц - %8.2f руб" % (t_list[i], credit_list[i]))

print("Доход банка - %6.2f руб" % bank_income)