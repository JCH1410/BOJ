import sys

input = sys.stdin.readline


def num_sum(num):
    nums = str(num)
    result = num
    for i in nums:
        result += int(i)
    if result == n:
        return True
    else:
        return False


n = int(input())
n_range = len(str(n))
output = 0
for i in range(n - n_range * 9, n):
    if i < 0:
        continue

    if num_sum(i):
        output = i
        break
print(output)