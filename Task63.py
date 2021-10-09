# -*- coding: utf-8 -*-
"""
Created on Sun Sep 26 17:47:26 2021

@author: Fetibek Aliev
"""

class Counter:
    def __init__(self):
        self.count = 0
    
    def inc(self):
        self.count += 1
        
    def reset(self):
        self.count = 0

x = Counter()

x.inc()

print(x.count)

Counter.inc(x)

print(x.count)

x.reset()

print(x.count)



class A:
    def __init__(self, val = 0):
        self.val = val
    def add(self, x):
        self.val +=x
    def print_val(self):
        print(self.val)


a = A()
b = A(2)
c = A(4)

a.add(2)
b.add(2)

a.print_val()
b.print_val()
c.print_val()        