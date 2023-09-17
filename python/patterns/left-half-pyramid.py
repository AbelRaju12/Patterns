rows = int(input())
for i in range(rows):
    for j in range(i + 1):
        print("*", end = " ")
    print("\r")

print("")

for i in range(rows + 1, 0, -1):
    for j in range(i - 1):
        print("*", end=" ")
    print("")
    
# 1
# 2 1
# 3 2 1
# 4 3 2 1

# 5 4 3 2 1
# 4 3 2 1
# 3 2 1
# 2 1
# 1 use for j in range(i, 0, -1)