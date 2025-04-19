n = int(input())
paper = [
    list(map(int, input().split())) for _ in range(n)
]
blue = 0
white = 0


def divide_and_conquer(x, y, n):
    global blue, white
    same = paper[x][y]
    s = n//2
    for i in range(x, x+n):
        for j in range(y, y+n):

            if paper[i][j] != same:
                divide_and_conquer(x, y, s)
                divide_and_conquer(x+s, y, s)
                divide_and_conquer(x, y+s, s)
                divide_and_conquer(x+s, y+s, s)
                return

    if not same:
        white += 1
    else:
        blue += 1
    return


divide_and_conquer(0, 0, n)
print(white)
print(blue)