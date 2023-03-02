import sys

input = sys.stdin.readline

n, m = map(int, input().split())
nums = [[0] * (n + 1) for _ in range(n + 1)]
for i in range(n):
    num = list(map(int, input().split()))
    for x in range(1, n):
        num[x] += num[x - 1]
    for x in range(1, n + 1):
        nums[i + 1][x] = nums[i][x] + num[x - 1]

def solution():
    x1, y1, x2, y2 = map(int, input().split())
    result = nums[x2][y2] - nums[x1 - 1][y2] - nums[x2][y1 - 1] + nums[x1 - 1][y1 - 1]
    return str(result)

answer = []
for _ in range(m):
    answer.append(solution())
print('\n'.join(answer))