import sys
from collections import deque

input = sys.stdin.readline

v = int(input())
vortex = [[] for _ in range(v + 1)]
vs = [True] * (v + 1)

for i in range(1, v + 1):
    connect = list(map(int, input().split()))
    index = i
    j = 1
    while connect[j] > 0:
        a, b = connect[j], connect[j + 1]
        vortex[index].append((a, b))
        vs[a] = False
        j += 2


def dfs(start):
    stack = deque([(start, 0)])
    visited = [False] * (v + 1)
    
