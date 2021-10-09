# -*- coding: utf-8 -*-
"""
Created on Mon May 10 14:05:54 2021

@author: Fetibek Aliev
"""

def compute_income(deposit, interest_rate, amount_months):
    s = deposit * (1 + (interest_rate/(12 * 100)))**amount_months
    return s

k = float(input()) # занести процент вклада
n = int(input()) # занести количество месяцев
p = float(input()) # занести прибыль

for x in range(37000, 38000):
    #вычислить прибыль для вклада x с помощью функции  compute_income(x, ..., ...)
    income = compute_income(x, k, n)
    pribl = round(income - x, 0)

    
    print(x, round(income, 0), pribl)