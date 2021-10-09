# -*- coding: utf-8 -*-
"""
Created on Sun Jul 11 21:26:05 2021

@author: Fetibek Aliev
"""

def pay_credit(S, n, k, t):
    y = S/n + (S - (t - 1) * S/n) * k/1200
    return y

S = int(input("Сколько на душу взял, Братишка? "))
n = int(input("На сколько лет умудрился? "))
k = int(input("И че, Баклан, каков процент? "))

credit_list = [i + 1 for i in range(0,n)]

print(credit_list)

credit_list_pay_credit = [pay_credit(S, n, k, t) for t in credit_list]

print(credit_list_pay_credit)

bank_income = sum(credit_list_pay_credit) - S

for i in range(len(credit_list)):

    print("%2d месяц - %8.2f руб" % (credit_list[i], credit_list_pay_credit[i]))

print("Доход банка - %6.2f руб" % bank_income)