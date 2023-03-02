import random
import sys

input = sys.stdin.readline
MAX_NUM = 2 ** 31
min_heap = [MAX_NUM] * 100002
min_heap[0] = 0
result = []


def heap_append(num):
    min_heap[0] += 1
    i = min_heap[0]
    min_heap[i] = num
    if i == 1:
        return 0
    while min_heap[i] < min_heap[i // 2]:
        if i == 1:
            break
        min_heap[i], min_heap[i // 2] = min_heap[i // 2], min_heap[i]
        i //= 2


def heap_remove():
    if min_heap[0] == 0:
        result.append('0')
        return 0
    result.append(str(min_heap[1]))
    min_heap[1] = MAX_NUM
    min_heap[1], min_heap[min_heap[0]] = min_heap[min_heap[0]], min_heap[1]
    min_heap[0] -= 1
    i = 1
    while min_heap[i] > min_heap[2 * i] or min_heap[i] > min_heap[2 * i + 1]:
        if min_heap[2 * i] < min_heap[2 * i + 1]:
            min_heap[i], min_heap[2 * i] = min_heap[2 * i], min_heap[i]
            i = 2 * i
        else:
            min_heap[i], min_heap[2 * i + 1] = min_heap[2 * i + 1], min_heap[i]
            i = 2 * i + 1
        if i >= min_heap[0] or (2 * i) > 100000:
            break


n = int(input())
for _ in range(n):
    j = int(input())
    if j == 0:
        heap_remove()
    else:
        heap_append(j)
print('\n'.join(result))
'''test_arr = [i + 1 for i in range(100000)]
random.shuffle(test_arr)
for n in test_arr:
    heap_append(n)
for _ in range(100000):
    heap_remove()'''