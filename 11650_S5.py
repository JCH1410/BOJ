import sys


input = sys.stdin.readline


n = int(input())
xy = []
for _ in range(n):
    xy.append(list(map(int, input().split())))

xy.sort(key = lambda x : (x[0], x[1]))

result = ""
for num in xy:
    result += f'{num[0]} {num[1]}\n'
print(result)