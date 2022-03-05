from collections import deque

N = int(input())
arr = list(map(int, input().split()))
deq = deque()
results = []

for i in range(N-1, -1, -1):
    while deq:
        tmp = deq.pop()

        if tmp > arr[i]:
            results.append(tmp)
            deq.append(tmp)
            deq.append(arr[i])
            break

    if not deq:
        deq.append(arr[i])
        results.append(-1)

results.reverse()

print(*results)