happiness = 0
n, m = map(int, input().split(' '))
elements_arr = list(map(int, input().split(' ')))

A = set(map(int, input().split(' ')))
B = set(map(int, input().split(' ')))

for i in elements_arr:
    if i in A:
        happiness += 1
    elif i in B:
        happiness -= 1
print(happiness)