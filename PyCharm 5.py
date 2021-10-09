def greet(name):
    if name[0].isupper():
        return "Hello, " + name
    else:
        raise ValueError(name + " is inappropriate name")

while True:
    try:
        name = input("Please enter your name, my Dear friend: ")
        greeting = greet(name)
        print(greeting)
    except ValueError:
        print("incorrect, Please try again your name with title first letter")
    else:
        break
