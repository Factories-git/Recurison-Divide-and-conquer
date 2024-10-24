def hanoi(n, start, mid, end):
    if n == 1:
        print(start, end)
    else:
        hanoi(n - 1, start, end, mid)
        print(start, end)
        hanoi(n - 1, mid, start, end)


num = int(input())
print(2 ** num - 1)
hanoi(num, 1, 2, 3)
