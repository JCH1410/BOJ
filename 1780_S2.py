import sys

input = sys.stdin.readline
drcs = [[-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1]]
n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))
nums = [0, 0, 0]


def papers(y, x, k):
    if k == 1:
        return arr[y][x]

    else:
        output = True
        output_nums = [0, 0, 0]
        is_same = papers(y, x, k // 3)
        if is_same < 2:
            output_nums[is_same + 1] += 1
        for drc in drcs:
            dy, dx = drc[0] * k // 3, drc[1] * k // 3
            num = papers(y + dy, x + dx, k // 3)
            if num != is_same:
                output = 9
            if num < 2:
                output_nums[num + 1] += 1
        if output == 9:
            for i in range(3):
                nums[i] += output_nums[i]
        else:
            output = is_same
        return output


a = papers(n // 2, n // 2, n)
if a < 2:
    nums[a + 1] += 1
print('\n'.join(map(str, nums)))

# print(y, x, k, output_nums, output)