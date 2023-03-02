import sys


input = sys.stdin.readline


'''n = int(input())
max_len = 0
words = [[] for k in range(51)]
for _ in range(n):
    word = input().replace("\n", "")
    i = len(word)
    if i > max_len:
        max_len = i
    if word not in words[i]:
        words[i].append(word)

result = ""
for j in range(max_len + 1):
    if words[j]:
        words[j].sort()
        for word in words[j]:
            result += (word + '\n')

print(result)'''

words = set()
for _ in range(int(input())):
    words.append(input().rstrip())
words = list(words)
words.sort()
words.sort(key = lambda x:len(x))