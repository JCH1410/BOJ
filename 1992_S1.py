import sys

input = sys.stdin.readline

n = int(input())
quads = [list(input().rstrip()) for _ in range(n)]
dir = [[0, 1], [1, 0], [1, 1]]


def quad_tree(y, x, num):
    if num == 1:
        return quads[y][x]
    output = ['(']
    now = quad_tree(y, x, num // 2)
    output.append(now)
    is_same = True
    for d in dir:
        dy, dx = y + d[0] * num // 2, x + d[1] * num // 2
        quad = quad_tree(dy, dx, num // 2)
        output.append(quad)
        if now != quad:
            is_same = False
    if is_same and (now == '0' or now == '1'):
        return now
    else:
        output.append(')')
        return ''.join(output)


result = quad_tree(0, 0, n)
print(result)