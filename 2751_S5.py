"""def quick_sort(arr, low, high):
    if low >= high:
        return
    pivot = high
    a = low
    b = high - 1
    while a <= b:
        while arr[a] < arr[pivot] and a <= high:
            a += 1
        while arr[b] > arr[pivot] and b >= low:
            b -= 1
        if a > b:
            arr[a], arr[pivot] = arr[pivot], arr[a]
        else:
            arr[a], arr[b] = arr[b], arr[a]
    quick_sort(arr, low, a - 1)
    quick_sort(arr, a + 1, high)"""

import sys


def merge(arr, start, mid, end):
    temp = []
    a = start
    b = mid
    while a < mid and b <= end:
        if arr[a] <= arr[b]:
            temp.append(arr[a])
            a += 1
        else:
            temp.append(arr[b])
            b += 1
    while a < mid:
        temp.append(arr[a])
        a += 1
    while b <= end:
        temp.append(arr[b])
        b += 1
    index = start
    for n in temp:
        arr[index] = n
        index += 1


def merge_sort(arr, start, end):
    if start >= end:
        return
    mid = (start + end) // 2
    merge_sort(arr, start, mid)
    merge_sort(arr, mid + 1, end)
    merge(arr, start, mid + 1, end)


n = int(input())
nums = []
for _ in range(n):
    nums.append(int(sys.stdin.readline()))
merge_sort(nums, 0, n - 1)
for num in nums:
    print(num)
