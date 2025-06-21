M = 10**18 + 31
g = 42
n = int(input())

# 문제에서 알려준 값
a_n = 300  # a_1000000

if n == 1000000:
    print(a_n)
    exit()

if n > 1000000:
    print("n은 1000000 이하여야 합니다.")
    exit()

# a_1000000부터 역으로 a_n까지 계산 (n <= 1000000)
a = a_n
for _ in range(1000000 - n):
    a = pow(g, a, M)

print(a)
