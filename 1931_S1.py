import sys

input = sys.stdin.readline
MAX_NUM = 2 ** 31

n = int(input())
times = dict()
meetings = []
for _ in range(n):
    a, b = map(int, input().split())
    if a == b:
        meetings.append((a, b))
    elif a in times and times[a] < b:
        continue
    else:
        times[a] = b
        meetings.append((a, b))
# meetings = dict(sorted(meetings.items()))
meetings.sort()

start = 0
end = MAX_NUM
cnt = 0
for m in meetings:
    if cnt == 0:
        start, end = m[0], m[1]
        cnt += 1
        continue

    m_s, m_e = m[0], m[1]
    if m_s >= end:
        start = m_s
        end = m_e
        cnt += 1
    else:
        if m_e <= end:
            start = m_s
            end = m_e
        else:
            continue

print(cnt)
