# -*- coding: utf-8 -*-
"""
Created on Sun May  9 23:31:59 2021

@author: Fetibek Aliev
"""

# deposit - сумма вклада, interest_rate -процентная ставка,
# amount_months - количество месяцев
def compute_income(deposit, interest_rate, amount_months):
    s = deposit * (1 + (interest_rate/(12 * 100)))**amount_months
    return s

x = float(input())

k = float(input())

n = int(input())

# вычислить прибыль с помощью функции

s = compute_income(x, k, n)

raznica = s - x

#вывести результат

print(round(raznica))