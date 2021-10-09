n = int(input())
list_class = []

for i in range(n):
    if i == 0:
        list_class.append("|")
        a = list(input().split())
        a.append("|")
        list_class.extend(a)
    else:
        a = list(input().split())
        a.append("|")
        x_a = a[0]

        try:
            x_a_index = list_class.index(x_a)
            print(x_a_index)
            list_class_index = list_class[:x_a_index]
            print(list_class_index)
            list_class_index.reverse()
            print(list_class_index)
            y_a_index = list_class_index.index("|")
            f_a_index = len(list_class_index) - y_a_index
            print(f_a_index)
            print(len(list_class_index))



            list_class_1 = list_class[:f_a_index]
            list_class_2 = list_class[f_a_index:]

            print(list_class_1)
            print(list_class_2)

            list_class_1.extend(a)
            list_class_1.extend(list_class_2)
            list_class = list_class_1
        except:
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