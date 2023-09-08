def isvalidparenthesis(s):
    stack = []
    
    valid_parenthesis = {')': '(', '}': '{', ']': '['}
    
    for character in s:
        if character in valid_parenthesis.values():
            stack.append(character)
        elif character in valid_parenthesis.keys():
            if not stack or stack.pop() != valid_parenthesis[character]:
                return False
            
    return not stack

input_string = input()

if isvalidparenthesis(input_string):
    print("Valid")
else:
    print("Not Valid")