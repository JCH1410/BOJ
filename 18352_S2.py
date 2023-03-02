import sys
import heapq as hq

input = sys.stdin.readline
INF = int(1e9)
n, m, k, x = map(int, input().split())
cities = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    cities[a].append([b, 1])
distance = [INF] * (n + 1)


def dijkstra(start):
    queue = []
    hq.heappush(queue, [0, start])
    distance[start] = 0
    while queue:
        dist, now = hq.heappop(queue) # start 에서 now 도시로 가는 거리가 dist
        if distance[now] < dist: # 저장된 start 에서 now 로 가는 거리가 dist 보다 짧으면 continue
            continue
        for c in cities[now]: # now 에서 갈 수 있는 도시들
            cost = dist + c[1] # cost = start ~ now 거리 + now ~ c 도시 거리
            if cost < distance[c[0]]:
                distance[c[0]] = cost
                hq.heappush(queue, [cost, c[0]])


dijkstra(x)
result = []
for i in range(1, n + 1):
    if distance[i] == k:
        result.append(i)
if not result:
    print(-1)
else:
    print('\n'.join(list(map(str, result))))