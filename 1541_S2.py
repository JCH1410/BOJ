import sys
from collections import deque

input = sys.stdin.readline

nums = list(input().rstrip().split('-'))
results = []
for num in nums:
    if num.isdigit():
        results.append(int(num))
    else:
        arr = list(map(int, num.split('+')))
        results.append(sum(arr))
output = 2 * results[0] - sum(results)
print(output)