def hansoo(num):
    num_list = list(map(int, str(num)))
    if num_list[2] - num_list[1] == num_list[1] - num_list[0]:
        return True
    else:
        return False


n = int(input())
count = 0
if n < 100:
    count = n
else:
    count = 99
    for num in range(100, n + 1):
        if hansoo(num):
            count += 1
print(count)