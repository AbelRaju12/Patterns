def print_pascal_traingle(size):
    for i in range(0, size):
        for j in range( 0, i + 1):
            print(decide_number(i, j), end = ' ')
        print("")
        
def decide_number(i, j):
    num = 1
    if j > i - j:
        j = i - j
    for n in range(0, j):
        num = num * (i - n)
        num = num // (n + 1)
    return num

rows = int(input())
print_pascal_traingle(rows)
