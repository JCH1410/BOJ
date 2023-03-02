import sys
from collections import deque

input = sys.stdin.readline
brackets = ['(', ')', '[', ']']


def f4949(letters):
    queue = deque(letters.replace(' ', ''))
    check = deque()
    while queue:
        letter = queue.popleft()
        if letter == '(' or letter == '[':
            check.append(letter)
        if letter == ')':
            if not check or check[-1] != '(':
                return 'no'
            else:
                check.pop()
        if letter == ']':
            if not check or check[-1] != '[':
                return 'no'
            else:
                check.pop()

    if check:
        return 'no'
    else:
        return 'yes'


while True:
    sentence = input()
    if sentence == '.\n':
        break
    print(f4949(sentence))