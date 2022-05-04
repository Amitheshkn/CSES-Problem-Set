for i in range(1, int(input()) + 1):
    a = (i ** 2) * ((i ** 2) - 1) / 2
    b = 4 * (i - 1) * (i - 2)
    print(int(a - b))
