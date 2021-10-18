from collections import deque

def find_shark():
    for i in range(N):
        for j in range(N):
            if board[i][j] == 9:
                board[i][j] = 0
                return (i, j)


def bfs(i, j, cnt):
    global flag, tmp
    queue = deque()
    dij = [(-1, 0), (0, -1), (0, 1), (1, 0)]

    queue.append((i, j, cnt))
    visited[i][j] = 1

    while queue:
        i, j, cnt = queue.popleft()

        if 0 < board[i][j] < shark_size:
            if tmp == 0:
                tmp = cnt
            else:
                if tmp != cnt:
                    return

            tmp_result.append([i, j, cnt])

        for di, dj in dij:
            ni = i + di
            nj = j + dj

            if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj]:
                if board[ni][nj] <= shark_size:
                    visited[ni][nj] = 1
                    queue.append((ni, nj, cnt+1))
    
    if tmp == 0:
        flag = 0
    return


N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
shark_size = 2
shark_eat = 0
result = 0
flag = 1

while flag:
    i, j = find_shark()
    tmp = 0
    visited = [[0 for _ in range(N)] for _ in range(N)]
    tmp_result =[]
    bfs(i, j, 0)
    if tmp_result:
        tmp_result.sort(key=lambda x: (x[0], x[1]))
        i, j, cnt = tmp_result[0]
        result += cnt
        board[i][j] = 9
        
        shark_eat += 1
        if shark_eat == shark_size:
            shark_size += 1
            shark_eat = 0

print(result)