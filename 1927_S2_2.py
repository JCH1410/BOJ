from heapq import heappush, heappop
import sys

input = sys.stdin.readline

n = int(input())
min_heap = []
results = []
for _ in range(n):
    num = int(input())
    if num > 0:
        heappush(min_heap, num)
    else:
        if not min_heap:
            results.append('0')
        else:
            results.append(str(heappop(min_heap)))

print('\n'.join(results))