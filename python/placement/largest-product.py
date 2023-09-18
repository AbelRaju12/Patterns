def maxProduct(nums):
    res = max(nums)
    currMin, currMax = 1, 1
    
    for i in nums:
        if i == 0:
            currMax, currMin = 1, 1
            continue
        temp = currMax * i
        currMax = max(currMax * i, currMin * i, i)
        currMin = min(temp, currMin * i, i)
        res = max(res, currMax)
    return res

nums = [ -1, 8, -2 , 4 , 6, -10, 3]
print(maxProduct(nums))        