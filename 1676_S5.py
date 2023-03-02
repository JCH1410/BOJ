import sys

input = sys.stdin.readline

n = int(input())

k = 5
ans = 0
while k <= n:
    for i in range(k, n + 1, k):
        ans += 1
    k *= 5

print(ans)
