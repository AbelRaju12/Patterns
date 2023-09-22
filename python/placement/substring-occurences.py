def find_substring(sentence, word):
    occurences = []
    i = 0
    while i < len(sentence):
        index = sentence.find(word, i)
        if index == -1:
            break
        occurences.append(index)
        i = index + 1
    return len(occurences)
# Example usage:
string = "Hello, Hello, Hello, WorlhelloeHellod!"
substring = "Hello"
result = find_substring(string, substring)
print(result)  # Output: [0, 7, 14]