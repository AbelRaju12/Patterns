import re

text_to_search = '''
Hai my name is Abel Raju
abcdefghijklmnopqrstuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ

haa ha haahaha
123456789
a
!@#$%^&*()_+}.{":>?<}

1234-569-87

fsehdjlo5+665fsd65sdffsd
'''

sentence = ' Start a sentence and bring it to an end'

# pattern = re.compile(r'abc')
# pattern = re.compile(r'$')
# pattern = re.compile(r'\.')
# pattern = re.compile(r'\d')
# pattern = re.compile(r'\bha') # words starting with ha

pattern = re.compile(r'\d\d\d\d.\d\d\d.\d\d') #. means any character

matches = pattern.finditer(text_to_search)
    
    
for match in matches:
    print(match)
    
# print(text_to_search[26:29])