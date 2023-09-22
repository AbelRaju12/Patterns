def longestCommonPrefix(str):
        str.sort()
        first = str[0]
        for i in range(1, len(str)):
            word = str[i]
            prefix = ""
            i = 0
            while i < len(first):
                if word[i] == first[i]:
                    prefix += word[i]
                    i += 1
                else:
                    break
            first = prefix
        return first
        
    
strs = ["flower","flow","flight"]
print(longestCommonPrefix(strs))