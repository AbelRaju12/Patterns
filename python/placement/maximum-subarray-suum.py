def maxsubsum(array):
    
    if not array:
        return 0
    
    max_sum = current_sum = array[0]

    for num in array[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    
    return max_sum
        

array =[]
for i in range(int(input())):
    N = int(input())
    array.append(N)
    
result = maxsubsum(array)
print(result)