import sys

input = sys.stdin.readline

n = int(input())
drct = [-1, 0, 1]
a, b, c = map(int, input().split())
max_sum = [a, b, c]
min_sum = [a, b, c]

for i in range(n - 1):
    a, b, c = map(int, input().split())
    max0 = max(max_sum[0], max_sum[1]) + a
    max1 = max(max_sum) + b
    max2 = max(max_sum[1], max_sum[2]) + c
    max_sum = [max0, max1, max2]

    min0 = min(min_sum[0], min_sum[1]) + a
    min1 = min(min_sum) + b
    min2 = min(min_sum[1], min_sum[2]) + c
    min_sum = [min0, min1, min2]
print(max(max_sum), min(min_sum))