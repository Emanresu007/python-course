# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 01:17:36 2021

@author: Fetibek Aliev
"""

class MoneyBox:
    def __init__(self, capacity):
        self.capacity = capacity
        self.c = 0

    def can_add(self, v):
        if  self.c  + v <= self.capacity:
            return True
        else:
            return False

    def add(self, v):
       if self.can_add(v) == True:
           self.c += v

c = MoneyBox(15)
c.add(5)

