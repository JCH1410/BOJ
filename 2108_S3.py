from collections import Counter
import sys

input = sys.stdin.readline


def f2108():
    n = int(input())
    nums = [int(input()) for _ in range(n)]
    nums.sort()
    nums_cnt = dict(Counter(nums))
    nums_cnt = sorted(nums_cnt.items(), key=lambda x: x[1], reverse=True)

    result = [0] * 4

    # 1 산술평균
    result[0] = round(sum(nums) / len(nums))

    # 2 중앙값
    result[1] = nums[len(nums) // 2]

    # 3 최빈값
    most_common = nums_cnt[0][1]
    most_commons = []
    for num_cnt in nums_cnt:
        if num_cnt[1] == most_common:
            most_commons.append(num_cnt[0])
        else:
            break

    if len(most_commons) > 1:
        most_commons.sort()
        result[2] = most_commons[1]
    else:
        result[2] = most_commons[0]

    # 4 범위
    result[3] = abs(nums[0] - nums[-1])

    for i in result:
        print(i)


f2108()