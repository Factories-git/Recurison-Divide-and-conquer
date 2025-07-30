def matrix_multiply(arr1, arr2):
    ans = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for u in range(n):
                ans[i][j] += (arr1[i][u] * arr2[u][j]) % 1000000007
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


n = 2
m = int(input())
arr = [[1, 1], [1, 0]]
result = divide_and_conquer(arr, m)
for i in range(2):
    for j in range(2):
        result[i][j] %= 1000000007
print(result[1][0])