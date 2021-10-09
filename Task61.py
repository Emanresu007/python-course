# -*- coding: utf-8 -*-
"""
Created on Sun Sep 26 11:59:06 2021

@author: Fetibek Aliev
"""

class MyClass:
    a = 10
    
    def func(self):
        print("hello")

print(MyClass.a)

x = MyClass()

print(type(x))

print(MyClass.func(x))

class Counter:
    pass

Counter
x = Counter()
x.count = 0
x.count +=1


class MyClass(object):
     i = 123
     def __init__(self):
         self.i = 345

a = MyClass()

print (a.i)

print (MyClass.i)
