import sys

input = sys.stdin.readline

n = int(input())
rgb = [[0, 0, 0]]
for _ in range(n):
    rgb.append(list(map(int, input().split())))

for i in range(1, n + 1):
    for j in range(3):
        a = rgb[i][j] + rgb[i - 1][(j + 1) % 3]
        b = rgb[i][j] + rgb[i - 1][(j + 2) % 3]
        if a < b:
            rgb[i][j] = a
        else:
            rgb[i][j] = b

print(min(rgb[n]))