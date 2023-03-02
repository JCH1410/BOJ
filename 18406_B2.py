num = list(map(int, list(input().rstrip())))
if sum(num[:len(num)//2]) == sum(num[len(num)//2:]):
    print('LUCKY')
else:
    print('READY')