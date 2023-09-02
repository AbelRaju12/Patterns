from collections import Counter

a = "aabbccdd"

my_counter = Counter(a)
print(my_counter) #Counter({'a': 2, 'b': 2, 'c': 2, 'd': 2})
print(my_counter.items()) #dict_items([('a', 2), ('b', 2), ('c', 2), ('d', 2)])
print(my_counter.keys()) #dict_keys(['a', 'b', 'c', 'd'])
print(my_counter.values()) #dict_values([2, 2, 2, 2])

a = "aaaaabbbbccdddddeeeeffghtyuabcd"

my_counter = Counter(a)

print(my_counter.most_common(1)) #[('a', 6)]
print(my_counter.most_common(1)[0]) #('a', 6)
print(my_counter.most_common(1)[0][0]) #a

print(list(my_counter.elements())) #converts it into a list and can be iterated