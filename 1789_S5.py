n = int(input())
n_sum = 0
result = 0
num = 1
while n_sum <= n:
    n_sum += num
    num += 1
    result += 1
if n_sum > n:
    result -= 1

print(result)