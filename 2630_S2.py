import sys

input = sys.stdin.readline

n = int(input())
papers = []
for _ in range(n):
    papers.append(list(map(int, input().split())))
drcs = [[0, 1], [1, 1], [1, 0]]
kind = [0, 0]


def cut_paper(y, x, k):
    if k == 1:
        return papers[y][x]

    is_same = cut_paper(y, x, k // 2)
    results = [0, 0, 0]
    results[is_same] += 1
    output = 0
    for drc in drcs:
        dy, dx = y + drc[0] * k // 2, x + drc[1] * k // 2
        result = cut_paper(dy, dx, k // 2)
        if result > 1 or result != is_same:
            output = 2
        results[result] += 1
    if output == 2:
        for i in range(2):
            kind[i] += results[i]
    else:
        output = is_same
    return output


a = cut_paper(0, 0, n)
if a < 2:
    kind[a] += 1
for i in kind:
    print(str(i))