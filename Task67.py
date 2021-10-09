# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 00:58:34 2021

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


print(A.mro())


class MyList(list):
    def even_length(self):
        return len(self) % 2 == 0

x = MyList()
print(x)
x.extend([1, 2, 3, 4, 5])
print(x)
print(x.even_length())
x.append(6)
print(x.even_length())