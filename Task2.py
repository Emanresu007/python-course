# -*- coding: utf-8 -*-
"""
Created on Sun May  2 11:02:53 2021

@author: Fetibek Aliev
"""

print("Ваше имя?")

name = input("Введите Ваше имя - ")

print("Привет, дорогой(ая) ", name, "!")

age = int(input("Сколько Вам полных лет, дорогой(ая) "))

height = float(input("Какой Ваш рост в метрах - "))

weight = float(input("Укажите Ваш вес в кг - "))

if age < 10 or height <= 0 or height > 3 or weight <= 0 or weight > 500:
    
    print("Ошибочные входные данные. Пожалуйста, проверьте данные и заполните форму снова. Спасибо!")
    
else:
    
    bmi = round(weight/ height ** 2, 0)

    print(name, ", Ваш индекс массы тела составляет: ", bmi)

    if bmi < 18.5:
        description = "недостаточной массой тела."
    elif bmi < 25:
        description = "нормальной массой тела."
    elif bmi < 30:
        description = "избыточной массой тела."
    else:
        description = "ожирением."

    print("Вы относитесь к группе людей с", description)  