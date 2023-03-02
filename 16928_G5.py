import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
ladders = dict()
snakes = dict()
for _ in range(n):
    start, end = map(int, input().split())
    ladders[start] = end
for _ in range(m):
    start, end = map(int, input().split())
    snakes[start] = end

nums = deque([[1, 0]])
visited = [False] * 101
visited[1] = True
while nums:
    p, cnt = nums.popleft()
    if p >= 94:
        print(cnt + 1)
        exit()
    is_ls = False
    for j in range(1, 7):
        i = j + p
        if i in ladders or i in snakes:
            is_ls = True
            break
    if not is_ls:
        for j in range(1, 7):
            visited[j + p] = True
        nums.append([p + 6, cnt + 1])
        continue
    for j in range(1, 7):
        i = j + p
        if i in ladders and not visited[i]:
            nums.append([ladders[i], cnt + 1])
            visited[ladders[i]] = True
            visited[i] = True
        elif i in snakes and not visited[i]:
            nums.append([snakes[i], cnt + 1])
            visited[i] = True
        elif not visited[i]:
            nums.append([i, cnt + 1])
            visited[i] = True

