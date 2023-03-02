from heapq import *
import sys

input = sys.stdin.readline

n = int(input())
max_heap = []
results = []
for _ in range(n):
    num = int(input())
    if num > 0:
        heappush(max_heap, (-num, num))
    else:
        if not max_heap:
            results.append('0')
        else:
            results.append(str(heappop(max_heap)[1]))

print('\n'.join(results))