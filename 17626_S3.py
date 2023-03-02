'''import sys

input = sys.stdin.readline

n = int(input())
nums = [5] * (n + 1)
squares = []
i = 1
while i ** 2 <= n:
    num = i ** 2
    squares.append(num)
    nums[num] = 1
    i += 1

cnt = 1
for i in range(2, n + 1):
    if nums[i] == 1:
        cnt += 1
    else:
        for j in range(cnt):
            nums[i] = min(nums[i - squares[j]] + 1, nums[i])

print(nums[n])'''

import math


def four_square(n):
    if math.sqrt(n) == int(math.sqrt(n)):
        return 1

    for i in range(1, int(math.sqrt(n)) + 1):
        if math.sqrt(n - i ** 2) == int(math.sqrt(n - i ** 2)):
            return 2

    for i in range(1, int(math.sqrt(n)) + 1):
        for j in range(1, int(math.sqrt(n - i ** 2)) + 1):
            if math.sqrt(n - i ** 2 - j ** 2) == int(math.sqrt(n - i ** 2 - j ** 2)):
                return 3
    return 4


num = int(input())
print(four_square(num))


