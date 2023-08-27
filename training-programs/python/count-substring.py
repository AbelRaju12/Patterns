def count_substring(string, sub_string):
    total = 0
    for i in range(len(string)):
        if string[i:len(string)].startswith(sub_string):
            total += 1
    return total

string = input().strip()
sub_string = input().strip()
    
count = count_substring(string, sub_string)
print(count)