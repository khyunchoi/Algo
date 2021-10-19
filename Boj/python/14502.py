from itertools import combinations
import copy

def infection(i, j):
    dij = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    for di, dj in dij:
        ni = i + di
        nj = j + dj

        if 0 <= ni < N and 0 <= nj < M:
            if board[ni][nj] == 0:
                board[ni][nj] = 2
                infection(ni, nj)


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
origin_board = copy.deepcopy(board)

zero_list = []
two_list = []
for i in range(N):
    for j in range(M):
        if board[i][j] == 0:
            zero_list.append((i, j))
        if board[i][j] == 2:
            two_list.append((i, j))

result = 0
combi_list = list(combinations(range(len(zero_list)), 3))
for a, b, c in combi_list:
    board = copy.deepcopy(origin_board)
    i1, j1 = zero_list[a]
    i2, j2 = zero_list[b]
    i3, j3 = zero_list[c]
    board[i1][j1] = 1
    board[i2][j2] = 1
    board[i3][j3] = 1
    for i, j in two_list:
        infection(i, j)

    cnt = 0
    for i in range(N):
        for j in range(M):
            if board[i][j] == 0:
                cnt += 1
    
    result = max(result, cnt)

print(result)