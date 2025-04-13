import sys

sys.setrecursionlimit(10**6)


n = int(input())
answer = [[' '] * n for _ in range(n)]


def star(i, j, p):
    if p == 1:
        answer[i][j] = '*'
        return

    p //= 3
    for r in range(3):
        for c in range(3):
            if r == 1 == c:
                continue
            star(i + r*p, j + c*p, p)


star(0, 0, n)
for row in answer:
    print(''.join(row))