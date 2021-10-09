# -*- coding: utf-8 -*-
"""
Created on Sun May  9 21:50:01 2021

@author: Fetibek Aliev
"""
from math import ceil

a = float(input())
b = float(input())
v = int(input())

if a <= 0:
    print("error")

elif b <= 0:
    print("error")
    
elif v <= 0:
    print("error")  

else:
    s = a**2 * 5
    rashod = s * b
    litr = rashod/1000
  
    col_banok = ceil(litr/v)

    print(col_banok)