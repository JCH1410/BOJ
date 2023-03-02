import sys

input = sys.stdin.readline

n, m = map(int, input().split())
nums = [0]
input_nums = list(map(int, input().split()))
nums += input_nums
sums = [0] * (n + 1)
for i in range(1, n + 1):
    sums[i] = sums[i - 1] + nums[i]

results = []
for _ in range(m):
    start, end = map(int, input().split())
    result = sums[end] - sums[start - 1]
    results.append(str(result))

print('\n'.join(results))