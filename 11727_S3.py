import sys

input = sys.stdin.readline


def solution(num):
    tiles = [0 for _ in range(num + 1)]
    if num < 2:
        return num
    tiles[1] = 1
    tiles[2] = 3
    for i in range(3, num + 1):
        tiles[i] = tiles[i - 1] + 2 * tiles[i - 2]
    return tiles[num] % 10007


n = int(input())
print(solution(n))
