class BadName(Exception):
    pass

def greet(name):
    if name[0].isupper() and len(name) > 4:
        return "Hello, " + name
    else:
        raise ValueError(name + " is inappropriate name")

print("Import is execution")