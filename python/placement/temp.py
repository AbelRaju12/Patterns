def fact(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    return fact
    
def count_perm(s):
    count = {}
    for i in s:
        count[s] = 1 + count.get(i, 0)
    
    fact1 = fact(len(s))
    
    val = 1
    
    for i,c in count.items():
        if c > 1:
            val = val * fact(c)
            
    return fact1 // val   

print(count_perm("eye"))  