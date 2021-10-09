# -*- coding: utf-8 -*-
"""
Created on Sun May  9 22:24:54 2021

@author: Fetibek Aliev
"""

h = int(input())
m = int(input())
s = int(input())

if h < 0 or h > 11:
    print("error")

elif m < 0 or m > 59:
    print("error")
    
elif s < 0 or s > 59:
    print("error") 

else:
    h_g = (360/12) * h
    m_g = (360/12)/60 * m
    s_g = (360/12)/60/60 * s
    
    gradus = h_g + m_g + s_g
    
    print(round(gradus, 2))