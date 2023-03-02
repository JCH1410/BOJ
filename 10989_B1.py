import sys

input = sys.stdin.readline

n = int(input())
nums = [0] * 10001
for _ in range(n):
    nums[int(input())] += 1

for i in range(10001):
    if nums[i] != 0:
        str_i = str(i)
        while nums[i] > 1000:
            result = [str_i] * 1000
            print('\n'.join(result))
            nums[i] -= 1000
        result = [str_i] * nums[i]
        print('\n'.join(result))


'''nums = dict()
for _ in range(n):
    num = int(input())
    if num in nums:
        nums[num] += 1
    else:
        nums[num] = 1
nums = sorted(nums.items(), key=lambda x: x[0])

for num in nums:
    this_num = str(num[0]) + '\n'
    print(this_num * num[1], end='')'''
