import sys

input = sys.stdin.readline

n, k = map(int, input().split())
lines = []
for _ in range(n):
    lines.append(int(input()))


def binary_search(arr, value):
    start, end = 1, max(arr)
    output = 0

    while start <= end:
        mid = (start + end) // 2
        if line_calculate(mid) >= value:
            output = mid
            start = mid + 1
        else:
            end = mid - 1

    return output


def line_calculate(num):
    output = 0
    for line in lines:
        output += (line // num)
    return output


result = binary_search(lines, k)
print(result)