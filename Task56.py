# -*- coding: utf-8 -*-
"""
Created on Sun Sep 19 12:51:18 2021

@author: Fetibek Aliev
"""

objects = input().split()

ans = 0

for i in range(len(objects)):
    objects_n = objects[:i+1]
    y = objects_n.count(objects[i])
    if y == 1:
       ans += 1
    else:
        ans += 0

print(ans)
