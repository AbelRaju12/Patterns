def minion(s):
    vowel = 0
    consonant = 0
    
    for i in range(len(s)):
        if string[i] in ('aeiou' or 'AEIOU'):
            vowel += len(s) - i
        else:
            consonant += len(s) - i 
#  len(s) - i ==> if Banana is the word. for the 2nd i which is 'n', we have n, na, nan, nana 4 words which 6 - 2 = 4
            
    if vowel > consonant:
        print(f"Stuart {vowel}")
    elif consonant > vowel:
        print(f"Kevin {consonant}")
    else:
        print("Draw")

string = input()
minion(string)