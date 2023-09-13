#longest substring without repeating characters
def longest_substring(s):
    if not s:
        return 0
    
    map = {}
    start = max_length = 0
    
    for i in range(len(s)):
        if s[i] in map and start <= map[s[i]]:
            start = map[s[i]] + 1
            # print(start)
        else:
            max_length = max(max_length, i - start + 1)
        map[s[i]] = i
        # print(map)

    return max_length

string_1 = "abelabelraju"
result  = longest_substring(string_1)
print(result)