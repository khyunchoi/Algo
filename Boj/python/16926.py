import copy
import sys

def spin(i, j, length, flag):
    if flag == 1:
        for a in range(i, i+length):
            new_board[a+1][j] = board[a][j]
    elif flag == 2:
        for a in range(j, j+length):
            new_board[i][a+1] = board[i][a]
    elif flag == 3:
        for a in range(i, i-length, -1):
            new_board[a-1][j] = board[a][j]
    elif flag == 4:
        for a in range(j, j-length, -1):
            new_board[i][a-1] = board[i][a]
    

N, M, R = map(int, input().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
new_board = [[0] * M for _ in range(N)]
R = R % ((N + M - 2) * 2)
num = min(N, M) // 2

for _ in range(R):
    i = 0
    j = 0
    tmp = N - 1
    for _ in range(num):
        spin(i, j, tmp, 1)
        i += 1
        j += 1
        tmp -= 2

    i = N-1
    j = M-1
    tmp = N - 1
    for _ in range(num):
        spin(i, j, tmp, 3)
        i -= 1
        j -= 1
        tmp -= 2

    i = N-1
    j = 0
    tmp = M - 1
    for _ in range(num):
        spin(i, j, tmp, 2)
        i -= 1
        j += 1
        tmp -= 2

    i = 0
    j = M-1
    tmp = M - 1
    for _ in range(num):
        spin(i, j, tmp, 4)
        i += 1
        j -= 1
        tmp -= 2

    board = copy.deepcopy(new_board)

for i in range(N):
    print(*board[i])