n = int(input())
list_class = []

for i in range(n):
    if i == 0:
        list_class.append("|")
    a = list(input().split())
    a.append("|")
    list_class.extend(a)

print(list_class)

m = int(input())

for i in range(m):
    a = input().split()
    x = a[0]
    y = a[1]
    x_index = list_class.index(x)
    y_index = list_class.index(y)
    if x == y:
        print('Yes')
    elif x_index < y_index:
        print('Yes')
    else:
        print('No')
    print(x, y,  x_index , y_index)