rows = int(input())
for i in range(rows):
    print("")
    for j in range(i):
        print(" ", end = "")
    for k in range(rows - i):
        print("* ", end = "")
    
    
for i in range(rows):
    print("")
    for j in range(rows - i - 1):
        print(" ", end = "")
    for k in range(i + 1):
        print("* ", end = "")

    