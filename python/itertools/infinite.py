from itertools import count, cycle, repeat

for i in count(10):
    print(i) #infinite prints from 10
    if i == 16:
        break
    
a = [2, 1, 3, 6, 5, 4]
count = 0
for i in cycle(a):
    print(i)
    count += 1
    if count == 10:
        break    

for i in repeat(1, 6):
    print(i) #prints 1 6 times