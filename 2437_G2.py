import sys

input = sys.stdin.readline

n = int(input())
coins = list(map(int, input().split()))
coins.sort()
coin_sum = 1
for coin in coins:
    if coin <= coin_sum:
        coin_sum += coin
    else:
        break
print(coin_sum)