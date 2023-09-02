def split_and_join(line):
    line_1 = line.split(" ")
    line_2 = " ".join(line_1)
    return line_2

def mutate_string(string, position, character):
    string_list = list(string)
    string_list[position] = character
    string_list = "".join(string_list)
    return string_list

if __name__ == '__main__':
    line = input()
    # result = split_and_join(line)
    result = mutate_string(line, 3, 'a')
    print(result)