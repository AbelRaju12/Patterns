def characterReplacement(s, k):
    l=0
    res = 0
    max_val = 0
    char = {}
    for r in range(len(s)):
        char[s[r]] = 1 + char.get(s[r], 0)
        max_val = max(max_val, char[s[r]])
        while (r - l + 1) - max_val > k:
            l += 1
            char[s[l]] -= 1           
        res = max(res, r - l + 1)
    return res
s = "ABELRAJU"
result= characterReplacement(s, 1)
print(result)