a, b, c = map(int, input().split())
print(pow(a, b, c)) #메소드를 사용한 분할정복 거듭제곱
def myPower_while(a, b, c):
    #반복문을 사용한 분할정복 거듭제곱
    re = 1
    a %= c
    while b > 0:
        if b % 2 == 1:
            re = (re * a) % c
        b //= 2
        a = (a * a) % c
    return re
print(myPower_while(a, b, c))
def myPower_recursive(a, b, c):
    #재귀함수를 사용한 분할정복 거듭제곱
    a %= c
    if b == 0:
        return 1
    elif b % 2 == 1:
        half_pow = myPower_recursive(a, (b-1) // 2, c)
        return (half_pow * half_pow * a) % c
    else:
        half_pow = myPower_recursive(a, b // 2, c)
        return (half_pow * half_pow) % c


print(myPower_recursive(a, b, c))