def right_angle(arr):
    if arr[0]**2 + arr[1]**2 == arr[2]**2:
        return "right"
    else:
        return "wrong"


while 1:
    nums = list(map(int, input().split()))
    nums.sort()
    if nums.count(0) == 3:
        break
    print(right_angle(nums))