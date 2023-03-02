import sys

input = sys.stdin.readline


def f11723_2():
    nums = [False] * 21
    m = int(input())
    for _ in range(m):
        order = list((input().split(' ')))
        if len(order) == 2:
            i = int(order[1])
            if order[0][0] == 'a':
                nums[i] = True
            elif order[0][0] == 'r':
                nums[i] = False
            elif order[0][0] == 'c':
                print(1 if nums[i] else 0)
            elif order[0][0] == 't':
                nums[i] = False if nums[i] else True

        else:
            if order[0][0] == 'a':
                nums = [True] * 21
            elif order[0][0] == 'e':
                nums = [False] * 21

f11723_2()




'''def f11723(command):
    order = list(command.split(' '))
    if order[0] == 'add':
        nums.add(int(order[1]))
    elif order[0] == 'remove':
        nums.discard(int(order[1]))
    elif order[0] == 'check':
        if int(order[1]) in nums:
            print(1)
        else:
            print(0)
    elif order[0] == 'toggle':
        if int(order[1]) in nums:
            nums.remove(int(order[1]))
        else:
            nums.add(int(order[1]))
    elif order[0] == 'all':
        nums.clear()
        for i in range(20):
            nums.add(i + 1)
    elif order[0] == 'empty':
        nums.clear()'''