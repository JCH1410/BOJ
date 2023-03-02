import sys


input = sys.stdin.readline


def beehive():
    n = int(input())
    if n == 1:
        return 1
    result = 1
    while True:
        start = 3 * result * (result - 1) + 2
        end = start + 6 * result - 1
        if start <= n <= end:
            break
        result += 1
    return result + 1


print(beehive())


