rows = int(input())

for i in range(1, rows + 1):
    for j in range(1, rows + 1):
        if j <= 1:
            print(i, end = ' ')
        else:
            print(j, end = ' ')
    print("")        