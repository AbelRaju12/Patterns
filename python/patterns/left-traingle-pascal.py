rows = int(input())

for i in range(rows):
    for j in range(rows - i):
        print(" ", end = " ")

    for k in range(i + 1):
        print("*", end = " ")
    print("")
    
for i in range(rows, 0, -1):
    for j in range(rows - i + 1): # rows - i + 2
        print(" ", end = " ")
    for k in range(i): # i - 1
        print("*", end = " ")
    print("")