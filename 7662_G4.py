import sys
import heapq

input = sys.stdin.readline


def double_queue(num):
    max_heap = []
    min_heap = []
    popped = dict()
    heap_num = 0
    for _ in range(num):
        order = list(input().rstrip().split())
        n = int(order[1])
        if order[0] == 'I': # 입력
            heapq.heappush(max_heap, -n)
            heapq.heappush(min_heap, n)
            if n in popped:
                popped[n] += 1
            else:
                popped[n] = 1
            heap_num += 1
        else: # 출력
            if heap_num == 0: # 힙이 비었으면 패스
                continue
            if n == 1: # 최대값 출력
                pop = -heapq.heappop(max_heap)
                while popped[pop] == 0: # min_heap 에서 출력했던 정수라면 계속 heappop
                    pop = -heapq.heappop(max_heap)
                popped[pop] -= 1
            else: # 최소값 출력
                pop = heapq.heappop(min_heap)
                while popped[pop] == 0: # max_heap 에서 출력했던 정수라면 계속 heappop
                    pop = heapq.heappop(min_heap)
                popped[pop] -= 1
            heap_num -= 1
    if heap_num == 0:
        return "EMPTY"
    else:
        while max_heap and popped[-max_heap[0]] == 0:
            heapq.heappop(max_heap)
        while min_heap and popped[min_heap[0]] == 0:
            heapq.heappop(min_heap)
        return str(-max_heap[0]) + ' ' + str(min_heap[0])


t = int(input())
result = []
for _ in range(t):
    result.append(double_queue(int(input())))

print('\n'.join(result))