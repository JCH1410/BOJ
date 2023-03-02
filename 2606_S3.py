import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
connected = int(input())
pcs = [[] for _ in range(n + 1)]
for _ in range(connected):
    x, y = map(int, input().split())
    pcs[x].append(y)
    pcs[y].append(x)


def bfs(start):
    bfs_queue = deque([start])
    output = 0
    bfs_visited = [False] * (n + 1)
    bfs_visited[start] = True
    while bfs_queue:
        now_vortex = bfs_queue.popleft()
        for i in pcs[now_vortex]:
            if not bfs_visited[i]:
                bfs_queue.append(i)
                output += 1
                bfs_visited[i] = True
    print(output)


bfs(1)