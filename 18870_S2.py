import sys
from collections import Counter

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr_cnt = Counter(set(arr))
arr_cnt = sorted(arr_cnt.items())
arr_dict = dict()
total = 0
for num in arr_cnt:
    arr_dict[num[0]] = total
    total += num[1]
    

results = []
for num in arr:
    results.append(str(arr_dict[num]))
print(' '.join(results))