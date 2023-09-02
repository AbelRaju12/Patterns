def formatting(n):
    width = len(bin(n)[2:])
    for i in range(1, n + 1):
        print(str(i), oct(i).rjust(width), hex(i).upper().rjust(width), bin(i).rjust(width))
        # print(str(i), oct(i)[2:].rjust(width), hex(i)[2:].upper().rjust(width), bin(i)[2:].rjust(width))

n = int(input())
formatting(n)