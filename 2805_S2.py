import sys
from collections import Counter

input = sys.stdin.readline


n, m = map(int, input().split())
trees = list(map(int, input().split()))
trees = Counter(trees).items()
output = 0
start, end = 0, max(trees)[0]
while start <= end:
    mid = (start + end) // 2

    tree_sum = 0
    for tree, count in trees:
        cut = tree - mid
        if cut > 0:
            tree_sum += (cut * count)
    if tree_sum >= m:
        start = mid + 1
        output = mid
    else:
        end = mid - 1

print(output)