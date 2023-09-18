def longestPalindrome(string):
    res = ""
    resLen = 0
    
    for i in range(len(string)):
        l, r = i, i
        while l >= 0 and r < len(string) and string[l] == string[r]:
            if (r -l + 1) > resLen:
                resLen = r - l + 1
                res = string[l: r + 1]            
            l -= 1
            r += 1
            
        l, r = i, i + 1
        while l >= 0 and r < len(string) and string[l] == string[r]:
            if (r -l + 1) > resLen:
                resLen = r - l + 1
                res = string[l: r + 1]            
            l -= 1
            r += 1
            
    return res

print(longestPalindrome("dfdsfifsjiosaaddaamalayalamdsuyfgs"))