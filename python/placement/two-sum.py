def two_sum(numbers, target):
    num_dict = {}
    
    for i, num in enumerate(numbers):
        compliment = target - num
        
        if compliment in num_dict:
            # print(f"{num_dict[compliment]} {i}")
            return(num_dict[compliment], i) 
        
        num_dict[num] = i #stores the value as key
        # print(num_dict)
        
    return []

#you can use two for loop and brute force the solution

nums = [2, 8, 11, 15, 7]
target = 9
result = two_sum(nums, target)
if result:
    print(f"The indices of the two numbers that add up to {target} are: {result}")
else:
    print("No solution found.")

