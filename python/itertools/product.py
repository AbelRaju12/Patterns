from itertools import product

a = [1, 2, 3]
b = [4, 5, 6]

prod = product(a,b)

print(list(prod)) #carterian product

b = [4]
prod = product(a, b, repeat = 2)
print(list(prod))