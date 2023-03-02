import sys

input = sys.stdin.readline

n = int(input())
words = dict()
for _ in range(n):
    word = input().rstrip()
    drow = ''.join(reversed(word))
    if drow == word or drow in words:
        l = len(word)
        print(l, word[l//2])
    else:
        words[word] = True