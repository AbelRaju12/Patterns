from itertools import accumulate
import operator

a = [2, 1, 3, 6, 5, 4]

acc = accumulate(a)
print(a)
print(list(acc)) #prints cumulative sum

acc = accumulate(a, func=operator.mul)
print(list(acc)) #prints cumulative sum

acc = accumulate(a, func=max)
print(list(acc)) #prints max value repeating until higher value

