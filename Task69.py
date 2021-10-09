# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 23:58:59 2021

@author: Fetibek Aliev
"""

class D: pass
class E: pass
class B(D, E): pass
class C: pass
class A(B, C): pass


print(issubclass(A, D))

print(issubclass(A, object))

print(issubclass(A, object))

x = A()

print(isinstance(x, E))
print(isinstance(x, E))