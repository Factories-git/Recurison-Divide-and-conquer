def matrix_multiply(arr1, arr2):
    ans = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for u in range(n):
                ans[i][j] += (arr1[i][u] * arr2[u][j]) % 1000
    return ans


def divide_and_conquer(matrix, multi):
    if multi == 1:
        return matrix
    if multi % 2 == 1:
        res_mat = divide_and_conquer(matrix, (multi-1) // 2)
        return matrix_multiply(matrix_multiply(res_mat, res_mat), matrix)
    else:
        res_mat = divide_and_conquer(matrix, multi // 2)
        return matrix_multiply(res_mat, res_mat)


n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
result = divide_and_conquer(arr, m)
for i in range(n):
    for j in range(n):
        result[i][j] %= 1000
    print(*result[i])