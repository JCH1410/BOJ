import sys

input = sys.stdin.readline


def slug():
    a, b, v = map(int, input().split())
    if a >= v:
        return 1

    h = v - a
    days = h // (a - b)
    height = days * (a - b)

    while 1:
        days += 1
        height += a
        if height >= v:
            break
        height -= b
    return days


print(slug())