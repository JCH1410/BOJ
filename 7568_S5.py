import sys

input = sys.stdin.readline


def f7568():
    n = int(input())
    rank = [1] * n
    people = [list(map(int, input().split())) for _ in range(n)]

    for i in range(n):
        base = people[i]
        for data in people:
            if data[0] > base[0] and data[1] > base[1]:
                rank[i] += 1

    print(' '.join(map(str, rank)))


f7568()