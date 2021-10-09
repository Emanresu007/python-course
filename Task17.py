# -*- coding: utf-8 -*-
"""
Created on Wed May 12 08:43:40 2021

@author: Fetibek Aliev
"""

from math import atan, pi

def compute_population(t):
   N = (172/45) * ((pi/2) - atan((2000 - t)/45))
   return N  
   #вычислить численность населения для года t по формуле


#ввести строку с перечисленными через пробел годами
line = input()

# преобразовать строку в список из строковых значений годов
years_str_list = line.split()

# вычислить количество элементов в списке
n = len(years_str_list)

# сформировать список years_list на основе years_str_list, 
#преобразовав строковые значения в целые

years_list = [int(x) for x in years_str_list]

# создать список population_list, каждый элемент которого вычисляется 
# функцией compute_population от соответсвующего года из списка years_list

for x in years_list:
    N = compute_population(x)
    print("%5d - %6.3f миллиард(ов)" % (x,  N))

# в цикле для каждого года вывести численность населения, для вывода использовать 
# формат "%5d - %6.3f миллиард(ов)"