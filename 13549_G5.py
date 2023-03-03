from collections import deque

n, k = map(int, input().split())

def hns(n):
    queue = deque([(n, 0)])
    visited = dict()
    visited[n] = 0
    while queue:
        now, cnt = queue.popleft()
        if now == k or now * 2 == k:
            return cnt
        elif abs(now - k) == 1:
            return cnt + 1
        
        if ((2 * now) not in visited or visited[now * 2] > cnt) and now <= k:
            queue.append((now * 2, cnt))
            visited[now * 2] = cnt
        if (now - 1) not in visited or visited[now - 1] > cnt + 1:
            queue.append((now - 1, cnt + 1))
            visited[now - 1] = cnt + 1
        if ((now + 1) not in visited or visited[now + 1] > cnt + 1) and now <= k:
            queue.append((now + 1, cnt + 1))
            visited[now + 1] = cnt + 1

print(hns(n))
