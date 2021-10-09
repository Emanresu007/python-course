# -*- coding: utf-8 -*-
"""
Created on Sat Aug  7 22:56:27 2021

@author: Fetibek Aliev
"""

import numpy as np

a = np.array([1, 4, 5, 8], float)

print(a)

print(a[:2])

print(type(a))

print(a[3])

a[3] = 15

print(a)


b = np.array([[1,1,1], [2,2,2]], float)

print(b[1,2])

b.shape

b.dtype


10 in b

c = np.array(range(10), float)

print(c)

c = c.reshape((5, 2))

c.shape


print(list(c))


from array import array

numbers = array('i', [2,4,6,8])

print (numbers)

test = [1, 2, 3, 4, [5, 6, 7 ]]

print(test)

test1 = [1, 2, 3]

test2 = test1 + test1

print(test2)

name = ['fetibek', 'dasha', 'masha']

print('se[' in name)

if 'fetibek' not in name:
    print(1)
else:
    print(0)
    
kek = []

kek.append('хуй')

print(kek)

data
