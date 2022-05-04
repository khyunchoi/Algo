import heapq
import sys

min_heap_list = []
max_heap_list = []

N = int(sys.stdin.readline())
for _ in range(N):
    x = int(sys.stdin.readline())

    if min_heap_list and min_heap_list[0] < x:
        heapq.heappush(min_heap_list, x)
    else:
        heapq.heappush(max_heap_list, (-x, x))

    if len(max_heap_list) == len(min_heap_list) + 2:
        heapq.heappush(min_heap_list, heapq.heappop(max_heap_list)[1])
    elif len(max_heap_list) + 2 == len(min_heap_list):
        y = heapq.heappop(min_heap_list)
        heapq.heappush(max_heap_list, (-y, y))

    if len(max_heap_list) == len(min_heap_list):
        print(min(min_heap_list[0], max_heap_list[0][1]))
    elif len(max_heap_list) > len(min_heap_list):
        print(max_heap_list[0][1])
    else:
        print(min_heap_list[0])
