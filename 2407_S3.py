n, m = map(int, input().split())
m = min(m, (n - m))
up, down = 1, 1
for i in range(m):
    up *= (n - i)
    down *= (m - i)
print(up // down)