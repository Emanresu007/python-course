# -*- coding: utf-8 -*-
"""
Created on Sun May  9 19:19:25 2021

@author: Fetibek Aliev
"""

k = int(input())

if k < 1 or k > 99:
    print("ошибка")
elif k % 10 == 1 and k != 11: 
    print (k, "рубль")
elif k % 10 == 5 or k % 10 == 6 or k % 10 == 7 or k % 10 == 8 or k % 10 == 9 or k % 10 == 0 or k == 11 or k == 12 or k == 13 or k == 14:
     print (k, "рублей")
else:
    print (k, "рубля")