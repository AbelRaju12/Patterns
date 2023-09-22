import math
def is_palindrome(s):
    return s == s[::-1]

def lcm(a, b):
    return abs(a *  b) // math.gcd(a, b)

def hcf(a, b):
    return math.gcd(a,b)

def rotate(nums, k):
    k = k % len(nums)
    nums = nums [::-1]
    l, r = 0, k-1
    while l<r:
        nums[l], nums[r] = nums[r], nums[l]
        l += 1
        r -= 1
    
    l, r = k, len(nums)-1
    while l<r:
        nums[l], nums[r] = nums[r], nums[l]
        l += 1
        r -= 1
    return nums
        
print(rotate([1,2,3,4,5],2))