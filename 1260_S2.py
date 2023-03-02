import sys
from collections import deque

input = sys.stdin.readline

n, m, v = map(int, input().split())
vortexes = [[] for _ in range(n + 1)]
for _ in range(m):
    vortex, to = map(int, input().split())
    vortexes[vortex].append(to)
    vortexes[to].append(vortex)

for vortex in vortexes:
    vortex.sort()


def dfs(start):
    dfs_stack = deque([start])
    dfs_output = [start]
    dfs_visited = [False] * (n + 1)
    dfs_visited[start] = True
    dfs_visited[0] = False
    while dfs_stack:
        now_vortex = dfs_stack.pop()
        for i in vortexes[now_vortex]:
            if not dfs_visited[i]:
                dfs_stack.append(now_vortex)
                dfs_stack.append(i)
                dfs_output.append(i)
                dfs_visited[i] = True
                break

    print(' '.join(map(str, dfs_output)))


def bfs(start):
    bfs_queue = deque([start])
    bfs_output = []
    bfs_visited = [False] * (n + 1)
    bfs_visited[start] = True
    while bfs_queue:
        now_vortex = bfs_queue.popleft()
        bfs_output.append(now_vortex)
        for i in vortexes[now_vortex]:
            if not bfs_visited[i]:
                bfs_queue.append(i)
                bfs_visited[i] = True
    print(' '.join(map(str, bfs_output)))


dfs(v)
bfs(v)
