# -*- coding: utf-8 -*-
"""
Created on Sun May  9 18:30:26 2021

@author: Fetibek Aliev
"""

year = int(input())

if year < 1582:
    print("error")
elif year % 4 != 0:
    print("365")
elif year % 100 == 0 and year % 400 != 0:
    print("365")
else:
    print("366")