import sys
from collections import deque

input = sys.stdin.readline

ans_arr = deque()
in_arr = deque()
nums = deque()
result = ""
n = int(input())
nums_tf = [True] * (n + 1)
for i in range(n):
    ans_arr.append(int(input()))
    nums.append(i + 1)

while ans_arr:
    this_num = ans_arr.popleft()
    while nums_tf[this_num]:
        in_num = nums.popleft()
        in_arr.append(in_num)
        nums_tf[in_num] = False
        result += '+\n'
    if in_arr[-1] == this_num:
        in_arr.pop()
        result += '-\n'
    else:
        result = "NO"
        break

print(result)
