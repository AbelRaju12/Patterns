rows = int(input())
for i in range(rows):
    print("")
    for j in range(rows - i):
        print(" ", end = "")
    for k in range(i + 1):
        print("* ", end = "")
for i in range(rows): #rows - 1
    print("")
    for j in range(i + 1): # i + 2
        print(" ", end = "")
    for k in range(rows - i): #rows - i - 1
        print("* ", end = "")
    
    
for i in range(rows):
    print("")
    for j in range(rows - i):
        print(" ", end = "")
    for k in range(i + 1):
        if( k == 0 or k == i):
            print("* ", end = "")
        else:
            print(" ", end = " ")
for i in range(rows): #rows - 1
    print("")
    for j in range(i + 1): # i + 2
        print(" ", end = "")
    for k in range(rows - i): #rows - i - 1
        if( k == 0 or k == rows - i - 1):
            print("* ", end = "")
        else:
            print(" ", end = " ")