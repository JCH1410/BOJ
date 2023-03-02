import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def bfs(start):
    bfs_queue = deque([start])
    visited = [False] * (n + 1)
    cnt = [101] * (n + 1)
    cnt[start] = 0
    while bfs_queue:
        s = bfs_queue.popleft()
        for p in graph[s]:
            if not visited[p]:
                bfs_queue.append(p)
                visited[p] = True
                cnt[p] = min(cnt[p], cnt[s] + 1)
    return sum(cnt) - 101


result, result_bacon = 0, 101
for i in range(n):
    bacon = bfs(i + 1)
    if bacon < result_bacon:
        result, result_bacon = i + 1, bacon
    elif bacon == result_bacon:
        if i + 1 < result:
            result = i + 1

print(result)



