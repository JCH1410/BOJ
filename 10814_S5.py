import sys


input = sys.stdin.readline

members = []
for _ in range(int(input())):
    members.append(list(input().split()))

members.sort(key = lambda x : int(x[0]))
result = ""
for member in members:
    result += (member[0] + " " + member[1] + "\n")

print(result)