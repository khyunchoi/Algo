N, K = map(int, input().split())
things = [list(map(int, input().split())) for _ in range(N)]
board = [[0 for _ in range(K+1)] for _ in range(N)]

for i in range(N):
    W, V = things[i]

    for j in range(K+1):

        if i == 0:
            if j < W:
                board[i][j] = 0
            else:
                board[i][j] = V
        else:
            if j < W:
                board[i][j] = board[i-1][j]
            else:
                board[i][j] = max(board[i-1][j], V + board[i-1][j-W])

print(board[N-1][K])