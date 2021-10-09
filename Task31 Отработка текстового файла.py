# -*- coding: utf-8 -*-
"""
Created on Thu Jul 29 15:38:52 2021

@author: Fetibek Aliev
"""

f = open("students.txt", "r", encoding = "utf-8-sig")



#список для фамилий
list_second_name = []

#список оценок по первой дисциплине
list_mark_1 =[]

for student in f:

    student_list = student.split()

    # заносим оценки в соответствующие переменные,
    # преобразуя их к целому типу
    mark_1 = int(student_list[1])
    mark_2 = int(student_list[2])
    mark_3 = int(student_list[3])

    # вычисляем среднюю оценку
    avg_mark = (mark_1 + mark_2 + mark_3) / 3

    print(student_list[0], ", средняя оценка : ", avg_mark)

    # добавляем очередную фамилию к списку
    list_second_name.append(student_list[0])

    # добавляем очередную оценку к списку
    list_mark_1.append(mark_1)

print("Список фамилий : ", list_second_name)

print("Список оценок по первой дисциплине : ", list_mark_1)

print("Средний балл по первой дисциплине : ", sum(list_mark_1)/len(list_mark_1))

f.close()