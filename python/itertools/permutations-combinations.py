from itertools import permutations #ordering
from itertools import combinations, combinations_with_replacement #comb with spec length


a = [1, 2, 3]
b = [4, 5, 6]

perm = permutations(a)
print(list(perm)) #all orderings

perm = permutations(b, 2)
# print(list(perm)) #with length 2

comb = combinations(a, 2)
print(list(comb))

comb = combinations_with_replacement(a , 2)
print(list(comb))