import sys
from collections import deque

input = sys.stdin.readline

m, n = map(int, input().split())
starts = []
tomatoes = []
days = [[(m * n) for _ in range(m)] for _ in range(n)]
ds = [[1, 0], [-1, 0], [0, 1], [0, -1]]
fresh = 0
success = True
for i in range(n):
    tomato = list(map(int, input().split()))
    tomatoes.append(tomato)
    for j in range(m):
        if tomato[j] == 1:
            starts.append((i, j, 0))
        elif tomato[j] == 0:
            fresh += 1


def bfs(arr):
    bfs_queue = deque(arr)
    visited = [[False for _ in range(m)] for _ in range(n)]
    if bfs_queue:
        visited[bfs_queue[0][0]][bfs_queue[0][1]] = True
    rotten = 0
    max_day = 0
    while bfs_queue:
        ny, nx, day = bfs_queue.popleft()
        for d in ds:
            dy, dx = ny + d[0], nx + d[1]
            if dy < 0 or dx < 0 or dy >= n or dx >= m:
                continue
            if not visited[dy][dx] and tomatoes[dy][dx] == 0:
                bfs_queue.append((dy, dx, (day + 1)))
                visited[dy][dx] = True
                rotten += 1
                if days[dy][dx] >= day + 1:
                    days[dy][dx] = day + 1
                    if day + 1 > max_day:
                        max_day = day + 1

    return rotten, max_day


rot, result = bfs(starts)
if rot < fresh:
    print(-1)
else:
    print(result)
