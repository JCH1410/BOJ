import sys

input = sys.stdin.readline


def fashion():
    output = 1
    n = int(input())
    cd = dict()
    lens = []
    for _ in range(n):
        clothes = list(input().rstrip().split(' '))
        if clothes[1] in cd:
            cd[clothes[1]].append(clothes[0])
        else:
            cd[clothes[1]] = [clothes[0]]
    for clothes in list(cd):
        output *= (len(cd[clothes]) + 1)
    return output - 1


t = int(input())
for _ in range(t):
    print(fashion())