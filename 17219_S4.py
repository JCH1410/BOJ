import sys

input = sys.stdin.readline

n, m = map(int, input().split())
passwords = dict()
for _ in range(n):
    site, password = input().rstrip().split()
    passwords[site] = password

result = []
for _ in range(m):
    w = input().rstrip()
    result.append(passwords[w])
print('\n'.join(result))