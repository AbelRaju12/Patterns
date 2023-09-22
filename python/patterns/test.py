n = 6
for i in range(n, 0, -1):
    # Print spaces before the first star
    for j in range(n - i):
        print(" ", end="")

    # Print stars for the left side of the hourglass
    for j in range(2 * i - 1):
        if j == 0 or j == 2 * i - 2 or i == n:
            print("*", end="")
        else:
            print(" ", end="")

    # Move to the next line
    print()

# Lower half of the hourglass
for i in range(2, n + 1):
    # Print spaces before the first star
    for j in range(n - i):
        print(" ", end="")

    # Print stars for the left side of the hourglass
    for j in range(2 * i - 1):
        if j == 0 or j == 2 * i - 2 or i == n:
            print("*", end="")
        else:
            print(" ", end="")

    # Move to the next line
    print()
