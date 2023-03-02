import sys

input = sys.stdin.readline

n = int(input())
m = int(input())
word = list(input().rstrip())

result = 0
series = 0
prev = 0
for i in range(m):
    k = word[i]
    if k == 'I':
        if prev == 0:
            series += 1
        else:
            if series > n:
                result += (series - n)
            series = 1
        prev = 1
    else:
        if prev == 0:
            if series > n:
                result += (series - n)
            series = 0
        prev = 0
if series > 1 and series > n:
    result += (series - n)
print(result)