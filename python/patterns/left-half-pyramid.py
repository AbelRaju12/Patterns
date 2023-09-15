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