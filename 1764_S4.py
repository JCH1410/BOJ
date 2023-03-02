import sys

input = sys.stdin.readline

n, m = map(int, input().split())
people = dict()
result = []
cnt = 0
for _ in range(n):
    people[input().rstrip()] = True

for _ in range(m):
    name = input().rstrip()
    if people.get(name, False):
        result.append(name)
        cnt += 1

print(str(cnt))
result.sort()
print('\n'.join(result))