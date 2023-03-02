import sys

input = sys.stdin.readline


n = int(input())
xys = []
for _ in range(n):
    xy = list(map(int, input().split()))
    xys.append(xy)

xys.sort(key=lambda x:(x[1], x[0]))

result = []
for xy in xys:
    result.append(" ".join(map(str, xy)))
print("\n".join(result))
