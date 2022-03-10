import sys
sys.setrecursionlimit(10**6)

def dfs(a, b):
    if board[a][b] == 0:
        return

    board[a][b] = 0

    for di, dj in dij:
        ni = a + di
        nj = b + dj

        if 0 <= ni < M and 0 <= nj < N and board[ni][nj] == 1:
            dfs(ni, nj)

T = int(input())
dij = ((-1, 0), (0, 1), (1, 0), (0, -1))

for _ in range(T):
    M, N, K = map(int, input().split())
    board = [[0 for _ in range(N)] for _ in range(M)]
    
    for _ in range(K):
        i, j = map(int, input().split())
        board[i][j] = 1

    result = 0

    for i in range(M):
        for j in range(N):
            if board[i][j]:
                dfs(i, j)
                result += 1

    print(result)