def divide_and_conquer(c):
    if len(c) == 1:
        return c
    for i in range(len(c) // 3, len(c) // 3 * 2):
        c[i] = ' '
    divide_and_conquer(c)



while True:
    try:
        n = int(input())
    except:
        break
    cantor = ['-' for _ in range((3 ** n))]
    print(divide_and_conquer(cantor))