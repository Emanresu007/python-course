# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 21:06:32 2021

@author: Fetibek Aliev
"""



class EvenLengthMixin:
    def even_length(self):
        return len(self) % 2 == 0

class MyList(list, EvenLengthMixin):
    pass

print(MyList.mro())

x = MyList([1, 2, 3])
print(x.even_length())
x.append(4)
print(x.even_length())




class EvenLengthMixin:
    def even_length(self):
        return len(self) % 2 == 0

class MyList(list, EvenLengthMixin):
    pass

class MyDict(dict, EvenLengthMixin):
    pass

x = MyDict()
x["key"] = "value"
x["another key"] = "another value"
print(x.even_length())


class EvenLengthMixin:
    def even_length(self):
        return len(self) % 2 == 0

class MyList(list, EvenLengthMixin):
    def pop(self):
        x = super(MyList, self).pop()
        print("Last value is ", x)
        return x
    
ml = MyList([1, 2, 4 , 17])
z = ml.pop()

print(z)
print(ml)


class A:
   def foo(self):
      print("A")

class B(A):
   pass

class C(A):
   def foo(self):
      print("C")

class D:
   def foo(self):
      print("D")

class E(B, C, D):
   pass

E().foo()

print(E.mro())