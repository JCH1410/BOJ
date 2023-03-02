def factorial(num):
    if num < 2:
        return 1
    output = 1
    for i in range(1, num + 1):
        output *= i
    return output


def factorial2(a, b):
    output = 1
    num = a
    for _ in range(b):
        output *= num
        num -= 1
    return output


n, k = map(int, input().split())
print(factorial2(n, k) // factorial(k))