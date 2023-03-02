string = list(input().rstrip())
zero_one = string[0]
cnt = [0, 0]
cnt[int(zero_one)] += 1
for i in range(1, len(string)):
    if string[i] != zero_one:
        zero_one = string[i]
        cnt[int(string[i])] += 1
print(min(cnt))