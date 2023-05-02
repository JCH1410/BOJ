import sys

input = sys.stdin.readline
INF = int(1e9)

v, e = map(int, input().split())
start = int(input())
maps = [[] for _ in range(v + 1)]
distance = [INF] * (v + 1)
for _ in range(e):
    a, b, c = map(int, input().split())
    maps[a].append((b, c))
