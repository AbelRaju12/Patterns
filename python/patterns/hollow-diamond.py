n = 7
# Upper half of the diamond
for i in range(1, n // 2 + 1):
    # Print spaces before the first asterisk
    for j in range(n // 2, i, -1):
        print(" ", end="")

    # Print the first asterisk
    print("*", end="")

    # Print spaces between the first and second asterisk
    for j in range(2 * i - 3):
        print(" ", end="")

    # Print the second asterisk or newline character
    if i != 1:
        print("*", end="")
    print()

# Middle line of the diamond
# print("*" * n)

# Lower half of the diamond
for i in range(n // 2, 0, -1):
    # Print spaces before the first asterisk
    for j in range(n // 2, i, -1):
        print(" ", end="")

    # Print the first asterisk
    print("*", end="")

    # Print spaces between the first and second asterisk
    for j in range(2 * i - 3):
        print(" ", end="")

    # Print the second asterisk or newline character
    if i != 1:
        print("*", end="")
    print()