import heapq
import sys

heap_list = []

N = int(sys.stdin.readline())
for _ in range(N):
    x = int(sys.stdin.readline())

    if x == 0:
        if heap_list:
            print(heapq.heappop(heap_list))
        else:
            print(0)
    else:
        heapq.heappush(heap_list, x)
