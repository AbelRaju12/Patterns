# set = set()
# set.add('a')
# list = ['a', 'b', 'c', 'd', 'e']
# set = {i for i in list}
# set.add("a")
# print(set)
# set.discard('e')
# print(set)
# set2 = {'b', 'c', 'd', 'e', 'f', 'g', 'z'}
# print(set.intersection(set2))
# print(set.union(set2))
# print(set.difference(set2))

# n1 = int(input())
# set_a = set(map(int,input().split()))
# n2 = int(input())
# set_b = set(map(int,input().split()))
# a = (set_a.difference(set_b))
# b = (set_b.difference(set_a))
# ans = a.union(b)
# for i in sorted(ans):
#         print (i)


# N = int(input())
# country = set()
# for _ in range(N):
#     country.add(input())
# print(len(country))
    
num = int(input())
data = set(map(int, input().split()))
operations = int(input())

for x in range(operations):
  oper = input().split()
  if oper[0] == "remove":
    data.remove(int(oper[1]))
  elif oper[0] == "discard":
    data.discard(int(oper[1]))
  else:
    data.pop()
    
print(sum(data))