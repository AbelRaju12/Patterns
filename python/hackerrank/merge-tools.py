from collections import OrderedDict

def merge(string, k):
    i = 0
    while i < len(string):
        word = "".join(OrderedDict.fromkeys(string[i:i+k]))
        print(word)
        i += k
        
string, num = input(), int(input())
merge(string, num)