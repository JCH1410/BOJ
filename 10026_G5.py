import sys
from collections import deque

input = sys.stdin.readline


n = int(input())
colors_rgb = []
colors_rb = []
direct = [[1, 0], [-1, 0], [0, 1], [0, -1]]
for _ in range(n):
    color = input().rstrip()
    colors_rgb.append(list(color))
    colors_rb.append(list(color.replace('G', 'R')))
visited = [[False for _ in range(n)] for _ in range(n)]


def bfs(y, x, c, graph):
    queue = deque([[y, x]])
    visited[y][x] = True
    while queue:
        now = queue.popleft()
        for d in direct:
            dy, dx = d[0] + now[0], d[1] + now[1]
            if dy < 0 or dy >= n or dx < 0 or dx >= n:
                continue
            if not visited[dy][dx] and c == graph[dy][dx]:
                queue.append([dy, dx])
                visited[dy][dx] = True


rgb_cnt = 0
rb_cnt = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i, j, colors_rb[i][j], colors_rb)
            rb_cnt += 1

visited = [[False for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i, j, colors_rgb[i][j], colors_rgb)
            rgb_cnt += 1

print(rgb_cnt, rb_cnt)