from collections import OrderedDict

a = OrderedDict()

n =int(input())

for i in range(n):
    item, price = input().split()
    # a[item] = int(price)
    # print(a.get(item,0)) returns value for 'item previously in dict'
    a[item] = a.get(item,0) + int(price)



for item, price in a.items():
    print(item, price)