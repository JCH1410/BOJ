import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
tree = [[] for _ in range(n + 1)]
nodes = dict()

for _ in range(n - 1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

for i in range(n):
    nodes[i + 1] = 0

def bfs():
    queue = deque([1])
    visited = [False] * (n + 1)
    visited[1] = True
    while queue:
        q = queue.popleft()
        for t in tree[q]:
            if not visited[t]:
                nodes[t] = q
                queue.append(t)
                visited[t] = True

bfs()
result = []
for i in range(2, n + 1):
    result.append(str(nodes[i]))
print('\n'.join(result))