from collections import deque

def bfs(a, b, cnt):
    queue = deque()
    queue.append((a, b, cnt))

    while queue:
        global result

        i, j, cnt = queue.popleft()
        if board[i][j] == 0:
            continue

        if i == N-1 and j == M-1:
            result = cnt
            return

        board[i][j] = 0

        for di, dj in dij:
            ni = i + di
            nj = j + dj

            if 0 <= ni < N and 0 <= nj < M and board[ni][nj] == 1:
                queue.append((ni, nj, cnt+1))


N, M = map(int, input().split())
board = [list(map(int, input())) for _ in range(N)]
dij = ((-1, 0), (0, 1), (1, 0), (0, -1))
result = 0

bfs(0, 0, 1)

print(result)