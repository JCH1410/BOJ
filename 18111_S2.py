import sys
from collections import Counter

input = sys.stdin.readline


n, m, b = map(int, input().split())
blocks = []
for _ in range(n):
    block = list(map(int, input().split()))
    blocks += block

lowest, highest = min(blocks), max(blocks)
blk_cnt = Counter(blocks)

ans = [99999999, -1]

for height in range(lowest, highest + 1):
    inventory = b
    days = 0
    for block in blk_cnt:
        need = (height - block) * blk_cnt[block]
        if need >= 0:
            days += need
            inventory -= need
        else:
            days += (-2 * need)
            inventory -= need

    if inventory >= 0 and height > ans[1] and days <= ans[0]:
        ans[0], ans[1] = days, height

print(' '.join(map(str, ans)))