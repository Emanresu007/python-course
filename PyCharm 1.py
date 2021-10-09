try:
    x = [1 ,2 , 3, 1, 6 ,8]
    x.sort()
    print(x)

except TypeError:
    print(":(")

print ('Finish')


def f(x, y):
    try:
        return x/y
    except TypeError:
        print("TypeError")

f(5, [])