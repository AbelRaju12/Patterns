def swapcase(word):
    string = ""
    for i in word:
        if i.isupper():
            string += i.lower()
        elif i.islower():
            string += i.upper()
        else:
            string += i
    return string

if __name__ =="__main__":
    word = input()
    new_word = swapcase(word)
    print(new_word)