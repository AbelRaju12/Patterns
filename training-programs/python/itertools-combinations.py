from itertools import combinations

# print(list(combinations(['1','2','3'],2)))

string = input()
num = int(input())

for i in combinations(string, num):
    print(i)
    # print("".join(i))
    
# for j in range(1, int(num)+1):
# for i in combinations(sorted(string), j):
#     print("".join(i))