import sys

input = sys.stdin.readline


def hashing31(n, arr):
    mod13s = [0] * n
    output = 0
    if n <= 7:
        for i in range(n):
            mod13s[i] = (31 ** i)
            l2n = ord(arr[i]) - 96
            output += (l2n * mod13s[i])
    else:
        for i in range(7):
            mod13s[i] = (31 ** i)
            l2n = ord(arr[i]) - 96
            output += (l2n * mod13s[i])
        for i in range(7, n):
            if i % 2 == 1:
                mod13s[i] = mod13s[i // 2] * mod13s[(i // 2) + 1]
            else:
                mod13s[i] = mod13s[i // 2] * mod13s[i // 2]
            l2n = ord(arr[i]) - 96
            output += (l2n * mod13s[i])
    return output % 1234567891


n = int(input())
letters = list(input())
print(hashing31(n, letters))
