def merge_sort(a, p, r):
    if p < r:
        q = (p + r) // 2
        merge_sort(a, p, q)
        merge_sort(a, q+1, r)
        merge(a, p, q, r)


def merge(a, p, q, r):
    global c, re
    i = p
    j = q + 1
    t = 1
    tmp = [0] * (r - p + 2)
    while i <= q and j <= r:
        if a[i] <= a[j]:
            if tmp[t] == 0:
                c += 1
            tmp[t] = a[i]
            i += 1
        else:
            if tmp[t] == 0:
                c += 1
            tmp[t] = a[j]
            j += 1
        if c == k:
            re = tmp[t]
        t += 1
    while i <= q:
        if tmp[t] == 0:
            c += 1
        tmp[t] = a[i]
        if c == k:
            re = tmp[t]
        t += 1
        i += 1
    while j <= r:
        if tmp[t] == 0:
            c += 1
        tmp[t] = a[j]
        if c == k:
            re = tmp[t]
        t += 1
        j += 1
    i = p
    t = 1
    while i <= r:
        if tmp[t] == 0:
            c += 1
        a[i] = tmp[t]
        if c == k:
            re = tmp[t]
        i += 1
        t += 1


c = 0
re = 0
n, k = map(int, input().split())
arr = list(map(int, input().split()))
merge_sort(arr, 0, len(arr)-1)
if c < k:
    print(-1)
    exit(0)
print(re)