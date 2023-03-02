import sys

input = sys.stdin.readline


n = input()
input_cards = list(input().split())
m = input()
counts = list(input().split())

cards = dict()
for card in input_cards:
    if card in cards:
        cards[card] += 1
    else:
        cards[card] = 1


result = ""
for num in counts:
    if num in cards:
        result += str(cards[num])
    else:
        result += '0'
    result += ' '
print(result)