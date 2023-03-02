import sys
import heapq as hq

input = sys.stdin.readline
n, d = map(int, input().split())
distance = [i for i in range(d + 1)]
shortcut = []
for _ in range(n):
    a, b, c = map(int, input().split())
    if b > d:
        continue
    hq.heappush(shortcut, (b, a, c))

for i in range(1, d + 1):
    distance[i] = distance[i - 1] + 1
    while shortcut and shortcut[0][0] == i:
        s, t, l = hq.heappop(shortcut)
        distance[i] = min(distance[i], distance[t] + l)

print(distance[d])