def split_and_join(line):
    line_1 = line.split(" ")
    line_2 = "-".join(line_1)
    return line_2

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
    
# def print_full_name(first, last):
#     print("Hello",first,f"{last}! You just delved into python.")

# def mutate_string(string, position, character):
#     s_list = list(string)
#     s_list[position] = character
#     string_ = "".join(s_list)
#     return string_