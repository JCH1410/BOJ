import sys

input = sys.stdin.readline

n = int(input())
m = int(input())
if m > 0:
    x_buttons = list(map(str, input().split()))
else:
    x_buttons = []


def remote_control_ans(channel):
    if channel == 100:
        return 0
    if len(x_buttons) == 10:
        return abs(100 - channel)

    c_len = len(str(channel))
    if not x_buttons:
        return min(c_len, abs(100 - channel))

    if len(x_buttons) == 9:
        for i in range(10):
            if str(i) not in x_buttons:
                x = str(i)
                break
        if c_len > 1:
            x_min = channel - int(x * (c_len - 1)) + c_len - 1
        else:
            x_min = abs(int(x) - channel) + 1
        x_mid = abs(int(x * c_len) - channel) + c_len
        if int(x) == 0:
            x_max = channel + 1
        else:
            x_max = int(x * (c_len + 1)) - channel + c_len + 1
        return min(x_min, x_mid, x_max, abs(channel - 100))

    c = channel
    output_plus = 999999999
    output_minus = -999999999
    while c < 10 ** (c_len + 1):
        arr_c = list(str(c))
        arr_c_len = len(arr_c)
        cnt = 0
        for num in arr_c:
            if num not in x_buttons:
                cnt += 1
        if cnt == arr_c_len:
            output_plus = c
            break
        else:
            c += 1

    c = channel
    while c >= 0:
        arr_c = list(str(c))
        arr_c_len = len(arr_c)
        cnt = 0
        for num in arr_c:
            if num not in x_buttons:
                cnt += 1
        if cnt == arr_c_len:
            output_minus = c
            break
        else:
            c -= 1
    output_plus = len(str(output_plus)) + output_plus - channel
    output_minus = len(str(output_minus)) + channel - output_minus
    return min(output_plus, output_minus, abs(channel - 100))


print(remote_control_ans(n))

