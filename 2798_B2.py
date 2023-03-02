n, m = map(int, input().split())
cards = list(map(int, input().split()))

max_sum = 0
for i in range(n):
    a = cards[i]
    for j in range(i + 1, n):
        b = cards[j]
        for k in range(j + 1, n):
            c = cards[k]
            card_sum = a + b + c
            if m >= card_sum > max_sum:
                max_sum = card_sum
print(max_sum)