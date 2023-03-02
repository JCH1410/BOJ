import sys

input = sys.stdin.readline

n = int(input())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

for i in range(n):
    for a in range(n):
        for b in range(n):
            if graph[a][i] * graph[i][b] == 1:
                graph[a][b] = 1

for i in range(n):
    print(' '.join(list(map(str, graph[i]))))