import sys

stk = []


def stack_command(command):
    order = list(command.split(' '))
    if order[0] == 'push':
        stk.append(int(order[1]))
    elif order[0] == 'pop':
        if not stk:
            print(-1)
        else:
            print(stk.pop(-1))
    elif order[0] == 'size':
        print(len(stk))
    elif order[0] == 'empty':
        if stk:
            print(0)
        else:
            print(1)
    elif order[0] == 'top':
        if not stk:
            print(-1)
        else:
            print(stk[-1])


n = int(sys.stdin.readline())
for _ in range(n):
    command = sys.stdin.readline()
    command = command.strip()
    stack_command(command)