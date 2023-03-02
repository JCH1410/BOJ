import sys
from collections import deque

input = sys.stdin.readline

def solution():
    n, m = map(int, input().split())
    cnt = m
    party = []
    group = [[] for _ in range(n + 1)]
    party.append(list(map(int, input().split())))

    if party[0][0] == 0:
        return m

    for i in range(m):
        member = list(map(int, input().split()))
        party.append(member)
        for j in range(1, member[0] + 1):
            group[member[j]].append(i + 1)

    queue = deque([0])
    v_people = [False] * (n + 1)
    v_party = [False] * (m + 1)
    v_party[0] = True
    while queue:
        now = queue.popleft()
        for i in range(1, party[now][0] + 1):
            p = party[now][i] # 사람
            if not v_people[p]:
                v_people[p] = True
                for g in group[p]:
                    if not v_party[g]:
                        v_party[g] = True
                        queue.append(g)
                        cnt -= 1
    return cnt

print(solution())