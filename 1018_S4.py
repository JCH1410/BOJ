import sys


input = sys.stdin.readline
n, m = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(input()))


def bw(x, y):
    output_b = 0
    output_w = 0

    # 처음이 B 기준(짝수가 B)
    for i in range(8):
        for j in range(8):
            if (i + j) % 2 == 0:
                if board[y + j][x + i] != 'B':
                    output_b += 1
                if board[y + j][x + i] != 'W':
                    output_w += 1
            else:
                if board[y + j][x + i] != 'W':
                    output_b += 1
                if board[y + j][x + i] != 'B':
                    output_w += 1
    return min(output_b, output_w)


values = []
for y in range(n - 7):
    for x in range(m - 7):
        values.append(bw(x, y))

print(min(values))