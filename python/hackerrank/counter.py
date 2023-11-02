from collections import Counter

# list = list(map(int, input().split()))

# print(Counter(list))
# print(Counter(list).items(),
# Counter(list).keys(),
# Counter(list).values())

x = int(input())
y = Counter(map(int, input().split()))
z = int(input())

total = 0
for i in range(z):
    size, rate = map(int, input().split())
    if y[size]: 
        y[size] -= 1
        total += rate
print(total)