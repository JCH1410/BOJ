import sys
from collections import deque

input = sys.stdin.readline
visited = [False] * 200001


def f1697(num, target):
    if num == target:
        return 0
    t = 0
    start = num
    queue = deque([start])
    while True:
        t += 1
        d = deque()
        for _ in range(len(queue)):
            now = queue.popleft()
            if now >= 50000:
                print(now)
            a, b, c = 2 * now, now + 1, now - 1
            if a == target or b == target or c == target:
                return t
            if now < target and not visited[a]:
                visited[a] = True
                d.append(a)
            if now < target and not visited[b]:
                visited[b] = True
                d.append(b)
            if c >= 0 and not visited[c]:
                visited[c] = True
                d.append(c)
        queue += d


n, k = map(int, input().split())
print(f1697(n, k))
