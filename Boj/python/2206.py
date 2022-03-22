from collections import deque

def bfs(i, j, skill, cnt):
    global result

    queue = deque()
    queue.append((i, j, skill, cnt))

    while queue:
        i, j, skill, cnt = queue.popleft()

        if visited[skill][i][j] == 1:
            continue

        visited[skill][i][j] = 1

        if i == N-1 and j == M-1:
            result = cnt
            return

        for di, dj in dij:
            ni = i + di
            nj = j + dj

            if 0 <= ni < N and 0 <= nj < M and not visited[skill][ni][nj]:
                if board[ni][nj] == 1 and skill == 1:
                    queue.append((ni, nj, 0, cnt+1))
                elif board[ni][nj] == 0:
                    queue.append((ni, nj, skill, cnt+1))


N, M = map(int, input().split())
board = [list(map(int, input())) for _ in range(N)]
visited = [[[0 for _ in range(M)] for _ in range(N)] for _ in range(2)]
dij = ((-1, 0), (0, 1), (1, 0), (0, -1))
result = -1

bfs(0, 0, 1, 1)

print(result)