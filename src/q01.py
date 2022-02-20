def print_stairs(num):
    c = 0
    while c <= num:
        print(('*' * c).rjust(num))
        c += 1


numberOfStairs = 5
print_stairs(numberOfStairs)
