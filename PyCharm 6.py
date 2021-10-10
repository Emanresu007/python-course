
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

