import re
n = int(input())
for i in range(0, n):
    try:
        experession = input()
        a = (re.compile(experession))
        print(bool(a))
    except re.error:
        print('False')
        

# for _ in range(int(input())):
#     print(re.search(r'^([-\+])?\d*\.\d+$', input()) is not None)