import sys
import heapq

input = sys.stdin.readline

n = int(input())
nums = []
result = []
for _ in range(n):
    num = int(input())
    if num != 0:
        abs_num = abs(num)
        heapq.heappush(nums, (abs_num, num // abs_num))
    else:
        if not nums:
            result.append('0')
        else:
            pop_num, pm = heapq.heappop(nums)
            result.append(str(pop_num * pm))

print('\n'.join(result))