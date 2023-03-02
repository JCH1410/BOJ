import sys

input = sys.stdin.readline

tetro = [[] for _ in range(19)]
tetro[0] = [[0, 0], [0, 1], [-1, 1], [-2, 1]]
tetro[1] = [[0, 0], [0, -1], [-1, -1], [-2, -1]]
tetro[2] = [[0, 0], [0, 1], [1, 1], [2, 1]]
tetro[3] = [[0, 0], [0, -1], [1, -1], [2, -1]]

tetro[4] = [[0, 0], [0, 1], [0, 2], [-1, 2]]
tetro[5] = [[0, 0], [0, -1], [0, -2], [-1, -2]]
tetro[6] = [[0, 0], [0, 1], [0, 2], [1, 2]]
tetro[7] = [[0, 0], [0, -1], [0, -2], [1, -2]]

tetro[8] = [[0, 0], [-1, 0], [-1, -1], [-2, -1]]
tetro[9] = [[0, 0], [-1, 0], [-1, 1], [-2, 1]]
tetro[10] = [[0, 0], [0, -1], [1, -1], [1, -2]]
tetro[11] = [[0, 0], [0, 1], [1, 1], [1, 2]]

tetro[12] = [[0, 0], [0, 1], [0, 2], [0, 3]]
tetro[13] = [[0, 0], [1, 0], [2, 0], [3, 0]]

tetro[14] = [[0, 0], [0, 1], [1, 1], [-1, 1]]
tetro[15] = [[0, 0], [0, -1], [1, -1], [-1, -1]]
tetro[16] = [[0, 0], [1, 0], [1, -1], [1, 1]]
tetro[17] = [[0, 0], [-1, 0], [-1, -1], [-1, 1]]

tetro[18] = [[0, 0], [0, 1], [1, 0], [1, 1]]

n, m = map(int, input().split())
answer = 0
nums = []
for _ in range(n):
    nums.append(list(map(int, input().split())))

for y in range(n):
    for x in range(m):
        for t in tetro:
            output = 0
            for i in range(4):
                dy, dx = y + t[i][0], x + t[i][1]
                if dy < 0 or dy >= n or dx < 0 or dx >= m:
                    output -= 4000
                    continue
                output += nums[dy][dx]
            if output > answer:
                answer = output

print(answer)