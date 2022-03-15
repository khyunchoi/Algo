from collections import deque

def bfs(n, cnt):
    global result

    queue = deque()
    queue.append((n, cnt))

    while queue:
        m, count = queue.popleft()
        if m < 0 or m > 100000:
            continue
        
        if visited[m] == 1:
            continue

        visited[m] = 1

        if m == K:
            result = count
            return

        queue.append((m-1, count+1))
        queue.append((m+1, count+1))
        queue.append((m*2, count+1))


N, K = map(int, input().split())
result = 0
visited = [0 for _ in range(100001)]

bfs(N, 0)

print(result)