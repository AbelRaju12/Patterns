x = int(input())
y = int(input())
z = int(input())
n = int(input())
L =[]
for i in range(x+1):
    for j in range(y+1):
        for k in range(z+1):
            if(i+j+k != n):
                L.append([i,j,k])
print(L)           

# print(list([i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1)  if i+j+k !=n))