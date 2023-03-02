import sys

input = sys.stdin.readline


n, r, c = map(int, input().split())
case = n - 1
x, y = 0, 0
stacks = []
while case >= 0:
    stack = 0
    case_by2 = 2 ** case

    if y <= r < y + case_by2:
        stack = 1
    else:
        stack = 3
        y += case_by2

    if c >= x + case_by2:
        stack += 1
        x += case_by2

    case -= 1
    stacks.append(stack)

k = n - 1
output = 0
for stack in stacks:
    output += (stack - 1) * (4 ** k)
    k -= 1

print(output)