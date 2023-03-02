import sys
from collections import deque

input = sys.stdin.readline
queue = deque()


def queue_order(order):
    arr = list(order.split())
    if arr[0] == 'push':
        queue.append(int(arr[1]))
    elif arr[0] == 'pop':
        if queue:
            print(queue.popleft())
        else:
            print(-1)
    elif arr[0] == 'size':
        print(len(queue))
    elif arr[0] == 'empty':
        print(0 if queue else 1)
    elif arr[0] == 'front':
        print(queue[0] if queue else -1)
    elif arr[0] == 'back':
        print(queue[-1] if queue else -1)


for _ in range(int(input())):
    queue_order(input())