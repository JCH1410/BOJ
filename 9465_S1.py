import sys

input = sys.stdin.readline

t = int(input())

def solution():
    n = int(input())
    stickers = []
    for _ in range(2):
        stickers.append(list(map(int, input().split())))

    if n == 1:
        return max(stickers[0][0], stickers[1][0])

    results = [[0 for _ in range(n)] for _ in range(2)]
    results[0][0] = stickers[0][0]
    results[1][0] = stickers[1][0]
    results[0][1] = stickers[0][1] + stickers[1][0]
    results[1][1] = stickers[1][1] + stickers[0][0]

    if n == 2:
        return max(results[0][1], results[1][1])
    
    for i in range(2, n):
        results[0][i] = stickers[0][i] + max(results[1][i - 1], results[0][i - 2], results[1][i - 2])
        results[1][i] = stickers[1][i] + max(results[0][i - 1], results[0][i - 2], results[1][i - 2])

    return max(results[0][n - 1], results[1][n - 1])

for _ in range(t):
    print(solution())