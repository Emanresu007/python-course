
class BadName(Exception):
    pass
print(Exception.mro())

def greet(name):
    if name[0].isupper():
        return "Hello, " + name
    else:
        raise BadName(name + " is inappropriate name")

print(greet("Anton"))



try:
    for i in range(3):
        print(3/i)
except:
    print("Деление на 0")
    print("Исключение было обработано")


a, b = 1, 0
try:
    print(a/b)
    print("Это не будет напечатано")
    print('10'+10)
except TypeError:
    print("Вы сложили значения несовместимых типов")
except ZeroDivisionError:
    print("Деление на 0")


a, b = 1, 0
try:
   print(a/b)
except:
   print("Вы не можете разделить на 0")
print("Будет ли это напечатано?")


try:
    print('1'+1)
    print(sum)
    print(1/0)
except NameError:
    print("sum не существует")
except ZeroDivisionError:
    print("Вы не можете разделить на 0")
except:
    print("Что-то пошло не так...")


try:
    print('10'+10)
    print(1/0)
except (TypeError,ZeroDivisionError):
    print("Неверный ввод")

a,b=1, 0
try:
    if b==0:
        raise ZeroDivisionError
except:
   print("Деление на 0")
print("Будет ли это напечатано?")


assert(True)


try:
    print(1)
    assert 2+2==4
    print(2)
    assert 1+2==3
    print(3)
except:
    print("assert False.")
    raise
finally:
    print("Хорошо")
print("Пока")


class MyError(Exception):
    print("Это проблема")



def some_func(a = None, b = None):
    assert a or b, "Введите хотя бы одно значение!"

some_func(1)


class Person:

    def can_walk(self):
        print("Я могу ходить")

    def can_breath(self):
        print("Я могу дышать")

    def my_job(self):
        print("Моя профессия - ", self.job)


class Doctor(Person):
    job = "Доктор"

    def can_cure(self):
        print("Я могу лечить")


class Architect(Person):
    job = "Строитель"
    def can_build(self):
        print("Я могу строить")

d = Doctor()
d.can_cure()
d.can_walk()
d.my_job()

a = Architect()
a.can_build()
a.can_walk()
a.my_job()

class TooShortNameException(Exception):
    pass

def some_func(name):
    if len(name) < 3:
        raise TooShortNameException('Имя слишком короткое!')




