import sys


def merge_sort(arr, start, end):
    if start >= end:
        return
    mid = (start + end) // 2
    merge_sort(arr, start, mid)
    merge_sort(arr, mid + 1, end)
    merge(arr, start, mid + 1, end)


def merge(arr, start, mid, end):
    merged = []
    a = start
    b = mid
    while a < mid and b <= end:
        if arr[a] <= arr[b]:
            merged.append(arr[a])
            a += 1
        else:
            merged.append(arr[b])
            b += 1
    for i in range(a, mid):
        merged.append(arr[i])
    for j in range(b, end + 1):
        merged.append(arr[j])
    for k in range(start, end + 1):
        arr[k] = merged.pop(0)


def bin_search(value, arr, start, end):
    a = start
    b = end
    while a <= b:
        mid = (a + b) // 2
        if arr[mid] == value:
            return 1
        elif value < arr[mid]:
            b = mid - 1
        elif value > arr[mid]:
            a = mid + 1
    return 0


n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
targets = list(map(int, sys.stdin.readline().split()))

merge_sort(nums, 0, n - 1)
for num in targets:
    print(bin_search(num, nums, 0, n - 1))