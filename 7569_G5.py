import sys
from collections import deque

input = sys.stdin.readline

tomatoes = []
direct = [[1, 0, 0], [-1, 0, 0], [0, 1, 0], [0, -1, 0], [0, 0, 1], [0, 0, -1]]
m, n, h = map(int, input().split())
for _ in range(h):
    tomato = []
    for _ in range(n):
        tomato.append(list(map(int, input().split())))
    tomatoes.append(tomato)


# h, n, m 좌표 순서
def bfs():
    queue = deque()
    empty = 0
    origin = 0
    days = 0
    visited = []
    for i in range(h):
        v1 = []
        for j in range(n):
            v2 = []
            for k in range(m):
                if tomatoes[i][j][k] == 0:
                    v2.append(False)
                    empty += 1
                elif tomatoes[i][j][k] == 1:
                    queue.append([i, j, k, 0])
                    origin += 1
                    v2.append(True)
                else:
                    v2.append(True)
            v1.append(v2)
        visited.append(v1)

    if empty == 0:
        return 0

    while queue:
        t = queue.popleft()
        cnt = t[3]
        for d in direct:
            dh, dn, dm = t[0] + d[0], t[1] + d[1], t[2] + d[2]
            if dh < 0 or dh >= h or dn < 0 or dn >= n or dm < 0 or dm >= m:
                continue
            if not visited[dh][dn][dm]:
                visited[dh][dn][dm] = True
                days = cnt + 1
                empty -= 1
                queue.append([dh, dn, dm, cnt + 1])
    if empty > 0:
        return -1
    else:
        return days


print(bfs())

'''for i in range(h):
    for j in range(n):
        print(tomatoes[i][j])
print('--------------------------------')
for i in range(h):
    for j in range(n):
        print(visited[i][j])
print(empty)'''