import sys
from collections import deque

input = sys.stdin.readline

def solution():
    n, m = map(int, input().split())
    result = []
    queue = deque()
    queue.append(([], 0))
    if m == 1:
        for i in range(n):
            result.append([i + 1])
        return result
    while queue:
        q, cnt = queue.popleft()
        if q:
            for i in range(q[-1] + 1, n + 1):
                if cnt + 1 == m:
                    result.append(q + [i])
                else:
                    queue.append((q + [i], cnt + 1))
        else:
            for i in range(1, n + 1):
                queue.append((q + [i], cnt + 1))
    return result

temp = solution()
output = []
for t in temp:
    num = map(str, t)
    output.append(' '.join(num))
print('\n'.join(output))
