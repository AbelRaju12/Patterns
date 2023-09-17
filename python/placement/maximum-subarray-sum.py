def maxsubsum(array):
    maxSum = array[0]
    currSum = 0
    
    for n in array:
        if currSum < 0:
            currSum = 0
        currSum += n
        maxSum = max(maxSum, currSum)
    
    return maxSum
        

array =[1,2,-1,3,6,-7,8,-9,1,9,-10]
# for i in range(int(input())):
#     N = int(input())
#     array.append(N)
    
result = maxsubsum(array)
print(result)