import sys
from collections import deque

input = sys.stdin.readline


def f1874():
    n = int(input())
    ans = deque()
    result = []
    cnt = 1
    for _ in range(n):
        num = int(input())
        while cnt <= num:
            ans.append(cnt)
            result.append("+")
            cnt += 1

        if ans[-1] == num:
            ans.pop()
            result.append("-")
        else:
            return "NO"
    return '\n'.join(result)


print(f1874())
