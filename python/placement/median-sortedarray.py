def mediansortedarray(nums1, nums2):
    A, B = nums1, nums2
    total = len(nums1) + len(nums2)
    half = total // 2
    
    if len(nums1) > len(nums2):
        A, B = nums2, nums1
        
    left = 0
    right = len(A) - 1 # [1(l), 2, 3, 4, 5(r)] of the smaller array
    
    while True:
        i = (left + right) // 2 #A
        j = half - i - 2 #B -2 is because of index of two arrays
        
        Aleft = A[i] if i >= 0 else float('-inf')
        Aright = A[i + 1] if (i + 1) < len(A) else float('inf')
        Bleft = B[j] if j >= 0 else float('-inf')
        Bright = B[j + 1] if (j + 1) < len(B) else float('inf')
        
        if Aleft <= Bright and Bleft <= Aright:
            #odd
            if total % 2:
                return min(Aright, Bright)
            return(max(Aleft, Bleft) + min(Aright, Bright)) / 2
        elif Aleft > Bright:
            right = i - 1
        else:
            left = i + 1
        
nums1 = [1, 3, 5, 6, 8]
nums2 = [2, 4, 6, 7]
median = mediansortedarray(nums1, nums2)
print("Median:", median)