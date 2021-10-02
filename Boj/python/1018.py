N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]

result = N * M
cnt = 0
for i in range(N-7):
    for j in range(M-7):
        cnt = 0
        for x in range(i, i+8):
            for y in range(j, j+8):
                if (x+y) % 2 == 0 and board[x][y] == 'W':
                    cnt += 1
                elif (x+y) % 2 == 1 and board[x][y] == 'B':
                    cnt += 1
        if cnt > 32:
            cnt = 64 - cnt
        
        result = min(result, cnt)

print(result)