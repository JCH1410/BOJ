import sys

input = sys.stdin.readline

n = int(input())
people = list(map(int, input().split()))
people.sort()

s = 0
result = 0
for p in people:
    s += p
    result += s
print(result)