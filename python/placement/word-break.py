def wordbreak(string, wordDict):
    dp = [False] * (len(string) + 1)
    dp[len(string)] = True
    
    for i in range(len(s) - 1, -1, -1):
        for w in wordDict:
            if (i + len(w) <= len(string) and string[i: i + len(w)] == w):
                dp[i] = dp [i + len(w)]
            if dp[i]:
                break
    
    # for i in range(len(s)):
    #     print(dp[i], end =" ")
            
    return dp[0]
        
# Example usage:
s = "leetcode"
wordDict = ["leet", "code"]
result = wordbreak(s, wordDict)

if result:
    print("The string can be segmented.")
else:
    print("The string cannot be segmented.")