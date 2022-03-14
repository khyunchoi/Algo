from collections import deque

def bfs(arr):
    global result

    queue = deque()
    for i, j, cnt in arr:
        queue.append((i, j, cnt))
    
    while queue:
        i, j, cnt = queue.popleft()
        if cnt > 0 and board[i][j] == 1:
            continue

        board[i][j] = 1
        result = cnt

        for di, dj in dij:
            ni = i + di
            nj = j + dj

            if 0 <= ni < N and 0 <= nj < M and board[ni][nj] == 0:
                queue.append((ni, nj, cnt+1))


M, N = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
dij = ((-1, 0), (0, 1), (1, 0), (0, -1))

result = 0
tomatoes = []
for i in range(N):
    for j in range(M):
        if board[i][j] == 1:
            tomatoes.append((i, j, 0))

bfs(tomatoes)

for i in range(N):
    for j in range(M):
        if board[i][j] == 0:
            result = -1
            break

    if result == -1:
        break

print(result)