def gcd(n1, n2):
    a, b = n1, n2
    temp = 0
    while b != 0:
        a, b = b, a % b
    return a


def lcm(n1, n2):
    return n1 * n2 // gcd(n1, n2)


n, m = map(int, input().split())
print(gcd(n, m))
print(lcm(n, m))