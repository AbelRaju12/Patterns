def characterReplacement(s, k):
    l=0
    res = 0
    char = {}
    for r in range(len(s)):
        char[s[r]] = 1 + char.get(s[r], 0)
        while (r - l + 1) - max(char.values()) > k:
            l += 1
            char[s[l]] -= 1           
        res = max(res, r - l + 1)
    return res
s = "ABELRAJU"
result= characterReplacement(s, 1)
print(result)