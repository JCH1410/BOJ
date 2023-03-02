import sys
from collections import deque
from collections import Counter


input = sys.stdin.readline


def printer_queue():
    n, m = map(int, input().split())
    priorities = list(map(int, input().split()))
    prt_cnts = Counter(priorities)
    prints = deque()
    for i in range(n):
        prints.append((i, priorities[i]))
    priorities = list(set(priorities))
    priorities.sort()
    priority_queue = deque(priorities)
    cnt = 0
    while True:
        max_priority = priority_queue.pop()
        prt_cnt = 0
        while prt_cnt < prt_cnts[max_priority]:
            if prints[0][1] == max_priority:
                prt_cnt += 1
                cnt += 1
                if prints[0][0] == m:
                    return cnt
                prints.popleft()

            elif prints[0][1] < max_priority:
                prints.append(prints.popleft())


tc = int(input())
for _ in range(tc):
    print(printer_queue())