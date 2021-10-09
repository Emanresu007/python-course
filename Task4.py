# -*- coding: utf-8 -*-
"""
Created on Mon May  3 01:22:48 2021

@author: Fetibek Aliev
"""

r_1 =float(input("Введите r_1 - "))

r_2 =float(input("Введите r_2 - "))

def compute_resist(r_1, r_2):

   r = r_1 * r_2 / (r_1 + r_2)

   return r

print(compute_resist(r_1, r_2))

