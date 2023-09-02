from collections import defaultdict

d = defaultdict(list)
# d['python'].append('awesome')
# d['python'].append('awesomer')
# d['python'].append('awesomest')
# print(d)
input_n, input_m = map(int, input().split())
for i in range(input_n):
    ans1 = input()
    d[ans1].append(i+1)
# print(d)
for j in range(input_m):
    ans2 = input()
    if ans2 in d:
        print(*d[ans2])
    else:
        print(-1)