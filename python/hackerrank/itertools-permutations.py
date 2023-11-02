from itertools import permutations

# print(list(permutations(['1','2','3'],3)))

string = input()
num = int(input())

for i in permutations(string, num):
    # print(i)
    print("".join(i))