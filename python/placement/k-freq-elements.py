nums = [1,3,4,4,2,1,3,4,2,5,6,7,8,3,2,4,6,7,1,9,9,0,0]
k = 5

count = {}
for i in nums:
    count[i] = 1 + count.get(i, 0)

freq = [[] for i in range(len(nums) + 1)]

for n, c in count.items():
    freq[c].append(n)

print(freq)
res = []
for i in range(len(freq)-1,0,-1):
    for n in freq[i]:
        res.append(n)
        if len(res) == k:
            print(res)