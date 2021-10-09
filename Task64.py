# -*- coding: utf-8 -*-
"""
Created on Sun Sep 26 21:42:59 2021

@author: Fetibek Aliev
"""

class MoneyBox:
    def __init__(self, capacity):
        self.capacity = capacity
        self.c = 0

    def can_add(self, v):
        if  self.c  + v <= self.capacity:
            self.y = True
            self.j = self.c  + v
            return True
        else:
            self.y = False
            self.j = self.c  + v
            return False
    
    def add(self, v):
        self.can_add(v)
        if self.y == True:
            self.c += v
            print(str(self.y))
        else:
            print(str(self.y))
            
c = MoneyBox(15)
c.add(5)