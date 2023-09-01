from itertools import groupby

def smaller_than_3(a):
    return a < 3

a = [2, 1, 3, 6, 5, 4]

group_obj = groupby(a, key = smaller_than_3)
for key, value in group_obj:
    print(key, list(value))
    # True [2, 1]
    # False [3, 6, 5, 4]
    
group_obj = groupby(a, key = lambda x: x < 3)
for key, value in group_obj:
    print(key, list(value))
    
    
persons = [{'name':'Abel', 'age':21}, {'name':'Sanjay', 'age':21}, {'name':'Abdulla', 'age':25}, {'name':'Aron', 'age':24}]
group_obj = groupby(persons, key=lambda x: x['age'])
for key, value in group_obj:
    print(key, list(value))
    