import re
string = '''
123-459-8755
800-922-8754
900-922-8754

'''

pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')
pattern = re.compile(r'\d\d\d[-.]\d\d\d[-.]\d\d\d\d')
pattern = re.compile(r'[89]00[-.]\d\d\d[-.]\d\d\d\d')


# matches = pattern.finditer(string)

# for match in matches:
#     print(match)
pattern = re.compile(r'[a-zA-Z]')
pattern = re.compile(r'[^a-zA-Z]')

# pattern = re.compile(r'[^b]at')

with open('data.txt', 'r') as f:
    contents = f.read()

    matches = pattern.finditer(contents)
    
    for match in matches:
        print(match)
