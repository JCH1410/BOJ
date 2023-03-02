import sys
from collections import deque


def shuffle(arr):
    while len(arr) > 1:
        arr.popleft()
        arr.append(arr.popleft())
    return arr[0]


cards = deque([i + 1 for i in range(int(sys.stdin.readline()))])
print(shuffle(cards))