x, y, w, h = map(int, input().split())

min_num = 9999
output = min(x - 0, w - x, y - 0, h - y)
print(output)