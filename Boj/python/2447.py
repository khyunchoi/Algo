def star(N, x, y, is_blank):
    if is_blank:
        for i in range(x, x+N):
            for j in range(y, y+N):
                board[i][j] = ' '
        return

    if N == 1:
        return

    size = N // 3
    cnt = 0
    for i in range(x, x+N, size):
        for j in range(y, y+N, size):
            cnt += 1
            if cnt == 5:
                star(size, i, j, True)
            else:
                star(size, i, j, False)


N = int(input())
board = [['*']*N for _ in range(N)]

star(N, 0, 0, False)
for i in range(N):
    for j in range(N):
        print(board[i][j], end='')
    print()