import sys
import heapq as hq

input = sys.stdin.readline
n = int(input())
direct = [[-1, 0], [0, -1], [0, 1], [1, 0]]
fishes = []
total_fish = 0
start_x, start_y = 0, 0
for i in range(n):
    fish = list(map(int, input().split()))
    fishes.append(fish)
    for j in range(n):
        if fish[j] == 9:
            start_x, start_y = j, i
        elif fish[j] > 0:
            total_fish += 1


def bfs(sx, sy):
    level = 2
    hungry = 0
    output = 0
    eat_fish = 0
    heap = []
    hq.heappush(heap, (0 * 10000 + sy * 100 + sx, sy, sx, level, 0))
    visited = [[False] * n for _ in range(n)]
    visited[sy][sx] = True
    fishes[sy][sx] = 0
    while heap:
        if eat_fish >= total_fish:
            break
        var, now_y, now_x, now_level, now_time = hq.heappop(heap)
        if 0 < now_level < level:
            hungry += 1
            eat_fish += 1
            output += now_time
            fishes[now_y][now_x] = 0
            if hungry == level:
                hungry = 0
                level += 1
            heap.clear()
            hq.heappush(heap, (0 * 10000 + now_y * 100 + now_x, now_y, now_x, level, 0))
            visited = [[False] * n for _ in range(n)]
            visited[now_y][now_x] = True
        else:
            for d in direct:
                dy, dx = now_y + d[0], now_x + d[1]
                if dy < 0 or dx < 0 or dy >= n or dx >= n:
                    continue
                if fishes[dy][dx] <= level and not visited[dy][dx]:
                    hq.heappush(heap, ((now_time + 1) * 10000 + dy * 100 + dx, dy, dx, fishes[dy][dx], now_time + 1))
                    visited[dy][dx] = True
    return output


print(bfs(start_x, start_y))