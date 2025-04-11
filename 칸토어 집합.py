import sys

sys.setrecursionlimit(10**6)

def divide_and_conquer(c):
    for i in range(len(c) - 1):
        if c[i] == ' ':
            continue
        if c[i] == c[i+1] == '-':
            break
    else:
        return c
    for i in range(len(c) // 3, len(c) // 3 * 2):
        c[i] = ' '
    s = divide_and_conquer(c[:len(c) // 3])
    s2 = divide_and_conquer(c[len(c) // 3 * 2:])
    for i in range(len(s)):
        c[i] = s[i]
    for i in range(len(c) // 3 * 2, len(c)):
        c[i] = s2[i % len(s2)]
    return c


while True:
    try:
        n = int(input())
    except:
        break
    cantor = ['-' for _ in range((3 ** n))]
    print(''.join(divide_and_conquer(cantor)))