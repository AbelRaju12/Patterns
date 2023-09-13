import re

def is_match(s, p):
    
    match = re.match(p, s)
    # re.match(pattern, string)
    
    print(match.span()) # (0, 11)

    if match and match.span()[1] == len(s):
        return True
    else:
        return False

# Example usage
s = "mississippi"
p = "mis*is*ip*."
result = is_match(s, p)
print(result)
