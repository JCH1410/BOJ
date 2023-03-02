import sys

input = sys.stdin.readline


def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


def lcm(a, b):
    return (a * b) // gcd(a, b)


def extended_euclid(a, b):
    s0, s1, t0, t1 = 1, 0, 0, 1
    r0, r1 = a, b
    while True:
        q = r0 // r1
        r1, r0 = r0 % r1, r1
        if r1 == 0:
            break
        s1, s0 = (s0 - s1 * q), s1
        t1, t0 = (t0 - t1 * q), t1
    return s1, t1


def calender():
    m, n, x, y = map(int, input().split())
    gcd_mn = gcd(m, n)
    if (abs(x - y)) % gcd_mn != 0:
        return '-1'
    if m == 1:
        return str(y)
    if n == 1:
        return str(x)
    lcm_mn = lcm(m, n)
    p, q = extended_euclid(m, n)
    output = (x * q * n // gcd_mn + y * p * m // gcd_mn)
    while output <= 0:
        output += lcm_mn
    if output != lcm_mn:
        output %= lcm_mn
    return str(output)


t = int(input())
result = []
for _ in range(t):
    result.append(calender())
print('\n'.join(result))