import sys

input = sys.stdin.readline
t = int(input())
for _ in range(t):
    people = []
    n = int(input())
    output = n
    for _ in range(n):
        people.append(list(map(int, input().split())))
    people.sort()
    test = people[0][1]
    for i in range(1, n):
        if test < people[i][1]:
            output -= 1
        test = min(test, people[i][1])
    print(output)