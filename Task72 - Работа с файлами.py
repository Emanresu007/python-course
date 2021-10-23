# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 22:21:27 2021

@author: Fetibek Aliev
"""

f = open("dataset_24465_4.txt", "r")

f_read = f.read()


f_splitline = f_read.splitlines()

f_splitline.reverse()

print(f_splitline)


j = "\n".join(f_splitline)

