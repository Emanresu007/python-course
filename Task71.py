# -*- coding: utf-8 -*-
"""
Created on Sat Oct  2 01:01:47 2021

@author: Fetibek Aliev
"""



class ExtendedStack(list):
    
    def sum(self):
        # операция сложения
        self.append(self.pop() + self.pop())
    
    def sub(self):
        # операция вычитания
        self.append(self.pop() - self.pop())
    
    def mul(self):
        # операция умножения
        self.append(self.pop() * self.pop())
    
    def div(self):
        # операция целочисленного деления
        self.append(self.pop() // self.pop())
        
        
        
        
        

x = ExtendedStack([1, 2, 3, 4, -3, 3, 5, 10])

x.div()



import time

class Loggable:
    def log(self, msg):
        print(str(time.ctime()) + ": " + str(msg))
        

class LoggableList(list, Loggable):
    def append(self, object):
        super().append(object)
        return Loggable.log(self, object)
    

x = Loggable()

x.log(2)

y = LoggableList()

y.append(5)

    
    