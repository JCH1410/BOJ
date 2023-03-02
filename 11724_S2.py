import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
lines = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
cnt = 0
visit_check = False
for _ in range(m):
    start, end = map(int, input().split())
    lines[start].append(end)
    lines[end].append(start)


def bfs(v):
    bfs_queue = deque([v])
    visited[v] = True
    while bfs_queue:
        now = bfs_queue.popleft()
        for p in lines[now]:
            if not visited[p]:
                visited[p] = True
                bfs_queue.append(p)


for i in range(1, n + 1):
    if not visited[i]:
        cnt += 1
        bfs(i)

print(cnt)