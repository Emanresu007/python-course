# -*- coding: utf-8 -*-
"""
Created on Sun Sep  5 20:14:24 2021

@author: Fetibek Aliev
"""

import math

def n(t):
    y = (172/45) * (math.pi / 2 - math.atan((2000 - t)/45))
    return y

ti = int(input("Введите нижний интервал "))
t2_1 = int(input("Введите верхний интервал "))
t2 = t2_1 + 1

years = [1000, 1750, 1800, 1850, 1900, 1950, 1955, 
         1960, 1965, 1970, 1975, 1980, 1985, 1990, 1995, 
         2000, 2005, 2010, 2011, 2012, 2013, 2014, 2015,
         2016, 2017, 2018, 2019]

population =[0.400, 0.791, 1.000, 1.262, 1.650, 2.519,
             2.756, 3.021, 3.335, 3.692, 4.068, 4.435, 4.831,
             5.264, 5.674, 6.071, 6.344, 6.933, 7.015, 7.100,
             7.162, 7.271, 7.358, 7.444, 7.530, 7.669, 7.763]  

test_population =[n(i) for i in years]

error_list = []

error_list = [abs((population[i] - test_population[i]) / population[i])
              for i in range(ti, t2)]

min_index = error_list.index(min(error_list)) + ti

min_error = years[min_index]

max_index = error_list.index(max(error_list)) + ti

max_error = years[max_index]

avg_error = (sum(error_list) / len(error_list)) * 100

print("Погрешность - минимальная, год: %4d, максимальная, год: %4d, средняя, процент: %6.3f"%(min_error, max_error, avg_error))