import sys

input = sys.stdin.readline


def ac(order, arr, length):
    os = list(order)
    nums = []
    is_int = False
    for num in arr:
        if num.isdigit():
            if is_int:
                nums.append(nums.pop() * 10 + int(num))
            else:
                nums.append(int(num))
                is_int = True
        else:
            is_int = False

    start = 0
    end = length - 1
    is_rvs = 1

    for o in os:
        if o == 'R':
            is_rvs *= -1
        else:
            if start > end:
                return 'error'
            if is_rvs == 1:
                start += 1
            else:
                end -= 1
    if start > end:
        return '[]'

    output = []
    if is_rvs == -1:
        for i in range(end, start - 1, -1):
            output.append(nums[i])
    else:
        for i in range(start, end + 1):
            output.append(nums[i])
    return str(output).replace(' ', '')


t = int(input())
result = []
for _ in range(t):
    p = list(input().rstrip())
    n = int(input())
    m = input().rstrip()
    result.append(ac(p, m, n))

print('\n'.join(result))