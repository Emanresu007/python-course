# -*- coding: utf-8 -*-
"""
Created on Sun May  9 16:37:24 2021

@author: Fetibek Aliev
"""

v_raketa = float(input())

if v_raketa <=0:
    print("error")
    
else:
    
    if v_raketa > 0 and v_raketa <= 7.8:
        
        print("0")
        
    if v_raketa > 7.8 and v_raketa <= 11.2:
        
        print("1")
        
    if v_raketa > 11.2 and v_raketa <= 16.4:
        
        print("2")
        
    if v_raketa > 16.4:
        
        print("3")
        
