
def f(x, y):
    try:
        return x/y
    except TypeError:
        print("TypeError")
    except ZeroDivisionError:
        print('Zero Division Error')

print(f(1, 0))


def f(x, y):
    try:
        return x/y
    except (TypeError, ZeroDivisionError):
        print("Error :-(")

print(f(1, []))


def divide(x , y):
    try:
        result = x/y
    except ZeroDivisionError:
        print("ZeroDivisionErrod :(")
    else:
        print("result is", result)
    finally:
        print('finally')


divide(2, 1)
divide(2, 0)
divide(2, [])

print(ZeroDivisionError.__mro__)
print(ArithmeticError.mro())
print(AssertionError.mro())
print(ZeroDivisionError.mro())


try:
    foo()
except ZeroDivisionError:
    print("ZeroDivisionError")
except ArithmeticError:
    print("ArithmeticError")
except AssertionError:
    print("AssertionError")


