import sys
from collections import deque

input = sys.stdin.readline


def DSLR():
    num, result = map(int, input().split())
    num_queue = deque([['', num]])
    visited = dict()
    visited[num] = True
    while num_queue:
        w, n = num_queue.popleft()

        n_d = (2 * n) % 10000
        if n_d == result:
            return w + 'D'
        if n_d not in visited:
            num_queue.append([w + 'D', n_d])
            visited[n_d] = True

        if n == 0:
            n_s = 9999
        else:
            n_s = (n - 1)
        if n_s == result:
            return w + 'S'
        if n_s not in visited:
            num_queue.append([w + 'S', n_s])
            visited[n_s] = True

        n_l = (n % 1000) * 10 + (n // 1000)
        if n_l == result:
            return w + 'L'
        if n_l not in visited:
            num_queue.append([w + 'L', n_l])
            visited[n_l] = True

        n_r = ((n % 10) * 1000) + n // 10
        if n_r == result:
            return w + 'R'
        if n_r not in visited:
            num_queue.append([w + 'R', n_r])
            visited[n_r] = True


t = int(input())
results = []
for _ in range(t):
    results.append(DSLR())
print('\n'.join(results))