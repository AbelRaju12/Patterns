import re

string = '''
Hai my name is Abel Raju
abcdefghijklmnopqrstuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ

abelraju12@gmail.com
abel-raju@ceconline.edu
abel.raju@hotmail.net

Mr. Abel Raju
Mr Abdulla S
Ms Gouri G Varma
Mrs. Merin Mary Shibu
Mr G

haa ha haahaha
123456789
a
!@#$%^&*()_+}.{":>?<}

123-459-8755
800-922-8754
900-922-8754
123-569-8709

fsehdjlo5+665fsd65sdffsd
'''

pattern = re.compile(r'\d{3}[-.]\d{3}[-.]\d{4}')
pattern = re.compile(r'Mr\.?\s[A-Z]\w*') #.? ., \s is space, \w* 0 or more words
# pattern = re.compile(r'M(r|s|rs)\.?\s[A-Z]\w*')
pattern = re.compile(r'(Mr|Ms|Mrs)\.?\s[A-Z]\w*') 

pattern = re.compile(r'[a-zA-Z0-9.-]+@[a-zA-Z-]+\.(com|edu|net)') 

 

matches = pattern.finditer(string)

for match in matches:
    print(match)
