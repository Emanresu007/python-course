x = [-3, -2, -1, 0, 1, 2, 3]

y = [i * i for i in x if i < 0]

print(y)


z = [(a, b) for a in range(3) for b in range(3) if b >= a]

print(z)
