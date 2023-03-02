import sys
from collections import deque

input = sys.stdin.readline


k = int(input())
moneys = deque()
for _ in range(k):
    money = int(input())
    if money == 0:
        moneys.pop()
    else:
        moneys.append(money)

print(sum(moneys))