from collections import deque

directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
count = 2


def bfs(box, start):
    queue = deque()
    queue.append(start)
    while queue:
        now_point = queue.popleft()
        box[now_point[0]][now_point[1]] = count
        for d in directions:
            dx = now_point[1] + d[1]
            dy = now_point[0] + d[0]
            if dx < 0 or dy < 0 or dx >= n or dy >= n:
                continue
            if box[dy][dx] == 1:
                box[dy][dx] = count
                queue.append([dy, dx])


n = int(input())
houses = []
for _ in range(n):
    houses.append(list(map(int, input())))

for i in range(n):
    for j in range(n):
        if houses[i][j] == 1:
            bfs(houses, [i, j])
            count += 1

complexes = [0] * (count - 1)
for i in range(n):
    for j in range(n):
        if houses[i][j] != 0:
            complexes[houses[i][j] - 1] += 1
complexes.sort()
complexes[0] = count - 2

for num in complexes:
    print(num)