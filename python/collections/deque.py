from collections import deque

d = deque()

d.append(1)
d.append(2)
d.append(3)

print(d) #deque([1, 2, 3])

d.appendleft(4)
print(d) #deque([1, 2, 3])

d.pop()
print(d) #deque([1, 2, 3])

d.extend([1, 2, 5, 6])
print(d)

d.extendleft([3, 9, 0]) #deque([0, 9, 3, 4, 1, 2, 1, 2, 5, 6])
print(d)

d.rotate(2) #move elements 2 position to right
d.rotate(-1) #move element 1 position to left
print(d)


d.clear()
print(d)


d = deque()
for _ in range(int(input())):
    inp = input().split()
    getattr(d, inp[0])(*[inp[1]] if len(inp) > 1 else [])
print(*[item for item in d])
