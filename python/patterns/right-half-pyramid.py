rows = int(input())
k = 2 * rows - 2

for i in range(rows):
    for j in range(k):
        print(" ",end = "")
    k = k - 2
    for j in range(i + 1):
        print("* ", end = "")
    print("\r")
    
# for i in range(rows):
#     for j in range( rows - i):
#         print(" ", end = "")
#     for j in range(i + 1):
#         print("*", end = " ")
#     print("\r")
# for i in range(rows):
#     for j in range(i + 1):
#         print(" ", end = "")
#     for j in range(rows - i):
#         print("*", end = " ")
#     print("")

